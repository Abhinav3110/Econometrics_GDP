# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:57:22 2019

@author: Abhinav Santoshi
"""
import statsmodels.formula.api as smf
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


def runLinearMixedEffectsModelOnData(fileName):

    dataSet = pd.read_excel(fileName, index_col = None)

    formulaStr = st.LINEAR_MIXED_EFFECT_FORMULA
    groupList = st.LINEAR_MIXED_EFFECT_GROUPLIST

    model = smf.mixedlm( formulaStr, dataSet, re_formula=" ~Credit + Import + Export", groups=dataSet[groupList])
    modeldFit = model.fit()
    resultSummmary = str(modeldFit.summary())

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



def runLinearMixedEffectsModel():
    runLinearMixedEffectsModelOnData( st.LINEAR_MIXED_EFFECT_INPUT_FILE_NAME )


if __name__== "__main__":
    runLinearMixedEffectsModel()