# Object Oriented Code
# Logical Parts

movies={}
class MoviePanel:
    def __init__(self,movies) :
        self.movies=movies
              
    def add_new_movies(self,mid,mtitle,mgenre,mshow_time,mavailableseats):
        self.movies[mid]={
            "movie_id":mid,
            "movie_title":mtitle,
            "movie_genre":mgenre,
            "movie_show_time":mshow_time,
            "movie_available_seat":int(mavailableseats)
        } 
        print(" Movie Details Added Successfully!!!!")   
    def view_movie(self):
        for key,value in self.movies.items():
            print(key,value)

    def update_movie(self,mid,mshow_time,mavailableseats):
        # check movie id is there
        if mid in self.movies:
            self.movies[mid]["movie_show_time"]=mshow_time
            self.movies[mid]["movie_available seat"]=mavailableseats
            print("Movie Successfully Updated!!!!!")
        else:
            print(f"Movie ID{mid} not Found")   

    def search_movie(self,mid):
        if mid in self.movies:
            movie=self.movies[mid]
            print("Movie is Found") 
            print(f"Title:{movie['movie_title']}") 
            print(f"Genre:{movie['movie_genre']}") 
            print(f"Show_time:{movie['movie_show_time']}") 
        else:
            print(f"Movie ID{mid}not Found")     
           
    def delete_movie(self,mid):
        if mid in self.movies:
            del self.movies[mid]
            print("Movie Successfully Deleted!!!")
        else:   
            print(f"Movie ID{mid} not Found")  
    
if __name__ == "__main__" :
    movies={}
    movie=MoviePanel(movies)
    # Add New Movies 
    movie.add_new_movies("M001","Jana Nayagan","Political Action Thriller","9 AM","50")
    movie.add_new_movies("M002","Katta Kusthi2","Sports/Drama","11 AM","60")
    movie.add_new_movies("M003","Arulvaan","Family Drama","2 PM","55")
    movie.add_new_movies("M004","Anbe Diana","Comedy/Family","11 AM","70")
    movie.view_movie()
    print(movies)
    movie.update_movie("M004",mshow_time="4PM",mavailable_seats="False")
    movie.search_movie("M001")
    movie.delete_movie("M004")

    
    
              