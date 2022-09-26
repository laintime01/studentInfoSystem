import pymysql
# open connect
conn = pymysql.connect(host='localhost', user="root", password="")
cursor = conn.cursor()
# create database
cursor.execute('CREATE DATABASE IF NOT EXISTS sis_db DEFAULT CHARSET utf8 COLLATE utf8_general_ci')
cursor.close()
print('sis db created')