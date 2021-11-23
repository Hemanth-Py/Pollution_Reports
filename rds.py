# Copyright (c) 2021 CodeOps Technologies LLP. All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#   - Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   - Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   - Neither the name of CodeOps or the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import pandas as pd
from sqlalchemy import create_engine


# this class connects to RDS database and performs creating, manu
class RDSDatabase:

    def __init__(self, host, username, password, port=3306):
        """
        this is a constructor of class which configures credentials the RDS MySql instance
        :param host: string representing host or endpoint provided in RDS instance
        :param username: string reprenting username of the RDS instance
        :param password: string reprenting the password of the RDS instance
        :param port: int or str representing the port of the database by default port is 3306 for MySql
        """
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def connect_database(self, db_name):
        """
        this method creates the connection with the database
        :param db_name: string representing the name of the database to which want to connect
        :return: object reference/address of the connection
        """
        engine = create_engine(f'mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{db_name}')
        connection = engine.connect()
        return connection

    @staticmethod
    def run_query(connection, query):
        """
        this static method run the sql queries
        :param connection: database connection object
        :param query: string representing the sql query
        :return: output reference/address of the sql query
        """
        query_result = connection.execute(query)
        return query_result

    @staticmethod
    def create_table_with_xl(connection, filename, table_name):
        """
        this static method creates the table with given connetion, filename, tablename
        the file should be an excel sheet and if the file with already exists it will be replaced
        :param connection: database connection object
        :param filename: its a string of file path or file name represents excel sheet
        :param table_name: string representing the table name
        """
        df = pd.read_excel(filename)
        df.to_sql(name=table_name, con=connection, if_exists='replace')


if __name__ == "__main__":
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
