
from main import DBConnection, DBConfiguration


def test_development_connection(development_environment):

    connect = DBConnection(development_environment)

    assert connect == True

def test_production_connection(production_environment):

    connect = DBConnection(production_environment)

    assert connect == True

def test_test_connection(testing_environment):

    connect = DBConnection(testing_environment)

    assert connect == True