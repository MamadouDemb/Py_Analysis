from BuildDataFrame import Download_AppData
from Manage_AppData import CrossApp_Data
import pandas as pd
import xlrd
import numpy as np
import xlrd
import xlsxwriter
from datetime import datetime

from pathL import path_SIGOS, path_AD, path_O365, path_SAPUSMM


def main():

    teste =CrossApp_Data(Download_AppData(0,'Cusr',path_SIGOS),\
        Download_AppData(0,'samaccountname',path_AD), \
        Download_AppData(0,'ID', path_O365), \
        #Download_AppData(0,'Cusr_s',path_RH),\
        Download_AppData(0,'User Name',path_SAPUSMM),\
        #Download_AppData(0,'User concerné',path_SAPBCT)
        #Download_AppData(5, path1),\
        #Download_AppData(0, path_REP)



    )
    #teste.toLower()
    teste.toLower_Merge()
    print(teste)
    #print(teste.SI_USER)




if __name__ =="__main__":
    main()
