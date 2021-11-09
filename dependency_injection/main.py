from testing import *


class DBConfiguration():
    def __init__(self, database, user, pwd, host, port):
        self.database = database
        self.user = user
        self.pwd = pwd
        self.host = host
        self.port = port
    


class DBConnection():
    def __init__(self, configuration: DBConfiguration):
        self.configuration = configuration

    def __str__(self):
        config = self.configuration

        return f"Connection to {config.database} DB on port {config.port} succesful"
    


if __name__ == '__main__':
    development_environment = DBConfiguration('mongodb', 'root', '1234567', 'localhost', 5555)
    production_environment = DBConfiguration('mongodb', 'admin', '1234567', '157.253.0.1', 3656)
    testing_environment = DBConfiguration('mongodb', 'test', '1234567', '157.253.0.1', 56555)

    connection1 = DBConnection(development_environment)
    connection2 = DBConnection(production_environment)
    connection3 = DBConnection(testing_environment)

    connections = [connection1, connection2, connection3]
    for i in connections:
        print(i)
