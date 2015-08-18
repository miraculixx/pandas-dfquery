class Q(object):
    """
    Query object to filter dataframes
    
    A Q object holds the conditions. You can combine Q objects
    using & and | operators, e.g.
    
    q1 = Q(year=2015)
    q2 = Q(year=2014)
    q_all = q1 | q2
    
    Query objects are passed into a Filter, and evaluated when
    the filter's .value property is read. 
    
    Conditions specified in one Q object are AND together. Various
    operators can be specified using __<op> syntax, e.g. year__eq=2015.
    
    eq     ==  (default)
    lt     <
    lte    <=
    gt     >
    gte    >=
    ne     <>
    not    <>
    in     isin(v) 
    isin   isin(v)
    
    string operators
    
    isalnum   str.isalnum()
    isalpha   str.isalpha()
    isdigit   str.isdigit()
    isspace   str.isspace()
    islower   str.islower()
    isupper   str.isupper()
    istitle   str.istitle()
    isnumeric str.isnumeric()
    contains  str.contains(v)
    match     str.match(v)
    
    Evaluation works as follows:
    
    1. for each Q object, apply the filters as df[<conditions>]
    2. concatenate resulting truth table using the operators &, |
    3. return the dataframe as df[<joint conditions>]
    
    The following methods can be overriden:
    
    build_conditions - returns the truth table v.v. a dataframe for one Q object
    apply_conditions - returns df[<conditions>]
    apply_filter - for each Q object, call build_conditions, concatenate according
                   to the operators &, | then call apply_conditions 
                   
    """
    def __init__(self, **kwargs):
        self.conditions = kwargs
        self.qlist = [('&', self)]
        # should we return ~(conditions)
        self._inv = False
        
    def __repr__(self):
        r = []
        for op, q in self.qlist:
            r.append('%s %s' % (op, q.conditions))
        return 'Q %s' % ('\n'.join(r))
    
    def value(self, df):
        return self.build_conditions(df)
    
    def apply_filter(self, df):
        cond = None
        for i, (op, q) in enumerate(self.qlist):
            if i == 0:
                cond = q.build_conditions(df)
            elif op == '&':
                cond &= q.build_conditions(df)
            elif op == '|':
                cond |= q.build_conditions(df)
        return self.apply_conditions(df, cond)
    
    def apply_conditions(self, df, cond):
        return df[cond]
            
    def build_conditions(self, df):
        cond = [True] * len(df.index)
        for k, v in self.conditions.iteritems():
            if '__' in k:
                k, op = k.split('__')
            else:
                op = 'eq'
            # standard logical operators
            if op == 'eq':
                cond &= (df[k] == v)
            elif op == 'lt':
                cond &= (df[k] < v)
            elif op == 'lte':
                cond &= (df[k] <= v)
            elif op == 'gt':
                cond &= (df[k] > v)
            elif op == 'gte':
                cond &= (df[k] >= v)
            elif op == 'ne':
                cond &= (df[k] != v)
            elif op == 'not':
                cond &= (df[k] != v)
            elif op in ['in', 'isin']:
                cond &= (df[k].isin(v))
            # string processing
            elif op == 'isalnum':
                cond &= (df[k].str.isalnum()) if v else ~(df[k].str.isalnum())
            elif op == 'isalpha':
                cond &= (df[k].str.isalpha()) if v else ~(df[k].str.isalpha())
            elif op == 'isdigit':
                cond &= (df[k].str.isdigit()) if v else ~(df[k].str.isdigit())
            elif op == 'isspace':
                cond &= (df[k].str.ispace()) if v else ~(df[k].str.ispace())
            elif op == 'contains':
                cond &= (df[k].str.contains(v))
            elif op == 'match':
                cond &= (df[k].str.match(v))
            elif op == 'startswith':
                cond &= (df[k].str.startswith(v))
            elif op == 'endswith':
                cond &= (df[k].str.endswith(v))
            elif op == 'islower':
                cond &= (df[k].str.islower()) if v else ~(df[k].str.islower())
            elif op == 'isupper':
                cond &= (df[k].str.isupper()) if v else ~(df[k].str.isupper(v)) 
            elif op == 'istitle':
                cond &= (df[k].str.istitle()) if v else ~(df[k].str.istitle())
            elif op == 'isnumeric':
                cond &= (df[k].str.isnumeric()) if v else ~(df[k].str.numeric())
            elif op in ['isnone', 'isnull']:
                cond &= (df[k].isnull()) if v else ~(df[k].isnull())
            else:
                raise SyntaxError('Invalid operator %s on field %s' % (op, k))
        return ~cond if self._inv else cond
    
    def negate(self):
        self._inv = True
    
    def __and__(self, other):
        self.qlist.append(('&', other))
        return self
    
    def __or__(self, other):
        self.qlist.append(('|', other))
        return self
    
    def __invert__(self):
        """
        return an inverted version of this object
        """
        import copy
        obj = copy.deepcopy(self)
        obj.negate()
        return obj