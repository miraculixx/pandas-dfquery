.. _Django ORM queries: https://docs.djangoproject.com/en/1.7/topics/db/queries/#retrieving-specific-objects-with-filters

pandas-dfquery
--------------


Provides keyword-style queries on Pandas DataFrames -- see examples below. Inspired by `Django ORM queries`_


Why?
----

Ever got tired of writing code like this:

.. code:: python

    # standard subsetting syntax
    df[df.YEAR == 2015 & df.MONTH == 1]
    df[df.YEAR == 2015 & df.PRODUCT.str.contains('Fab')]
    # .query() style
    df.query('YEAR==2015 & MONTH==1')
    # -- uups, string functions raise an exception (Node call not implemented)
    df.query('df.YEAR == 2015 & df.PRODUCT.str.contains("Fab")'

and wish you could instead write:

.. code:: python

    df.query(YEAR=2015, MONTH=1)
    df.query(PRODUCT__contains='Fab')

Then pandas-dfquery is for you. See the tutorial below.

Tutorial
--------

.. code:: python

    from dfquery import QDataFrame, Q, Filter
    import pandas as pd
    import numpy as np
    
    # basic filtering
    iris = QDataFrame(pd.read_csv('https://raw.github.com/pydata/pandas/master/pandas/tests/data/iris.csv'))
    df = iris.query(SepalLength__gte=6.0, Name__contains='versicolor')
    df


.. code:: python

    # create Q objects as query terms, which are combinable by logical &, | 
    q_versi = Q(SepalLength__lt=6.0, Name__contains='versi')
    q_setosa = Q(SepalLength__lt=6.0, Name__contains='setosa')
    iris.query(q_versi & ~q_setosa)

.. code:: python

    # create Q objects as query terms, which are combinable by logical &, | 
    q_versi = Q(SepalLength__gt=6.0, Name__contains='versi')
    q_setosa = Q(SepalLength__lt=6.0, Name__contains='setosa')
    iris.query(q_versi | q_setosa)


.. code:: python

    # lazy evaluation -- query() returns self instead of a new dataframe
    # calls to .query() build up a filter object which is only evaluated
    # on repr() or when accesing the .value property
    df = QDataFrame(iris).lazy()
    df.query(~Q(Name__contains='versicolor') & ~Q(Name__contains='setosa'))
    df.query(SepalLength=5.8)
    df.value

