
bookings={}
movies={}
users={}
class BookingPanel:
    
    def __init__(self,bookings,movies,users):
        self.bookings=bookings
        self.movies=movies
        self.users=users
    
    def book_ticket(self,bid,uid,mid,seat_booked):
        # save the dict
        self.bookings[uid]={
            "booking_id":bid,
            "user_id":uid,
            "movie_id":mid,
            "seat_booked":seat_booked
        }
        
        # Check the Movie Id
        if mid not in self.movies:
            return
        # Available Seats =20
        #20=M001[3]
        available=self.movies[mid]["movie_availableseat"]
        # 3>20
        if seat_booked>available:
            print(f"Not Enough seats.Only{available}left")
            return
        # decrease Seats
        #[M001][20]-3
        self.movies[mid]["movie_availableseat"]-=seat_booked 
        print("Booked the Tickets Successfully !!!!")

    def cancel_booking(self,mid,seat_booked):
        # Check the Movie Id
        if mid not in self.movies:
            return    
        # Increase Seats
        self.movies[mid]["movie_availableseat"]+=seat_booked 
        print("Cancelled the Tickets Successfully !!!!")

    def view_user_bookings(self)  :
        for key,values in self.bookings.items():
            print(key,values)
        
if __name__ == "__main__" :
    users={}
    # Each Movies Seats Availablity = 20
    movies={'M001': {'movie_id': 'M001', 'movie_title': 'Jana Nayagan', 'movie_genre': 'Political Action', 'movie_show_time': '9 am', 'movie_availableseat':20},
            'M002': {'movie_id': 'M002','movie_title': 'Katta Kusthi2','movie_genre': 'Sports/Drama','movie_show_time': '11 am','movie_availableseat':20},
            'M003': {'movie_id': 'M003', 'movie_title': 'Arulvaan', 'movie_genre': 'Family Drama', 'movie_show_time': '2 pm', 'movie_availableseat': 20} ,
            'M004': {'movie_id': 'M004', 'movie_title': 'Anbe Diana', 'movie_genre': 'Comedy/Family', 'movie_show_time': '11 am', 'movie_availableseat': 20}}
    # Test by Book Ticket
    b1=BookingPanel(bookings,movies,users)
    b1.book_ticket(bid="B101",uid="U001",mid="M001",seat_booked=3)
    b1.book_ticket(bid="B102",uid="U002",mid="M002",seat_booked=5)
    b1.book_ticket(bid="B103",uid="U003",mid="M003",seat_booked=6)
    b1.book_ticket(bid="B104",uid="U004",mid="M004",seat_booked=7)
    # Decrease Seats 
    print("Seats Left:",movies["M001"]["movie_availableseat"])
    print("Seats Left:",movies["M002"]["movie_availableseat"])
    print("Seats Left:",movies["M003"]["movie_availableseat"])
    print("Seats Left:",movies["M004"]["movie_availableseat"])
    # Test by Cancel Ticket
    b1.cancel_booking(mid="M001",seat_booked=1)
    b1.cancel_booking(mid="M002",seat_booked=3)
    b1.cancel_booking(mid="M003",seat_booked=4)
    b1.cancel_booking(mid="M004",seat_booked=2)
    # Increased Seats
    print("Seats Available:" ,movies["M001"]["movie_availableseat"])
    print("Seats Available:" ,movies["M002"]["movie_availableseat"])
    print("Seats Available:" ,movies["M003"]["movie_availableseat"])
    print("Seats Available:" ,movies["M004"]["movie_availableseat"])
    # Test view by user booking
    b1.view_user_bookings()

    
       
            
            

