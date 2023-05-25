import configparser
import pymssql
import psycopg2
from psycopg2 import Error

cnf = configparser.ConfigParser()
cnf.read("cnf.ini")

connection = pymssql.connect(user=cnf['mssqlDB']['user'],
                             password=cnf['mssqlDB']['pass'],
                             server=cnf['mssqlDB']['server'],
                             database=cnf['mssqlDB']['db'])
