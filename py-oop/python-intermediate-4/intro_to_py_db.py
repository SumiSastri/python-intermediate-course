import pymysql


class PythonDb:
    ''' this class processes databases'''

    connection = None # connects to db
    cursor = None # run db command and store the data

    def __init__(self):
        try:
            PythonDb.connection = pymysql.connect('127.0.0.1', 'root', '', 'testdb', unix_socket = '' ) # server IP or name, username, password, dbname, socket (linux and mac)
            PythonDb.cursor = PythonDb.connection.cursor()
        except Exception as e:
            print(e.args)
        else:
            print('connection established successfully')

    def createTable(self, tableName):
        command ='''CREATE TABLE %s (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50))''' %(tableName)
        try:
            PythonDb.cursor.execute(command)
        except Exception as e:
            print (e.args)
            print(command)
        else:
            print('Table created successfully')
    def insertData(self, tableName, name):
        command = '''INSERT INTO %s (name) VALUES ('%s')''' %(tableName, name)
        try:
            PythonDb.cursor.execute(command)
        except Exception as e:
            print (e.args)
            print(command)
        else:
            PythonDb.connection.commit()
            print('Data added successfully')

    def listData(self, tableName):
        command = '''SELECT * FROM %s''' %(tableName)
        try:
            PythonDb.cursor.execute(command)
        except Exception as a:
            print(a.args)
            print(command)
        else:
            data = PythonDb.cursor.fetchall()
            for row in data:
                print(row)

    def deleteData(self,tableName, id):
         command1 = '''DELETE FROM %s WHERE ID = %d''' %(tableName,id)
         command2 = '''DELETE FROM %s WHERE id = x''' %(tableName)
         try:
            PythonDb.cursor.execute(command1)
            # PythonDb.cursor.execute(command2)
         except Exception as e:
            print(command1, command2)
            print(e.args)
            PythonDb.connection.rollback()
         else:
            PythonDb.connection.commit()
            print('record deleted successfully')

db = PythonDb()
# db.createTable('studentdata') # comment out or it will rerun with error that it is already created
# db.insertData('studentdata', input('Enter name').title())
db.listData('studentdata')
db.deleteData('studentdata', 1)
print()
db.listData('studentdata')