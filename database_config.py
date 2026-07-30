# Setting + SQL Queries File
# Blueprint of Database File
import os            # Easy to Handle File Path
DB_NAME=os.path.join(os.path.dirname(__file__),"movies.db") # Safe Folder la Create aaganum(Safe Method)

#======================================
# SQL Scripts(Outside Function)
#======================================

CREATE_MOVIES_TABLE= """   
CREATE TABLE IF NOT EXISTS Movies(                    
      Movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
      User_id TEXT,
      Movie_Name TEXT NOT NULL,
      Show_Time TEXT,
      Total_Seats INTEGER DEFAULT 50,
      Seat_Booked INTEGER DEFAULT 0

);
"""
INSERT_MOVIES=""" INSERT INTO movies(
User_id,Movie_Name,Show_Time,Total_Seats,Seat_Booked)

VALUES
('U001','Jana Nayagan','09:00:00',50,3),
('U002','Anbe Diana','11:00:00',50,4),
('U003','Arulvaan','14:00:00',50,2),
('U004','Katta Khusthi 2','16:00:00',50,3); """

GET_MOVIES=""" 
SELECT
Movie_id, User_id,Movie_Name,Show_Time,Total_Seats,Seat_Booked,
(Total_Seats-Seat_Booked) As Remaining_Seats
FROM movies;
""" 
# DB la irukura ellam movies ah eduka use aagum
# Only Remaining Seats Calculate  see the Terminal Page Only not for Website SQL(Select Query La Mattum Calculate)
