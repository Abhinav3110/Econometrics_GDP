# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:19:00 2019

@author: Abhinav Santoshi
"""

import Settings as st
import Utilities as ut
import pandas as pd



def filterDataSetWithFilters(fileName):

    dataSet = pd.read_excel(fileName, index_col = None)

    filterList = st.INCLUDE_FILTERS

    for filterColumn in filterList.keys():
        filterItems = filterList[filterColumn]
        filterRule = dataSet[filterColumn].isin(filterItems)
        dataSet = dataSet[filterRule]

    outputFileName = st.FILTER_OUTPUT_FILE_NAME
    ut.writeToExcel(outputFileName, dataSet)



def applyDataSetFilter():
    filterDataSetWithFilters( st.FILTER_INPUT_FILE_NAME )


if __name__== "__main__":
    applyDataSetFilter()
