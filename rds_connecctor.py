from Utilities.rds import RDSDatabase

# credentials to access the RDS instance
rds_host = 'rds-python-1.c2b17fotakue.ap-south-1.rds.amazonaws.com'
rds_username = 'admin'
rds_password = 'hemanth123'
rds_port = 3306

rds = RDSDatabase(rds_host, rds_username, rds_password)
con_obj = rds.connect_database('Hemanth')
x = rds.run_query(con_obj, 'show tables')
print(list(x))
x = rds.run_query(con_obj, 'select distinct pollutants from pollution')
print(list(x))
