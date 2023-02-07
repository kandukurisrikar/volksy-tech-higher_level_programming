#!/usr/bin/pythton3
'''connections'''


import sys
import MySQLdb
if __name__ == '__main__':

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], bd=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM 'states'")
    [print(state) for state in c.fetchall()]
