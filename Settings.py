
PANEL_INPUT_FILES = {
"DATA" : r"D:\CCS_Econometrics\Popular Indicators.xlsx",
#"Population" : r"D:\CCS_Econometrics\Population_Data_Extract_From_World_Development_Indicators.xlsx",
#"GDP" : r"D:\CCS_Econometrics\GDP_Data_Extract_From_World_Development_Indicators.xlsx",
#"Electricity": r"D:\CCS_Econometrics\ELECTRICITY_Data_Extract_From_World_Development_Indicators.xlsx",
#"Export" : r"D:\CCS_Econometrics\EXPORT_Data_Extract_From_World_Development_Indicators.xlsx",
#"Import" :r"D:\CCS_Econometrics\IMPORT_Data_Extract_From_World_Development_Indicators.xlsx",
#"Credit" : "D:\CCS_Econometrics\CREDIT_Data_Extract_From_World_Development_Indicators.xlsx"
}

PANEL_OUTPUT_FILE_NAME = r"D:\CCS_Econometrics\Panel_Output.xlsx"

SELECTED_COLUMNS_INPUT_FILE = r"D:\CCS_Econometrics\Panel_Output_PaperData_Added_Variables_LogGrowth.xlsx"
SELECTED_COLUMNS_OUTPUT_FILE_NAME = r"D:\CCS_Econometrics\Panel_Output_PaperData_Added_Variables_LogGrowth_WIth_Interaction.xlsx"

ARITHMETIC_GROWTH_INPUT_FILE_NAME = r"D:\CCS_Econometrics\PanelData_Const_LCU_Added_Variables.xlsx"
ARITHMETIC_GROWTH_OUTPUT_FILE_NAME = r"D:\CCS_Econometrics\PanelData_Const_LCU_ArithGrowth_SUMAVG.xlsx"

LOGARITHMIC_GROWTH_INPUT_FILE_NAME = r"D:\CCS_Econometrics\Panel_Output_PaperData_Added_Variables.xlsx"
LOGARITHMIC_GROWTH_OUTPUT_FILE_NAME = r"D:\CCS_Econometrics\Panel_Output_PaperData_Added_Variables_LogGrowth.xlsx"

FILTER_INPUT_FILE_NAME = r"D:\CCS_Econometrics\Panel_Output_PaperData_2012_2016_LogGrowth.xlsx"
FILTER_OUTPUT_FILE_NAME = r"D:\CCS_Econometrics\Panel_Output_PaperData_LogGrowth_PERIOD_2012_2016.xlsx"

LINEAR_REGRESSION_INPUT_FILE_NAME = r"D:\CCS_Econometrics\Panel_Output_PaperData_Added_Variables_LogGrowth_WIth_Interaction.xlsx"

LINEAR_MIXED_EFFECT_INPUT_FILE_NAME = r"D:\CCS_Econometrics\Panel_Output_PaperData_Added_Variables_LogGrowth_WIth_Interaction.xlsx"


PANEL_INCLUDE_COUNTRY = ["ALB","DZA","AGO","ARG","ARM","AUS","AUT","AZE","BGD","BLR","BEL","BOL","BIH","BWA","BRA","BGR","CMR","CAN","CHL","CHN","COL","COG","CRI","CIV","HRV","CYP","CZE","DNK","DOM","ECU","SLV","FIN","FRA","GAB","DEU","GHA","GRC","GTM","HND","HKG","HUN","IND","IDN","ITA","JAM","JPN","KAZ","KEN","KOR","XKX","KGZ","LBN","MYS","MUS","MEX","MDA","MNG","MAR","MMR","NAM","NLD","NZL","NIC","NGA","MKD","NOR","PAK","PAN","PRY","PER","PHL","POL","PRT","ROU","SEN","SRB","SGP","SVK","SVN","ZAF","ESP","LKA","SWE","CHE","THA","TUR","UKR","GBR","USA","URY","VNM","ZMB", "KHM", "IRL", "TJK", "UKR"]


SPECIAL_COUNTRY = ["KHM", "IRL", "TJK", "UKR"]

PANEL_INCLUDE_YEAR = [ 2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016 ]

PANEL_TIME_COEFFICIENT_1 = [2012,2013,2014,2015,2016]

PANEL_COUNTRY_COEFFICIENT_1 = ["IND"]

DECIMAL_ROUND = 4

SELECTED_COLUMN_LIST = [

"Country Name",
"Country Code",
"Year",
"Time_Coefficient",
"Country_Coefficient",
"Import",
"Export",
"GDP",
"Electricty",
"Credit"


 ]


RAWDATA_ADD_ACTION_COLUMN_LIST = {

        }


RAWDATA_MULTIPLY_ACTION_COLUMN_LIST = {

        "Time_Import" : ("Time_Coefficient", "Import"),
        "Time_Export" : ("Time_Coefficient", "Export"),
        "Time_GDP" : ("Time_Coefficient", "GDP"),
        "Time_Electricty" : ("Time_Coefficient", "Electricty"),
        "Time_Credit" : ("Time_Coefficient", "Credit"),
        "Time_Country_Coefficient" : ("Time_Coefficient", "Country_Coefficient")

        }

RAWDATA_COLUMN_MULTIPLY_FACTOR = {

}


GROUP_BY_LIST = [ "Country Code" ]

LOGARITHMIC_GROWTH = [ "Electricty", "Credit", "Import", "Export", "GDP" ]

ARITHMETIC_GROWTH = ["Electricty", "Credit", "Import", "Export", "GDP" ]

REGRESSION_PARAMETERS = {

        "GDP" : [ "Time_Import", "Time_Export", "Time_Credit", "Time_Country_Coefficient", "Credit", "Import", "Export", "Country_Coefficient"]

        }

INCLUDE_FILTERS  = {

        "Year":[ 2016 ]

        }

GROWTH_YEAR_PERIOD = 1

RESULT_TITLE = "2002to2016_WITH_Electricty_Mixed"

RESULT_SUMMARY_FILE = r"D:\CCS_Econometrics\Regression_Summary.txt"

LINEAR_MIXED_EFFECT_FORMULA = "GDP ~ Electricty + Credit + Import + Export + Country_Coefficient"

LINEAR_MIXED_EFFECT_GROUPLIST =  "Country_Code"




