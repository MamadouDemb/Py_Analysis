import pandas as pd
import xlrd
import numpy as np
import xlrd
import xlsxwriter


def Download_AppData(ref_sht, colonne1,path):
    excel_file=pd.ExcelFile(path)
    al= excel_file.sheet_names
    DataTable =excel_file.parse(al[ref_sht])
    DataTable2=pd.DataFrame({colonne1: DataTable[colonne1]})
    return DataTable2

def MergeMYData(DF_ref,DF,DF_col, NewCol):
    DFmerged= pd.merge(DF_ref,DF,how='left',
                           left_on='Cusr', right_on=DF_col)

    DFmerged[NewCol]= DFmerged[DF_col].isnull()

    return DFmerged

def MergeDF(SIGOS, AD_USER, O_365,SAPUSMM_USER):   #RH_USER, S,SAP_BCT):
        FinalDF = MergeMYData(SIGOS, AD_USER, 'samaccountname','Absent dans AD')
        FinalDF=MergeMYData(FinalDF, O_365, 'ID','Absent dans Office_365')
        #FinalDF = MergeMYData(FinalDF, RH_USER, 'Cusr_s','Absent dans RH')
        FinalDF = MergeMYData(FinalDF, SAPUSMM_USER,'User Name','Absent dans SAPUSMM')
        #FinalDF = MergeMYData(FinalDF, SAP_BCT,'User concerné','Absent dans BCT')
        return FinalDF










