import unittest

from dfquery import Filter
from dfquery.qdf import QDataFrame
import pandas as pd


class FilterTests(unittest.TestCase):
    def test_none(self):
        """
        test filtering for null or None values
        """
        df = pd.DataFrame({
            'x' : [0,1,2,3,4,None]                 
        })
        subset = Filter(df, x__isnone=True).value
        self.assertEqual(len(subset.index), 1)
        subset = Filter(df, x__isnone=False).value
        self.assertEqual(len(subset.index), 5)
        
    def test_qdf_fromdf(self):
        """
        test filtering an existing dataframe by turning it into
        a QDataFrame
        """
        df = pd.DataFrame({
            'x' : xrange(0, 100)                 
        })
        qdf = QDataFrame(df)
        subset = qdf.query(x__gt=3) # 4, ..., 100 => 100 - 4 = 96 
        self.assertEqual(len(subset.index), 96)
        subset = qdf.query(x__gte=3) # 3, ..., 100 => 100 - 4 = 96 
        self.assertEqual(len(subset.index), 97)