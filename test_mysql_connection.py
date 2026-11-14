
import pymysql
from getpass import getpass

# Connect to the UrbanPulse MySQL database
connection = pymysql.connect(
    host="localhost",
    user="urbanpulse_user",
    password=getpass("Enter UrbanPulse database password: "),
    database="urbanpulse_db",
    port=3306
)

print("MySQL Connection Successful!")

# Display the connected database name
cursor = connection.cursor()
cursor.execute("SELECT DATABASE()")

result = cursor.fetchone()
print("Connected Database:", result[0])

# Close the database connection
cursor.close()
connection.close()

print("MySQL Connection Closed!")
