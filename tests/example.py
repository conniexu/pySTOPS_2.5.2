import os
import glob
import pystops
import pandas as pd

#report_file = os.path.join('..', 'data', 'STOPS', 'Reports', 'AC_DART#DART#DART_D2_Alt3-7a-A_STOPSY2045Results.prn')
report_file = os.path.join('..', 'data', 'STOPS', 'Reports', 'AC_DART#DART#DART_D2t1_STOPSY2018Results.prn')
# table number section 15, and section 16, please use "Section 15" and "Section 16"
# SECTION 16 runs about 25 mins, SECTION 15 runs about 

for i in range(1,17):
    isExist = os.path.exists(os.path.join('..', 'tests','SECTION '+ str(i), ""))
    if not isExist:
            os.makedirs(os.path.join('..', 'tests','SECTION '+ str(i), ""))

output16_path = os.path.join('..', 'tests','SECTION 16', "")
output15_path = os.path.join('..', 'tests','SECTION 15', "")

#'1.01','1.02','4.01','4.02','4.03','4.04','8.01','9.01','10.03','10.04','10.05','11.01','11.02','11.03'
#'11.01','11.02','11.03','SECTION 15','SECTION 16'



for table in ['1.01','1.02','4.01','4.02','4.03','4.04','8.01','9.01','10.03','10.04','10.05','11.01','11.02','11.03']:
    if table == "SECTION 16":
        print('Parse Table Series in : {}'.format(table))       
        table_no = table
        table = pystops.parse_table(report_file, table, output16_path)
        
        os.chdir(output16_path)        
        extension = 'csv'
        all_filenames = None
        all_filenames = [j for j in glob.glob('*.{}'.format(extension))]
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
        combined_csv.to_csv(table_no + "_combined.csv", index=False, encoding='utf-8-sig')
    
    elif table == "SECTION 15":
        print('Parse Table Series in : {}'.format(table))
        table_no = table
        table = pystops.parse_table(report_file, table, output15_path)
        
        os.chdir(output15_path)        
        extension = 'csv'
        all_filenames = None
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
        combined_csv.to_csv(table_no + "_combined.csv", index=False, encoding='utf-8-sig')    
        
    else:
        print('Parse Table: {}'.format(table))
        table_no = table
        table = pystops.parse_table(report_file, table, os.path.join('..', 'tests','SECTION '+table_no[:len(table_no)-3], ""))

#        os.chdir(os.path.join('..', 'tests','SECTION '+table_no[:len(table_no)-3], ""))
#        table.to_csv(r'Table_{}.csv'.format(table_no),index=False)
        table.to_csv(os.path.join('..', 'tests','SECTION '+table_no[:len(table_no)-3], "", r'Table_{}.csv').format(table_no),index=False)
    

