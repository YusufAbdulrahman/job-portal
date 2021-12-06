import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'workers',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS emp(
  ID INT NOT NULL AUTO_INCREMENT,
  fname VARCHAR(200) NOT NULL,
  mname VARCHAR(200) NOT NULL,
  lname VARCHAR(200) NOT NULL,
  address VARCHAR(200)NOT NULL,
  state VARCHAR(100) NOT NULL,   
  phone INT NOT NULL,
  emeil VARCHAR(300) NOT NULL,
 age INT NOT NULL,
 y_work VARCHAR(700) NOT NULL,
 PRIMARY KEY(ID)
 )
 """
) 


