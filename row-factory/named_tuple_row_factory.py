from collections import namedtuple
import sqlite3

"The following row factory returns a named tuple:"
def namedtuple_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    cls = namedtuple("DataRow", fields)
    return cls._make(row)

con = sqlite3.connect(":memory:")
con.row_factory = namedtuple_factory
cur = con.execute("SELECT 1 AS a, 2 AS b")
row = cur.fetchone()
print(row)

print(row[0])  # Indexed access.

print(row.b)   # Attribute access.

con.close()