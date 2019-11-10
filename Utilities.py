# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:33:32 2019

@author: Abhinav Santoshi
"""

import pandas as pd
import Settings as st
import EnumUtils as eu
import numpy as np

def writeToExcel(filename, dataFrame):
    dataFrame.to_excel(filename, engine='xlsxwriter', index=False)


def printFile(fileName, fileMode, dataStream):
    file = open(fileName, fileMode)
    file.write(dataStream)
    file.close()

def printPanelData(countryObjMap, yearList, seriesList):

#    totalNumOfCountries = len (countryObjMap)
#    print(totalNumOfCountries)
#    print(yearList)

    countryArray = []
    countryCodeArray = []
    yearArray = []
    seriesDataArray = {}
    countryCoefficientArray = []
    timeCoefficientArray = []

    for series in seriesList:
        seriesDataArray[series] = []

    for countryKey in countryObjMap.keys():

        includeCountryList = st.PANEL_INCLUDE_COUNTRY
        if countryKey in includeCountryList:

            countryObj = countryObjMap.get(countryKey)
            countryName = countryObj.getCountryName()
            countryCode = countryObj.getCountryCode()
            seriesObjMap = countryObj.getSeriesObjMap()

            for year in yearList:

                if year in st.PANEL_INCLUDE_YEAR:

                    countryArray.append(countryName)
                    countryCodeArray.append(countryCode)
                    yearArray.append(year)

                    if countryCode in st.PANEL_COUNTRY_COEFFICIENT_1:
                        countryCoefficientArray.append(1)
                    else:
                        countryCoefficientArray.append(0)

                    if year in st.PANEL_TIME_COEFFICIENT_1:
                        timeCoefficientArray.append(1)
                    else:
                        timeCoefficientArray.append(0)

                    for seriesKey in seriesObjMap.keys():
                        seriesObj = seriesObjMap.get(seriesKey)
                        seriesName = seriesObj.getSeriesName()
                        seriesYearData = seriesObj.getDataOfYear(year)

                        seriesDataArray[seriesName].append(seriesYearData)



    collectedData = {
            eu.COLUMN_COUNTRY_NAME : countryArray,
            eu.COLUMN_COUNTRY_CODE : countryCodeArray,
            eu.COLUMN_YEAR : yearArray,
            eu.COLUMN_TIME_COEFFICIENT : timeCoefficientArray,
            eu.COLUMN_COUNTRY_COEFFICIENT : countryCoefficientArray
            }

    for seriesKey in seriesDataArray:
        headerName = seriesKey
        seriesData = seriesDataArray.get(seriesKey)
        collectedData[headerName] = seriesData

    dataFrame = pd.DataFrame(collectedData)
    numericColumnIndex = dataFrame.select_dtypes(include=[np.number])
    dataFrame.loc[:, numericColumnIndex.columns] = np.round(numericColumnIndex, st.DECIMAL_ROUND )
    fileName = st.PANEL_OUTPUT_FILE_NAME
    writeToExcel(fileName, dataFrame)



















