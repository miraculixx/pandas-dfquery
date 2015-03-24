import six 

from dfquery.filter import Filter
import pandas as pd 


class QDataFrame(pd.DataFrame):
    """
    Drop-in replacement for DataFrame.query 
    
    use as
       qdf = QDataFrame(df)
       
    qdf.query supports the full Q / Filter semantics. It
    returns a new QDataFrame by default. If the QDF is lazy,
    it will return self instead.
    
    Note that query() calls build up a set of AND Filters. The
    underlying dataframe is not changed, but all conditions are
    applied whenever .value or __repr__ is called.
    
    Lazy evaluation (prototype)
    
    qdf.lazy()  sets lazy evalution. from here on, the
    query is only evaluated when repr or .value is called
    """
    _qfilter = None
    _lazy = False
    _debug = False
    
    def lazy(self, l=True):
        self._lazy = l
        return self
    
    def reset_query(self):
        self._qfilter = None
    
    def query(self, *args, **kwargs):
        query=kwargs.get('query', args[0] if len(args) > 0 else None)
        lazy=kwargs.get('lazy', False)
        reset=kwargs.get('reset', False)
        # check for string arguments to support Pandas DataFrame.query syntax
        # e.g. 'a > b' (compatibility) 
        if isinstance(query, six.string_types):
            return super(QDataFrame, self).query(query, **kwargs)
        # for Q objects or query by dictionary, apply a Filter
        kwargs['query'] = query 
        if not (lazy or self._lazy):
            qfilter = Filter(self, **kwargs)
            result = QDataFrame(qfilter.value)
        else:
            # lazy -- keep track of filters
            if not reset and self._qfilter:
                self._qfilter.filter(**kwargs)
            else:
                self._qfilter = Filter(self, **kwargs)
            result = self
        return result
    
    @property
    def value(self):
        if self._qfilter:
            return QDataFrame(self._qfilter.value)
        return self
    
    def __repr__(self):
        return super(QDataFrame, self.value).__repr__()
        
    def _repr_html_(self):
        return super(QDataFrame, self.value)._repr_html_()