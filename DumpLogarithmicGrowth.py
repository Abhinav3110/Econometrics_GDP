# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 22:58:44 2019

@author: Abhinav Santoshi
"""

import Settings as st
import Utilities as ut
import pandas as pd
import numpy as np


def dumpWithLogarithmicGrowth(fileName):

    rawDataSet = pd.read_excel(fileName, index_col = None)
    yearCount = st.GROWTH_YEAR_PERIOD
    groupByList = st.GROUP_BY_LIST
    logarithmicGrowthList = st.LOGARITHMIC_GROWTH
    rawDataSet[logarithmicGrowthList] = rawDataSet.groupby(groupByList)[logarithmicGrowthList].apply(lambda x: np.log(x) - np.log(x.shift()))
    rawDataSet[logarithmicGrowthList] = rawDataSet[logarithmicGrowthList].div(yearCount)

    numericColumnIndex = rawDataSet.select_dtypes(include=[np.number])
    rawDataSet.loc[:, numericColumnIndex.columns] = np.round(numericColumnIndex, st.DECIMAL_ROUND)

    outputFileName = st.LOGARITHMIC_GROWTH_OUTPUT_FILE_NAME
    ut.writeToExcel(outputFileName, rawDataSet)


def dumpLogarithmicGrowth():
    dumpWithLogarithmicGrowth( st.LOGARITHMIC_GROWTH_INPUT_FILE_NAME )


if __name__== "__main__":
    dumpLogarithmicGrowth()



