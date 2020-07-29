Dependencies:
1. You need to install Python 3 and MySQL.


2. The tkinter, pymysql, numpy and pandas libraries of python needs to be installed. This can be done by running following commands from command line:


pip install tkinter (or) pip3 install tkinter
pip install pymysql (or) pip3 install pymysql  
pip install numpy (or) pip3 install numpy
pip install pandas (or) pip3 install pandas


Set-up:
1. Then you should run pre_processing.py file to process the CSV files in mysql.


2. Then run the CONTACT_TABLE.sql file from mysql prompt using the “source” command:   source CONTACT_TABLE.sql
   After thet import the above csv files into mysql.

3. After successfully completing the above steps, change the parameters “host”, “user” , “password” of the pymysql.connect() method to your values in each .py file except pre_processing.py file.


4. Now your application is ready to launch, just run the main.py file from the terminal.