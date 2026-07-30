# Movie Ticket Booking System
# Gather Requirements========================================
# Movie- Name,Id,Title,Genre,Show time,Available Seats
# User- Id,name,E-mail
# Booking-Booking Id, User id, MovieId,seats-Booked
# Display Part = Movie ,User,Booking ,Main
from src.movie import MoviePanel
from src.user import UserPanel
from src.booking import BookingPanel

def main():

    movies={}
    users={}
    bookings={}
    movie_panel=MoviePanel(movies)
    user_panel=UserPanel(users)
    booking_panel=BookingPanel(bookings,users,movies)


    while True:    
        print("-*-"*40)
        print("Welcome to Gayathri Theatre")
        print("-*-"*40)
        print("Select on Option:")
        print("1.Movie Panel")
        print("2.User Panel")
        print("3.Booking Panel")
        print("4.Exit")

        user=input("Enter User Choice:")   
        if user=="4":                             
           print("Thank You,Visit Again!!!")
           break 

        if user=="1":
            print("We are Inside Movie Panel")
            while True:
                print("-*-"*40)
                print("Welcome to Movie Panel")
                print("-*-"*40)
                print("Select on Option:")
                print("1.Add a  New Movie")
                print("2.See Movie List")
                print("3.Update the Movie")
                print("4.Search the Movie")
                print("5. Delete the Movie")
                print("6. Exit")

                movie=input("Enter Your Choice:")
                if movie=="6":
                    print("Exiting the Movie Panel")
                    break
                elif movie=="5":
                    mid=input("Enter the Movie Id:")
                    movie_panel.delete_movie(mid)
                elif movie=="4": 
                    mid=input("Enter the Movie ID:")  
                    movie_panel.search_movie(mid) 
                elif movie=="3":
                    mid=input("Enter the Movie Id:")  
                    mshow_time=input("Enter the Movie Show_time")
                    mavailable_seat=input(" Availablity Seats:")
                    movie_panel.update_movie(mid,mshow_time,mavailable_seat)
                elif movie=="2":
                    print("See all the Movies") 
                    movie_panel.view_movie() 
                elif movie=="1":
                    print("Adding a New Movie") 
                    mid=input("Enter the Movie ID:")
                    mtitle=input("Enter the Movie Title:")
                    mgenre=input("Enter the Movie Genre:")
                    mshow_time=input("Enter the Movie Show_time:")
                    mavailable_seat=input("Availablity Seats:")
                    movie_panel.add_new_movies(mid,mtitle,mgenre,mshow_time,mavailable_seat)
                else:
                    print("Invalid Input: Please Select 1/2/3/4/5/6") 

        elif user=="2":
            print("We are inside User Panel")
            while True:
                print("-*-"*40)
                print("Welcome to User Panel")
                print("-*-"*40)
                print("Select on Option:")
                print("1.Register User")
                print("2.Get User By E-mail")
                print("3.Exit")

                user=input("Enter Your Choice:")
                if user=="3":
                    print("Exiting the User Panel")
                    break
                if user=="2":
                    print("Search User By E-mail")
                    email=input("Enter Your Mail:")
                    result=user_panel.get_user_by_email(email)
                    if result:
                        print("Found user:",result)
                    else:
                        print("Found User:", None)    
                elif user=="1":
                    print("Registering the User") 
                    user_id=input("Enter Your User-ID:") 
                    name=input("Enter Your Name:")
                    email=input("Enter Your E-mail:")
                    user_panel.register_user(user_id,name,email)
                else:
                    print("Invalid Input : Please Select 1/2/3")      

        elif user=="3":
            print("We are inside Booking  Panel")
            while True:
                print("-*-"*40)
                print("Welcome to Booking Panel")
                print("-*-"*40)
                print("Select on Option:")
                print("1.Book Ticket")
                print("2.Cancel Ticket")
                print("3.View By User Bookings") 
                print("4.Exit")

                booking=input("Enter Your Choice:")
                if booking=="4":
                    print("Exiting the Booking Panel")
                    break
                if booking=="3":
                    print("Viewing By User Booking Status")
                    booking_panel.view_user_bookings()
                elif booking=="2":
                    mid=input("Enter Your Movie ID:")
                    seat_booked=int(input("Enter Your Seats_Booked:"))
                    booking_panel.cancel_booking(mid,seat_booked)
                    print("Cancelled the Ticket") 
                elif booking=="1":
                    bid=input("Enter Your Booking ID:")
                    uid=input("Enter Your User-ID:")
                    mid=input("Enter Your Movie ID:")
                    seat_booked=int(input("Enter Your Seats_Booked:"))
                    booking_panel.book_ticket(bid,uid,mid,seat_booked)
                    print("Booked Ticket") 
                else:
                    print("Invalid Input : Please Select 1/2/3/4")         
        else:
            print("Invalid Input.Please use 1/2/3/4")

    md=open("mdetails.txt","w")  
    md.write(str(movies))  
    md.close()  

    bd=open("bdetails.txt","w")  
    bd.write(str(bookings))  
    bd.close()        


if __name__=="__main__":
    main()  

    

