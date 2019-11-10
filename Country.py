# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:02:14 2019

@author: Abhinav Santoshi
"""
import SeriesData as sd

class Country:

    def __init__(self, countryCode):
        self.myCountryName = ""
        self.myCountryCode = countryCode
        self.mySeriesObjMap = {}

    def setCountryName(self, countryName):
        self.myCountryName = countryName

    def getCountryName(self):
        return self.myCountryName

    def getCountryCode(self):
        return self.myCountryCode

    def getSeriesObjMap(self):
        return self.mySeriesObjMap

    def addDataOfSeries(self, seriesName, year, data):

        seriesDataObj = self.mySeriesObjMap.get(seriesName, -1)
        if (seriesDataObj != -1):
            seriesDataObj.addYearDataInfo( year, data)
        else:
            seriesyNewDataObj = sd.SeriesData(self.myCountryCode, seriesName)
            self.mySeriesObjMap[seriesName] = seriesyNewDataObj
            seriesyNewDataObj.addYearDataInfo( year, data)





