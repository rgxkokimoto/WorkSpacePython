import psycopg2

con = None
cur = None

try:
    con = psycopg2.connect("dbname=test user=postgres password=ADMIN")

    con = psycopg2.connect(dbname="test", user="postgres", password="ADMIN")
