# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:46:13 2019

@author: Abhinav Santoshi
"""

import Settings as st
import Utilities as ut
import pandas as pd
import numpy as np


def dumpOnlySelectedColumns(selectedColumnsFileName):

    rawDataSet = pd.read_excel(selectedColumnsFileName, index_col = None)
    collatedColumns = {}

    for columnKey in st.RAWDATA_COLUMN_MULTIPLY_FACTOR.keys():
        scalarFactor = st.RAWDATA_COLUMN_MULTIPLY_FACTOR.get(columnKey)
        rawDataSet[columnKey] = rawDataSet[columnKey].apply(lambda x: x*scalarFactor)

    for column in st.SELECTED_COLUMN_LIST:
        collatedColumns[column] = rawDataSet[column]

    multiplyColumnList =  st.RAWDATA_MULTIPLY_ACTION_COLUMN_LIST
    for multiplyKey in multiplyColumnList.keys():
        columnList = multiplyColumnList[multiplyKey]
        for columnNames in columnList:
            length = len(columnList)
            if length > 1:
                collatedColumns[multiplyKey] = rawDataSet[columnList[0]]
            for columnName in columnList[1:]:
                collatedColumns[multiplyKey] = collatedColumns[multiplyKey] * rawDataSet[columnName]


    dataFrame = pd.DataFrame(collatedColumns)
    numericColumnIndex = dataFrame.select_dtypes(include=[np.number])
    dataFrame.loc[:, numericColumnIndex.columns] = np.round(numericColumnIndex, st.DECIMAL_ROUND )
    outputFileName = st.SELECTED_COLUMNS_OUTPUT_FILE_NAME
    ut.writeToExcel(outputFileName, dataFrame)



def dumpSelectedColumns():
    dumpOnlySelectedColumns( st.SELECTED_COLUMNS_INPUT_FILE )

if __name__== "__main__":
    dumpSelectedColumns()



