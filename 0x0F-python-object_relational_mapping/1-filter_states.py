#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    """ MAIN FUNCTION"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
