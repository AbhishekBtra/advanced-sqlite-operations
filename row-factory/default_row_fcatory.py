"""By default, sqlite3 represents each row as a tuple. If a tuple does not suit your needs, you can use the sqlite3.
Row class or a custom row_factory."""
import sqlite3

con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row

res = con.execute("SELECT 'Earth' AS name, 6378 AS radius")
row = res.fetchone()
_keys=row.keys()

print(_keys)

#Row provides indexed and case-insensitive named access to columns,
#with minimal memory overhead and performance impact over a tuple

print(row[1])#6378
print(row["name"])#Earth
print(row["NAME"])#Earth


#default row factory is tuplecon = sqlite3.connect(":memory:")
con.row_factory = None
print(con.cursor().description)
for row in con.execute("SELECT 1 AS a, 2 AS b"):
    print(row)

con.close()