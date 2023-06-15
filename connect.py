import mysql.connector as sql

con = sql.connect(host="localhost", user="root",
                  password="harsh0312", database="AKSH")
global cur
cur = con.cursor()


def check_database():
    a = "show tables;"
    cur.execute(a)
    result = cur.fetchall()
    l = ["info"]
    try:
        if l != result:
            q1 = "create table info (NAME varchar(50) NOT NULL,EMAIL_ADDRESS varchar(100) NOT NULL,GENDER varchar(7) NOT NULL,DOB date NOT NULL,PASSWORD varchar(10) NOT NULL , primary key (EMAIL_ADDRESS));"
            cur.execute(q1)

    except:
        pass
    finally:
        con.close()
