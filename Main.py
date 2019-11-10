# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:34:53 2019

@author: Abhinav Santoshi
"""
import DataFileParser as dfp
import Utilities as ut
import Settings as st


def start(countryObjMap, yearList, seriesList):

    for key in st.PANEL_INPUT_FILES.keys():
        fileName = st.PANEL_INPUT_FILES[key]
        parserObj = dfp.DataFileParser(fileName, yearList, seriesList)
        parserObj.readFile(countryObjMap)

    ut.printPanelData(countryObjMap, yearList, seriesList)


if __name__== "__main__":

    countryObjMap = {}
    yearList = []
    seriesList = []
    start(countryObjMap, yearList, seriesList)


