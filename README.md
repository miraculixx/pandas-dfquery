
pandas-dfquery
--------------

Provides keyword-style queries on Pandas DataFrames -- see examples
below.

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



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>SepalLength</th>
          <th>SepalWidth</th>
          <th>PetalLength</th>
          <th>PetalWidth</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>50</th>
          <td> 7.0</td>
          <td> 3.2</td>
          <td> 4.7</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>51</th>
          <td> 6.4</td>
          <td> 3.2</td>
          <td> 4.5</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>52</th>
          <td> 6.9</td>
          <td> 3.1</td>
          <td> 4.9</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>54</th>
          <td> 6.5</td>
          <td> 2.8</td>
          <td> 4.6</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>56</th>
          <td> 6.3</td>
          <td> 3.3</td>
          <td> 4.7</td>
          <td> 1.6</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>58</th>
          <td> 6.6</td>
          <td> 2.9</td>
          <td> 4.6</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>62</th>
          <td> 6.0</td>
          <td> 2.2</td>
          <td> 4.0</td>
          <td> 1.0</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>63</th>
          <td> 6.1</td>
          <td> 2.9</td>
          <td> 4.7</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>65</th>
          <td> 6.7</td>
          <td> 3.1</td>
          <td> 4.4</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>68</th>
          <td> 6.2</td>
          <td> 2.2</td>
          <td> 4.5</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>71</th>
          <td> 6.1</td>
          <td> 2.8</td>
          <td> 4.0</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>72</th>
          <td> 6.3</td>
          <td> 2.5</td>
          <td> 4.9</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>73</th>
          <td> 6.1</td>
          <td> 2.8</td>
          <td> 4.7</td>
          <td> 1.2</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>74</th>
          <td> 6.4</td>
          <td> 2.9</td>
          <td> 4.3</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>75</th>
          <td> 6.6</td>
          <td> 3.0</td>
          <td> 4.4</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>76</th>
          <td> 6.8</td>
          <td> 2.8</td>
          <td> 4.8</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>77</th>
          <td> 6.7</td>
          <td> 3.0</td>
          <td> 5.0</td>
          <td> 1.7</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>78</th>
          <td> 6.0</td>
          <td> 2.9</td>
          <td> 4.5</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>83</th>
          <td> 6.0</td>
          <td> 2.7</td>
          <td> 5.1</td>
          <td> 1.6</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>85</th>
          <td> 6.0</td>
          <td> 3.4</td>
          <td> 4.5</td>
          <td> 1.6</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>86</th>
          <td> 6.7</td>
          <td> 3.1</td>
          <td> 4.7</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>87</th>
          <td> 6.3</td>
          <td> 2.3</td>
          <td> 4.4</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>91</th>
          <td> 6.1</td>
          <td> 3.0</td>
          <td> 4.6</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>97</th>
          <td> 6.2</td>
          <td> 2.9</td>
          <td> 4.3</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # create Q objects as query terms, which are combinable by logical &, | 
    q_versi = Q(SepalLength__lt=6.0, Name__contains='versi')
    q_setosa = Q(SepalLength__lt=6.0, Name__contains='setosa')
    iris.query(q_versi & ~q_setosa)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>SepalLength</th>
          <th>SepalWidth</th>
          <th>PetalLength</th>
          <th>PetalWidth</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>53</th>
          <td> 5.5</td>
          <td> 2.3</td>
          <td> 4.0</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>55</th>
          <td> 5.7</td>
          <td> 2.8</td>
          <td> 4.5</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>57</th>
          <td> 4.9</td>
          <td> 2.4</td>
          <td> 3.3</td>
          <td> 1.0</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>59</th>
          <td> 5.2</td>
          <td> 2.7</td>
          <td> 3.9</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>60</th>
          <td> 5.0</td>
          <td> 2.0</td>
          <td> 3.5</td>
          <td> 1.0</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>61</th>
          <td> 5.9</td>
          <td> 3.0</td>
          <td> 4.2</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>64</th>
          <td> 5.6</td>
          <td> 2.9</td>
          <td> 3.6</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>66</th>
          <td> 5.6</td>
          <td> 3.0</td>
          <td> 4.5</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>67</th>
          <td> 5.8</td>
          <td> 2.7</td>
          <td> 4.1</td>
          <td> 1.0</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>69</th>
          <td> 5.6</td>
          <td> 2.5</td>
          <td> 3.9</td>
          <td> 1.1</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>70</th>
          <td> 5.9</td>
          <td> 3.2</td>
          <td> 4.8</td>
          <td> 1.8</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>79</th>
          <td> 5.7</td>
          <td> 2.6</td>
          <td> 3.5</td>
          <td> 1.0</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>80</th>
          <td> 5.5</td>
          <td> 2.4</td>
          <td> 3.8</td>
          <td> 1.1</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>81</th>
          <td> 5.5</td>
          <td> 2.4</td>
          <td> 3.7</td>
          <td> 1.0</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>82</th>
          <td> 5.8</td>
          <td> 2.7</td>
          <td> 3.9</td>
          <td> 1.2</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>84</th>
          <td> 5.4</td>
          <td> 3.0</td>
          <td> 4.5</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>88</th>
          <td> 5.6</td>
          <td> 3.0</td>
          <td> 4.1</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>89</th>
          <td> 5.5</td>
          <td> 2.5</td>
          <td> 4.0</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>90</th>
          <td> 5.5</td>
          <td> 2.6</td>
          <td> 4.4</td>
          <td> 1.2</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>92</th>
          <td> 5.8</td>
          <td> 2.6</td>
          <td> 4.0</td>
          <td> 1.2</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>93</th>
          <td> 5.0</td>
          <td> 2.3</td>
          <td> 3.3</td>
          <td> 1.0</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>94</th>
          <td> 5.6</td>
          <td> 2.7</td>
          <td> 4.2</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>95</th>
          <td> 5.7</td>
          <td> 3.0</td>
          <td> 4.2</td>
          <td> 1.2</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>96</th>
          <td> 5.7</td>
          <td> 2.9</td>
          <td> 4.2</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>98</th>
          <td> 5.1</td>
          <td> 2.5</td>
          <td> 3.0</td>
          <td> 1.1</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>99</th>
          <td> 5.7</td>
          <td> 2.8</td>
          <td> 4.1</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # create Q objects as query terms, which are combinable by logical &, | 
    q_versi = Q(SepalLength__gt=6.0, Name__contains='versi')
    q_setosa = Q(SepalLength__lt=6.0, Name__contains='setosa')
    iris.query(q_versi | q_setosa)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>SepalLength</th>
          <th>SepalWidth</th>
          <th>PetalLength</th>
          <th>PetalWidth</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0 </th>
          <td> 5.1</td>
          <td> 3.5</td>
          <td> 1.4</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>1 </th>
          <td> 4.9</td>
          <td> 3.0</td>
          <td> 1.4</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>2 </th>
          <td> 4.7</td>
          <td> 3.2</td>
          <td> 1.3</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>3 </th>
          <td> 4.6</td>
          <td> 3.1</td>
          <td> 1.5</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>4 </th>
          <td> 5.0</td>
          <td> 3.6</td>
          <td> 1.4</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>5 </th>
          <td> 5.4</td>
          <td> 3.9</td>
          <td> 1.7</td>
          <td> 0.4</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>6 </th>
          <td> 4.6</td>
          <td> 3.4</td>
          <td> 1.4</td>
          <td> 0.3</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>7 </th>
          <td> 5.0</td>
          <td> 3.4</td>
          <td> 1.5</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>8 </th>
          <td> 4.4</td>
          <td> 2.9</td>
          <td> 1.4</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>9 </th>
          <td> 4.9</td>
          <td> 3.1</td>
          <td> 1.5</td>
          <td> 0.1</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>10</th>
          <td> 5.4</td>
          <td> 3.7</td>
          <td> 1.5</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>11</th>
          <td> 4.8</td>
          <td> 3.4</td>
          <td> 1.6</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>12</th>
          <td> 4.8</td>
          <td> 3.0</td>
          <td> 1.4</td>
          <td> 0.1</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>13</th>
          <td> 4.3</td>
          <td> 3.0</td>
          <td> 1.1</td>
          <td> 0.1</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>14</th>
          <td> 5.8</td>
          <td> 4.0</td>
          <td> 1.2</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>15</th>
          <td> 5.7</td>
          <td> 4.4</td>
          <td> 1.5</td>
          <td> 0.4</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>16</th>
          <td> 5.4</td>
          <td> 3.9</td>
          <td> 1.3</td>
          <td> 0.4</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>17</th>
          <td> 5.1</td>
          <td> 3.5</td>
          <td> 1.4</td>
          <td> 0.3</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>18</th>
          <td> 5.7</td>
          <td> 3.8</td>
          <td> 1.7</td>
          <td> 0.3</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>19</th>
          <td> 5.1</td>
          <td> 3.8</td>
          <td> 1.5</td>
          <td> 0.3</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>20</th>
          <td> 5.4</td>
          <td> 3.4</td>
          <td> 1.7</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>21</th>
          <td> 5.1</td>
          <td> 3.7</td>
          <td> 1.5</td>
          <td> 0.4</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>22</th>
          <td> 4.6</td>
          <td> 3.6</td>
          <td> 1.0</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>23</th>
          <td> 5.1</td>
          <td> 3.3</td>
          <td> 1.7</td>
          <td> 0.5</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>24</th>
          <td> 4.8</td>
          <td> 3.4</td>
          <td> 1.9</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>25</th>
          <td> 5.0</td>
          <td> 3.0</td>
          <td> 1.6</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>26</th>
          <td> 5.0</td>
          <td> 3.4</td>
          <td> 1.6</td>
          <td> 0.4</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>27</th>
          <td> 5.2</td>
          <td> 3.5</td>
          <td> 1.5</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>28</th>
          <td> 5.2</td>
          <td> 3.4</td>
          <td> 1.4</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>29</th>
          <td> 4.7</td>
          <td> 3.2</td>
          <td> 1.6</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>40</th>
          <td> 5.0</td>
          <td> 3.5</td>
          <td> 1.3</td>
          <td> 0.3</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>41</th>
          <td> 4.5</td>
          <td> 2.3</td>
          <td> 1.3</td>
          <td> 0.3</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>42</th>
          <td> 4.4</td>
          <td> 3.2</td>
          <td> 1.3</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>43</th>
          <td> 5.0</td>
          <td> 3.5</td>
          <td> 1.6</td>
          <td> 0.6</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>44</th>
          <td> 5.1</td>
          <td> 3.8</td>
          <td> 1.9</td>
          <td> 0.4</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>45</th>
          <td> 4.8</td>
          <td> 3.0</td>
          <td> 1.4</td>
          <td> 0.3</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>46</th>
          <td> 5.1</td>
          <td> 3.8</td>
          <td> 1.6</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>47</th>
          <td> 4.6</td>
          <td> 3.2</td>
          <td> 1.4</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>48</th>
          <td> 5.3</td>
          <td> 3.7</td>
          <td> 1.5</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>49</th>
          <td> 5.0</td>
          <td> 3.3</td>
          <td> 1.4</td>
          <td> 0.2</td>
          <td>     Iris-setosa</td>
        </tr>
        <tr>
          <th>50</th>
          <td> 7.0</td>
          <td> 3.2</td>
          <td> 4.7</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>51</th>
          <td> 6.4</td>
          <td> 3.2</td>
          <td> 4.5</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>52</th>
          <td> 6.9</td>
          <td> 3.1</td>
          <td> 4.9</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>54</th>
          <td> 6.5</td>
          <td> 2.8</td>
          <td> 4.6</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>56</th>
          <td> 6.3</td>
          <td> 3.3</td>
          <td> 4.7</td>
          <td> 1.6</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>58</th>
          <td> 6.6</td>
          <td> 2.9</td>
          <td> 4.6</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>63</th>
          <td> 6.1</td>
          <td> 2.9</td>
          <td> 4.7</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>65</th>
          <td> 6.7</td>
          <td> 3.1</td>
          <td> 4.4</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>68</th>
          <td> 6.2</td>
          <td> 2.2</td>
          <td> 4.5</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>71</th>
          <td> 6.1</td>
          <td> 2.8</td>
          <td> 4.0</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>72</th>
          <td> 6.3</td>
          <td> 2.5</td>
          <td> 4.9</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>73</th>
          <td> 6.1</td>
          <td> 2.8</td>
          <td> 4.7</td>
          <td> 1.2</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>74</th>
          <td> 6.4</td>
          <td> 2.9</td>
          <td> 4.3</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>75</th>
          <td> 6.6</td>
          <td> 3.0</td>
          <td> 4.4</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>76</th>
          <td> 6.8</td>
          <td> 2.8</td>
          <td> 4.8</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>77</th>
          <td> 6.7</td>
          <td> 3.0</td>
          <td> 5.0</td>
          <td> 1.7</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>86</th>
          <td> 6.7</td>
          <td> 3.1</td>
          <td> 4.7</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>87</th>
          <td> 6.3</td>
          <td> 2.3</td>
          <td> 4.4</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>91</th>
          <td> 6.1</td>
          <td> 3.0</td>
          <td> 4.6</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>97</th>
          <td> 6.2</td>
          <td> 2.9</td>
          <td> 4.3</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
      </tbody>
    </table>
    <p>70 rows × 5 columns</p>
    </div>



.. code:: python

    # note you can apply query objects to other dataframes, too
    versi_l7 = df.query(~q_setosa & Q(SepalLength__gte=7.0))
    versi_l7



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>SepalLength</th>
          <th>SepalWidth</th>
          <th>PetalLength</th>
          <th>PetalWidth</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>50</th>
          <td> 7</td>
          <td> 3.2</td>
          <td> 4.7</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    df



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>SepalLength</th>
          <th>SepalWidth</th>
          <th>PetalLength</th>
          <th>PetalWidth</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>50</th>
          <td> 7.0</td>
          <td> 3.2</td>
          <td> 4.7</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>51</th>
          <td> 6.4</td>
          <td> 3.2</td>
          <td> 4.5</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>52</th>
          <td> 6.9</td>
          <td> 3.1</td>
          <td> 4.9</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>54</th>
          <td> 6.5</td>
          <td> 2.8</td>
          <td> 4.6</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>56</th>
          <td> 6.3</td>
          <td> 3.3</td>
          <td> 4.7</td>
          <td> 1.6</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>58</th>
          <td> 6.6</td>
          <td> 2.9</td>
          <td> 4.6</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>62</th>
          <td> 6.0</td>
          <td> 2.2</td>
          <td> 4.0</td>
          <td> 1.0</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>63</th>
          <td> 6.1</td>
          <td> 2.9</td>
          <td> 4.7</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>65</th>
          <td> 6.7</td>
          <td> 3.1</td>
          <td> 4.4</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>68</th>
          <td> 6.2</td>
          <td> 2.2</td>
          <td> 4.5</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>71</th>
          <td> 6.1</td>
          <td> 2.8</td>
          <td> 4.0</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>72</th>
          <td> 6.3</td>
          <td> 2.5</td>
          <td> 4.9</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>73</th>
          <td> 6.1</td>
          <td> 2.8</td>
          <td> 4.7</td>
          <td> 1.2</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>74</th>
          <td> 6.4</td>
          <td> 2.9</td>
          <td> 4.3</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>75</th>
          <td> 6.6</td>
          <td> 3.0</td>
          <td> 4.4</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>76</th>
          <td> 6.8</td>
          <td> 2.8</td>
          <td> 4.8</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>77</th>
          <td> 6.7</td>
          <td> 3.0</td>
          <td> 5.0</td>
          <td> 1.7</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>78</th>
          <td> 6.0</td>
          <td> 2.9</td>
          <td> 4.5</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>83</th>
          <td> 6.0</td>
          <td> 2.7</td>
          <td> 5.1</td>
          <td> 1.6</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>85</th>
          <td> 6.0</td>
          <td> 3.4</td>
          <td> 4.5</td>
          <td> 1.6</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>86</th>
          <td> 6.7</td>
          <td> 3.1</td>
          <td> 4.7</td>
          <td> 1.5</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>87</th>
          <td> 6.3</td>
          <td> 2.3</td>
          <td> 4.4</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>91</th>
          <td> 6.1</td>
          <td> 3.0</td>
          <td> 4.6</td>
          <td> 1.4</td>
          <td> Iris-versicolor</td>
        </tr>
        <tr>
          <th>97</th>
          <td> 6.2</td>
          <td> 2.9</td>
          <td> 4.3</td>
          <td> 1.3</td>
          <td> Iris-versicolor</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: python

    # lazy evaluation -- query() returns self instead of a new dataframe
    # calls to .query() build up a filter object which is only evaluated
    # on repr() or when accesing the .value property
    df = QDataFrame(iris).lazy()
    df.query(~Q(Name__contains='versicolor') & ~Q(Name__contains='setosa'))
    df.query(SepalLength=5.8)
    df.value



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>SepalLength</th>
          <th>SepalWidth</th>
          <th>PetalLength</th>
          <th>PetalWidth</th>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>101</th>
          <td> 5.8</td>
          <td> 2.7</td>
          <td> 5.1</td>
          <td> 1.9</td>
          <td> Iris-virginica</td>
        </tr>
        <tr>
          <th>114</th>
          <td> 5.8</td>
          <td> 2.8</td>
          <td> 5.1</td>
          <td> 2.4</td>
          <td> Iris-virginica</td>
        </tr>
        <tr>
          <th>142</th>
          <td> 5.8</td>
          <td> 2.7</td>
          <td> 5.1</td>
          <td> 1.9</td>
          <td> Iris-virginica</td>
        </tr>
      </tbody>
    </table>
    </div>


