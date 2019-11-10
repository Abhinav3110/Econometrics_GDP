# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:59:02 2019

@author: Abhinav Santoshi
"""

class SeriesData:

    def __init__(self, countryCode, seriesName):
        self.mySeriesName= seriesName
        self.myCountryCode = countryCode
        self.myYearDataMap = {}

    def getSeriesName(self):
        return self.mySeriesName

    def getCountryCode(self):
        return self.myCountryCode

    def getYearDataMap(self):
        return self.myYearDataMap

    def addYearDataInfo(self, year, data):
        self.myYearDataMap[year] = data

    def getDataOfYear(self, year):
        return self.myYearDataMap.get(year, -1)






