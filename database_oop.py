import sqlite3    
from database_config import DB_NAME,CREATE_MOVIES_TABLE,INSERT_MOVIES,GET_MOVIES

def sql_executor(script):    # sql_executor function
    conn=sqlite3.connect(DB_NAME)   # DB Connect aagudhu
    cursor=conn.cursor()   #SQL Command run panna cursor create panrom
    cursor.execute(script)  # Namma kudutha SQL query ah run Panrom
    conn.commit()           # Changes a DB la Save Panrom.Must for Insert ,Create
    conn.close()            # Connection Closed
#setup database and create table
sql_executor(CREATE_MOVIES_TABLE)   # Table iruntha vidu,illana New Table Create pannu
# insert sample data 
sql_executor(INSERT_MOVIES)   # Sample Vehicles ah DB la Podu

#fetch and print all movies
# No need to commit since we are only reading data
conn=sqlite3.connect(DB_NAME)   # Again DB Ku connect   
cursor=conn.cursor()             # Cursor Open
cursor.execute(GET_MOVIES)     # Select* From movies run Panrom
movies=cursor.fetchall()       # Ellam row ah eduthu 'movies' list la podurom
print("Movies in Database:")
print("ID|Movie|Time|Total|Booked|Remaining")
for movie in movies:          
    print(movies)               # One by One row Printed
    conn.close()    

# fetchall() =DB la irukura ellam dataum list of tuples ah tharum