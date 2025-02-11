import sqlite3

"""You can create a custom row_factory 
that returns each row as a dict, with column names mapped to values"""

def dict_factory(cursor, row):
    
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

con = sqlite3.connect(":memory:")
con.row_factory = dict_factory
for row in con.execute("SELECT 1 AS a, 2 AS b"):
    print(row)

con.close()