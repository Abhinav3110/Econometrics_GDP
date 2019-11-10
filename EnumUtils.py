# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:09:33 2019

@author: Abhinav Santoshi
"""

from enum import IntEnum

class ColumnNames(IntEnum):
        SERIES_NAME = 2
        SERIES_CODE = 3
        COUNTRY_NAME = 0
        COUNTRY_CODE = 1
        YEARS = 4



COLUMN_COUNTRY_NAME = "Country Name"
COLUMN_COUNTRY_CODE = "Country Code"
COLUMN_SERIES_NAME = "Series Name"
COLUMN_SERIES_CODE = "Series Code"
COLUMN_YEAR = "Year"
COLUMN_COUNTRY_COEFFICIENT = "Country_Coefficient"
COLUMN_TIME_COEFFICIENT = "Time_Coefficient"

