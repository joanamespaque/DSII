import psycopg2
from psycopg2 import connect
class DAO:
    def __init__(self):
        self._con = 'dbname=trabalhoDS user=postgres password=postgres host=localhost port=5432'