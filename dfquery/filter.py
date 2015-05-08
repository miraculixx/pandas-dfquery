from dfquery.q import Q

class Filter(object):
    """
    Filter for Pandas DataFrames
    
    Allow keyword style filtering of dataframes:
    
    direct filtering
        filter = Filter(df, year=2015)
        filter.value
        
    filtering with Q objects
        q = Q(year=2015)
        filter = Filter(df, q)
        
    filtering with multiple Q objects
        q1 = Q(year=2015)
        q2 = Q(year=2014)
        filter = Filter(df, q1 | q2)
        
    filtering with filter() and exclude()
        filter = Filter(df, year=2015)
        filter.filter(month=1)
        filter.exclude(day=15)
    """
    _debug = False
    
    def __init__(self, df, query=None, **kwargs):
        self.df = df
        self.trace = False
        self.exc = None
        self.q = self.build_query(query, **kwargs)
        
    def build_query(self, query=None, **kwargs):
        if query:
            q = query
        else:
            q = Q(**kwargs)
        return q
        
    @property
    def query(self):
        return self.q
    
    def count(self):
        return len(self.value.index)
        
    @property
    def value(self):
        try:
            value = self.evalulate()
        except KeyError as e:
            self.exc = e
            if self.trace:
                raise
            raise SyntaxError('Error in Q object: column %s is unknown (KeyError on dataframe)' % e)
        return value
    
    def filter(self, query=None, **kwargs):
        self.q &= self.build_query(query, **kwargs)
        return self
        
    def exclude(self, query=None, **kwargs):
        self.q &= ~self.build_query(query, **kwargs)
        return self
            
    def evalulate(self):
        return self.q.apply_filter(self.df)
        
    def _repr_html_(self):
        return self.value._repr_html_()
        
    def __repr__(self):
        return self.value.__repr__()
        