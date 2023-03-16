
import mysql.connector
from logger import log
import csv
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')

# x = log(os.path.basename(__name__))
x = log("sql_logfile")
lg = x.get_logger()


class sql_operation():
    """class for mySql operation"""
    def __init__(self):
        try:
            
            self._host = config.get('mysql', 'host')
            self._user = config.get('mysql', 'user')
            self._password = config.get('mysql', 'password')
            self.database = None
            self.conn = None
            self.cursor = None
        except Exception as e:
            lg.error('error in init %s', e)
            raise e
        

    def connect(self):
        """connect to database"""
        try:
            self.conn = mysql.connector.connect(host=self._host,
                                                user=self._user,
                                                password=self._password,
                                                use_pure=True)
        except Exception as e:
            lg.error("Connection Failed %s",e)
            return False
        lg.info("Connection Successful")
        return True
    
    def get_cur(self):
        """get cursor"""
        if self.conn is None:
            lg.error("Connection is None")
            return False
        self.cursor = self.conn.cursor()
        lg.info("Cursor is created")
        return True
    
    def get_database_list(self):
        """get database list"""
        try:
            self.get_cur()
            self.cursor.execute("SHOW DATABASES")
            lg.info("database list is fetched")
            # db_lst = self.cursor.fetchall()
            # lg.info("list of database: {}".format(db_lst))    
            return self.cursor.fetchall()
            # return db_lst
        except Exception as e:
            lg.error("error in get_database_list %s",e)
            return False
    
    def get_table_list(self, database):
        """get table list"""
        try:
            self.get_cur()
            self.cursor.execute("SHOW TABLES FROM {}".format(database))
            lg.info("table list is fetched")
            # tbl_lst = self.cursor.fetchall()                    
            # lg.info("list of tables in {} : {}".format(database, tbl_lst))   
            return self.cursor.fetchall()
            # return tbl_lst
        except Exception as e:
            lg.error("error in get_table_list %s",e)
            return False
    
    def get_column_list(self, database, table):
        """get column list"""
        try:
            self.get_cur()
            self.cursor.execute("SHOW COLUMNS FROM {}.{}".format(database, table))
            lg.info("column list is fetched, %s %s", database, table)
            # col_lst = self.cursor.fetchall()
            # lg.info("list of columns in {}: {}".format(table,col_lst))    
            return self.cursor.fetchall()
            # return col_lst
        except Exception as e:
            lg.error("error in get_column_list %s",e)
            return False
    
    def get_data_with_condition(self, database, table, column, filter_condition):
        """get data"""
        try:
            self.get_cur()
            condition = " and ".join([key+"='"+str(filter_condition[key])+"'" for key in filter_condition.keys()])
            self.cursor.execute("SELECT {} FROM {}.{} WHERE {}".format(column, database, table, condition))
            result = self.cursor.fetchall()
            lg.info("%d data is fetched (based on condition) %s %s %s %s", len(result),database, table, column, condition)
            return result
        except Exception as e:
            lg.error("error in get_data %s",e)
            return False
         
    def get_data(self, database, table, limit = 30):
        """get data with out condition"""
        try:
            self.get_cur()
            self.cursor.execute("SELECT * FROM {}.{} LIMIT {}".format( database, table, limit))
            lg.info("data fetched (all data) %s %s ", str(database), table)
            return self.cursor.fetchall()
        except Exception as e:
            lg.error("error in get_data %s",e)
            return False

    def create_database(self, database):
        """create database"""
        try:
            self.get_cur()
            self.cursor.execute("CREATE DATABASE {}".format(database))
            self.conn.commit()
            lg.info("database is created %s", database)
            return True
        except Exception as e:
            lg.error("error in create_database %s",e)
            return False
    
    def create_table(self, database, table, column_list):
        """create table"""
        try:
            self.get_cur()
            self.cursor.execute("CREATE TABLE {}.{} ({})".format(database, table, column_list))
            self.conn.commit()
            lg.info("table is created %s %s %s", database, table, column_list)
            return True
        except Exception as e:
            lg.error("error in create_table %s",e)
            return False

    def read_file(self,file_loc):
        with open(file_loc, 'r') as file:
            lg.info("File opened and read into progress ...")
            file_read = csv.reader(file, delimiter='\n')
            next(file_read)
            row_data = [tuple(i[0].split(";")) for i in file_read]
        return row_data

    def insert_data(self, database, table):
        """insert data"""
        try:
            self.get_cur()
            # file_loc = "../dataset/carbon_nanotubes.csv" 
            row_data = self.read_file("../dataset/carbon_nanotubes.csv")         
            lg.info("data is inserting %s %s ", database, table)
            query = "INSERT INTO {}.{} VALUES ({value_list})".format(database, table, value_list = '%s,%s,%s,%s,%s,%s,%s,%s')
            self.cursor.executemany(query, row_data)
            self.conn.commit()
            lg.info("%d data inserted successfully %s %s ", len(row_data),database, table)
        
            return True
        except Exception as e:
            lg.error("error in insert_data %s",e)
            return False
        
    def update_data(self, database, table, set_value, update_condition):
        """update data"""
        try:
            self.get_cur()
            set = ",".join([key+"='"+str(set_value[key])+"'" for key in set_value.keys() ])
            condition = " and ".join([key+"='"+str(update_condition[key])+"'" for key in update_condition.keys()])
            self.cursor.execute("UPDATE {}.{} SET {} WHERE {}".format(database, table, set, condition))
            self.conn.commit()
            lg.info("data is updated %s %s %s %s", database, table, set, condition)
            return True
        except Exception as e:
            lg.error("error in update_data %s",e)
            return False
        
    def delete_data(self, database, table, del_condition):
        """delete data"""
        try:
            self.get_cur()
            condition = " and ".join([key+"='"+str(del_condition[key])+"'" for key in del_condition.keys()])
            self.cursor.execute("DELETE FROM {}.{} WHERE {}".format(database, table, condition))
            self.conn.commit()
            lg.info("data is deleted %s %s %s", database, table, condition)
            return True
        except Exception as e:
            lg.error("error in delete_data %s",e)
            return False
        
        
    def drop_table(self, database, table):
        """drop table"""
        try:
            self.get_cur()
            self.cursor.execute("DROP TABLE if exists {}.{}".format(database, table))
            self.conn.commit()
            lg.info("table is dropped %s %s", database, table)
            return True
        except Exception as e:
            lg.error("error in drop_table %s",e)
            return False
        
    def drop_database(self, database):
        """drop database"""
        try:
            self.get_cur()
            self.cursor.execute("DROP DATABASE if exists {}".format(database))
            self.conn.commit()
            lg.info("database is dropped %s", database)
            return True
        except Exception as e:
            lg.error("error in drop_database %s",e)
            return False
    
    
    
    
    
    
    
    
    
    
            

    