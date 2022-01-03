#import pymysql
# Open database connection
#db = pymysql.connect("5.196.109.133:3306","root","Cloud@place321#","enigma" )
#print(db)

import pymysql
import hashlib
connection = pymysql.connect(host='5.196.109.133',
                             user='root',
                             password='Cloud@place321#',
                             database='enigma',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# mycursor = connection.cursor()
# mycursor.execute("SELECT * FROM business_user1")
# account = mycursor.fetchone()
# account1 = account.get('role')
# print(account1)











	
	
  