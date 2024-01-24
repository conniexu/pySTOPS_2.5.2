# pySTOPS
## Summary
- This is a python based parsing tool to get tables from STOPS report to csv, and import them as datasource scheduled on refreshment on daily bases in STOPS Tableau for DART Capital Planning team.
- The tool is used on outputs from STOPS version 2.5.3, there is slight difference in prior version STOPS's output due to 2.5.2 has additional section 17 added at the end of the section 16, resulting changes in table lookup for section 16. As a results, if prior STOPS is used, please contact Phil Johnson at Pjohnso2@dart.org or Connie Xu at cxu@dart.org and request prior reader.py for STOPS 2.5.0 or prior.
- This tool requires Python install, the version on development is 3.9.0, with pandas and numpy as package requirements. 
- Tables that get processed in this tool are listed below, selection of those tableas is tailed to the needs of the developed Tableau dashboard, if any table needs to be added, please change reader.py with its table specs, table specs can be referenced to the existing table reading specs layout in reader.py, for table referencing tables, please referencing to section 15 and section 16 's table specs. 
Tables list
'1.01','1.02','4.01','4.02','4.03','4.04','8.01','9.01','10.03','10.04','10.05','11.01','11.02','11.03','SECTION 15','SECTION 16'
- output of this tool is stored at the environment folder "tests" with sub-section folders, this setup is for users to copy the entire content in tests folder to a Tableau targetted datasource location, for more about how to setup the Tableau template, please contact Phil Johnson at Pjohnso2@dart.org or Connie Xu at cxu@dart.org.

## Installation
- please download python 3.9 or up from https://www.python.org/downloads/release/python-390/ and install to local computer
- Go to Windows menu and open cmd window
- navigate to the installed python progame path, if installed for all users, the path usually is located at c:\program files\python39, change path by typing "cd e:\env", if cmd error on change to different drive occurs, give a try on "cd /d e:\env" 
- create a virtual environment by giving the command "python -m venv e:\env\pystops" for example, once the virtual environment is created, please browse to the location and make sure pyvenv.cfg was created
- navigate in cmd to newly created vitural environment folder by typing "cd e:\env\pystops\scripts" and activate the environment by command "activate". Once the vitural environment is activated, the cmd promote appearing "(pystops) e:\env\pystops\Scripts>"
- update pip by typing "python -m pip install --upgrade pip" to make sure pip is up to date, and install site packages pandas and numpy by typing "pip install pandas ==2.1" and "pip install numpy==1.25.1", pandas 1.5 and up or any numpy version is good as well. Or install through requirements.txt by going to e:\env\pystops\ and type "pip install -r requirements.txt". 

## Steps to Generate cvss
- copy STOPS rpn output file to environment's .data/STOPS/Reports folder
- open example.py in tests folder and change line 6 report name located in the last comma section
- change content in square brackets in line 24 in example.py file for specific table outputs, line 19/20 provide some examples, for line 24, for table in ['1.01','10.03']
- save example.py file and go back to cmd and run it by typing in the activated environment "python e:\env\pystops\tests\example.py"
- running time depending on which tables it is parsing, Section 15 and Section 16 each takes about 20 mins, and the rest takes less than few seconds each.

 

Tables list
#'1.01','1.02','4.01','4.02','4.03','4.04','8.01','9.01','10.03','10.04','10.05','11.01','11.02','11.03','SECTION 15','SECTION 16'

#'11.01','11.02','11.03','SECTION 15','SECTION 16'


