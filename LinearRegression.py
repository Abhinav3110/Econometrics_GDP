# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:50:32 2019

@author: Abhinav Santoshi
"""

import statsmodels.api as sm
import Settings as st
import pandas as pd
import Utilities as ut
import datetime as dt
from io import StringIO
#from sklearn.linear_model import LinearRegression


def printSummary(dataStream):

    fileName = st.RESULT_SUMMARY_FILE
    fileMode = "a"
    ut.printFile(fileName, fileMode, dataStream)
    print(dataStream)


def runLinearRegressionOnData(fileName):

    dataSet = pd.read_excel(fileName, index_col = None)

    regressionList = st.REGRESSION_PARAMETERS

    for yKey in regressionList.keys():
        y = dataSet[yKey]
        XList = regressionList[yKey]
        X = dataSet[XList]
        X = sm.add_constant(X)
#        reg = LinearRegression().fit(X, y)
#        print(reg.coef_)

        mod = sm.OLS(y, X)
        res = mod.fit()
        resultSummmary = str(res.summary())

        resultTitle = st.RESULT_TITLE
        timeRecord = dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        dataStream = StringIO()
        dataStream.write("\n\n{0:#^90}\n".format(""))
        dataStream.write("Title: {0:<50} Time: {1:<50}".format(resultTitle, timeRecord))
        dataStream.write("\n{0:#^90}\n\n\n".format(""))
        dataStream.write(resultSummmary)
        dataStream.write("\n\n{0:#^90}\n".format(""))
        dataString = dataStream.getvalue()
        dataStream.close()
        printSummary(dataString)



def runLinearRegression():
    runLinearRegressionOnData( st.LINEAR_REGRESSION_INPUT_FILE_NAME )


if __name__== "__main__":
    runLinearRegression()