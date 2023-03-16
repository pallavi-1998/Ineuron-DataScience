import Sql_Operation as sql_op

obj_main = sql_op.sql_operation()
#eshtablish connection
obj_main.connect()

# database list
db_lst = obj_main.get_database_list()
print(db_lst)

# table list
tbl_lst = obj_main.get_table_list("test")
print(tbl_lst)

# column list
col_lst = obj_main.get_column_list("test", "test_table")
print(col_lst)

# create new database
create_db = obj_main.create_database("Carbon_Nanotubes")
print("create database : ",create_db)

# create new table
create_tbl = obj_main.create_table("Carbon_Nanotubes", "carbon_nano", " chiralIndice_m INT(5), chiralIndice_n INT(5), iniAtomicCoordinate_u VARCHAR(50), iniAtomicCoordinate_v VARCHAR(50), iniAtomicCoordinate_w VARCHAR(50), finalAtomicCoordinate_u VARCHAR(50), finalAtomicCoordinate_v VARCHAR(50), finalAtomicCoordinate_w VARCHAR(50)"  )
print("create table : ", create_tbl)

# show databases
db_lst = obj_main.get_database_list()
print(db_lst)

#show tables
tbl_lst = obj_main.get_table_list("Carbon_Nanotubes")
print(tbl_lst)

#show columns
col_lst = obj_main.get_column_list("Carbon_Nanotubes", "carbon_nano")
print(col_lst)

# inserting bulk data
insertion = obj_main.insert_data("Carbon_Nanotubes", "carbon_nano") 
print(insertion)

# print all data without conditions
get_data = obj_main.get_data("Carbon_Nanotubes", "carbon_nano")
print(get_data)

# print data based on condition
get_data_with_cond = obj_main.get_data_with_condition("Carbon_Nanotubes", "carbon_nano", "*", {'chiralIndice_m': 3, 'chiralIndice_n': 2})
print(get_data_with_cond)

#update data based on condition
update_data = obj_main.update_data("Carbon_Nanotubes", "carbon_nano", {'chiralIndice_m': 123, 'chiralIndice_n': 124}, {'chiralIndice_m': 2, 'chiralIndice_n': 1})
print(update_data)

# print data based on condition
get_data = obj_main.get_data_with_condition("Carbon_Nanotubes", "carbon_nano","*",{'chiralIndice_m': 123, 'chiralIndice_n': 124} )
print(get_data)

#deleting data
del_data = obj_main.delete_data("Carbon_Nanotubes", "carbon_nano", {'chiralIndice_m': 3, 'chiralIndice_n': 1})
print(del_data)

# print data based on condition
get_data = obj_main.get_data_with_condition("Carbon_Nanotubes", "carbon_nano","*",{'chiralIndice_m': 3, 'chiralIndice_n': 1} )
print(get_data)

# drop table
drop_tbl = obj_main.drop_table("Carbon_Nanotubes", "carbon_nano")
print(drop_tbl)

#show table list
tbl_lst = obj_main.get_table_list("Carbon_Nanotubes")
print(tbl_lst)

#drop database
drop_db = obj_main.drop_database("Carbon_Nanotubes")
print(drop_db)

#show database list
db_lst = obj_main.get_database_list()
print(db_lst)