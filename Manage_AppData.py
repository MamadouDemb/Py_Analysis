import pandas as pd
import xlrd
import numpy as np
import xlrd
import xlsxwriter
from BuildDataFrame import Download_AppData, MergeMYData,MergeDF
#from Manage_App_Data.Main_AppData import pathf
from pathL import pathf


def CreateFile(DF1, path):
    writer = pd.ExcelWriter(
        path,
        engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    DF1.to_excel(writer, index=False)
    writer.save()
class CrossApp_Data:
    def __init__(self,SIGOS, AD,O_365, UMM): #BCT,RH,AD,UMM,BCT,BWP,REP,REP_FONCTIONS):
        self.SIGOS=SIGOS
        self.AD=AD
        self.O_365 = O_365
        #self.RH=RH
        self.UMM=UMM
        #self.BCT=BCT
        #self.BWP=BWP
        #self.REP=REP
        #self.REP_FONCTIONS=REP_FONCTIONS
    def toLower_Merge(self):
        SIGOS = self.SIGOS
        AD = self.AD
        O_365=self.O_365
        #RH=self.RH
        UMM = self.UMM
        #BCT = self.BCT
        #BWP = self.BWP
        #REP = self.REP
        #REP_FONCTIONS=self.REP_FONCTIONS
        SIGOS["Cusr"]=SIGOS["Cusr"].str.lower()
        AD["samaccountname"]=AD["samaccountname"].str.lower()
        O_365["ID"]=O_365["ID"].str.lower()
        #RH["Cusr_s"] = RH["Cusr_s"].str.lower()
        UMM["User Name"]=UMM["User Name"].str.lower()
        #BCT["User concerné"]=BCT["User concerné"].str.lower()
        #BWP["User Name"] = BWP["User Name"].str.lower()
        #REP["User Name"]=REP["User Name"].str.lower()
        #REP_FONCTIONS["User"]= REP_FONCTIONS["User"].str.lower()
        MERGING=MergeDF(SIGOS,AD,O_365,UMM)    #BCT)


        CreateFile(MERGING, pathf)





