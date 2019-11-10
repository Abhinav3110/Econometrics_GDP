# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:58:41 2019

@author: Abhinav Santoshi
"""

import Settings as st
import Utilities as ut
import pandas as pd
import numpy as np


def dumpWithArithmeticGrowth(fileName):

    rawDataSet = pd.read_excel(fileName, index_col = None)
    groupByList = st.GROUP_BY_LIST
    yearCount = st.GROWTH_YEAR_PERIOD
    arithmeticGrowthList = st.ARITHMETIC_GROWTH
    rawDataSet[arithmeticGrowthList] = rawDataSet.groupby(groupByList)[arithmeticGrowthList].pct_change()
    rawDataSet[arithmeticGrowthList] = rawDataSet[arithmeticGrowthList].div(yearCount)

    numericColumnIndex = rawDataSet.select_dtypes(include=[np.number])
    rawDataSet.loc[:, numericColumnIndex.columns] = np.round(numericColumnIndex, st.DECIMAL_ROUND)

    outputFileName = st.ARITHMETIC_GROWTH_OUTPUT_FILE_NAME
    ut.writeToExcel(outputFileName, rawDataSet)


def dumpArithmeticGrowth():
    dumpWithArithmeticGrowth( st.ARITHMETIC_GROWTH_INPUT_FILE_NAME )


if __name__== "__main__":
    dumpArithmeticGrowth()



