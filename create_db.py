import pymysql
# open connect
conn = pymysql.connect(host='localhost', user="root", password="")
cursor = conn.cursor()
# create database
cursor.execute('CREATE DATABASE IF NOT EXISTS sis_db DEFAULT CHARSET utf8 COLLATE utf8_general_ci')
print('sis db created')
cursor.execute('use sis_db')
cursor.execute('CREATE TABLE IF NOT EXISTS teacher(id int(5) auto_increment primary key, name varchar(255) not null,subject varchar(255) not null,phone varchar(255))')
print('table teacher created')


