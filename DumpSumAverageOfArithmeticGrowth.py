# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:25:52 2019

@author: Abhinav Santoshi
"""

import Settings as st
import Utilities as ut
import pandas as pd
import numpy as np


def dumpSumAverageGrowth(fileName):

    rawDataSet = pd.read_excel(fileName, index_col = None)
    groupByList = st.GROUP_BY_LIST
    arithmeticGrowthList = st.ARITHMETIC_GROWTH
    rawDataSet[arithmeticGrowthList] = rawDataSet.groupby(groupByList)[arithmeticGrowthList].pct_change()
    rawDataSet = rawDataSet.groupby(groupByList)[arithmeticGrowthList].mean()
#    print(rawDataSet)
#    growthDataSet = growthDataSet.groupby(groupByList)[arithmeticGrowthList].mean()

    numericColumnIndex = rawDataSet.select_dtypes(include=[np.number])
    rawDataSet.loc[:, numericColumnIndex.columns] = np.round(numericColumnIndex, st.DECIMAL_ROUND)

    outputFileName = st.ARITHMETIC_GROWTH_OUTPUT_FILE_NAME
    ut.writeToExcel(outputFileName, rawDataSet)


def dumpSumAverageOfArithmeticGrowth():
    dumpSumAverageGrowth( st.ARITHMETIC_GROWTH_INPUT_FILE_NAME )


if __name__== "__main__":
    dumpSumAverageOfArithmeticGrowth()