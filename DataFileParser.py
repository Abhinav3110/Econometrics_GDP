# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:41:52 2019

@author: Abhinav Santoshi
"""

import pandas as pd
import EnumUtils as eu
import Country as cntry


class DataFileParser:

    def __init__(self, fileName, yearList, seriesList):
        self.myFileName = fileName
        self.myYearList = yearList
        self.mySeriesList = seriesList

    def getFileName(self):
        return self.myFileName

    def getYearList(self):
        return self.myYearList

    def getSeriesList(self):
        return self.mySeriesList

    def readFile(self, countryObjMap):
        fileDataFrame = pd.read_excel(self.myFileName)
        self.parseDataFrame(fileDataFrame, countryObjMap)

    def parseDataFrame(self, fileDataFrame, countryObjMap):

        for index, row in fileDataFrame.iterrows():
            countryCode = row[eu.COLUMN_COUNTRY_CODE]
            countryObj = countryObjMap.get(countryCode, -1)

            if countryObj != -1 :
                self.addSeriesData(countryObj, fileDataFrame, row)
            else:
                newCountryObj = cntry.Country(countryCode)
                countryName = row[eu.COLUMN_COUNTRY_NAME]
                newCountryObj.setCountryName(countryName)
                countryObjMap[countryCode] = newCountryObj
                self.addSeriesData(newCountryObj, fileDataFrame, row)


    def addSeriesData( self, countryObj, fileDataFrame, row):

            seriesName = row[eu.COLUMN_SERIES_NAME]

            if not seriesName in self.mySeriesList:
                    self.mySeriesList.append(seriesName)

            yearStartIndex = eu.ColumnNames.YEARS
            for yearColumn in fileDataFrame.columns[yearStartIndex:]:

                if not yearColumn in self.myYearList:
                    self.myYearList.append(yearColumn)

                dataValue = row[yearColumn]
                countryObj.addDataOfSeries(seriesName, yearColumn, dataValue)




