# Object Oriented Code
#Logical Parts

users={}

class UserPanel:
    def __init__(self,users):
        self.users=users

    def register_user(self,uid,name,email) :
        self.users[name]={
            "user_id":uid,
            "user_name":name,
            "user_email":email
        }
        print(f"User ; {name},{email} is added Successfully !!!")

    def get_user_by_email(self,email):
        # check the Email is Register
        for name,user_data in self.users.items(): 
            if user_data["user_email"]==email:
                return user_data
                              
if __name__ == "__main__":
    users={}
    u1=UserPanel(users)
    # Register User
    u1.register_user("U001","Gayathri","123@gmail.com")
    u1.register_user("U002","Pradheepa","2102@gmail.com")
    u1.register_user("U003","Petchi","2807@gmail.com")
    u1.register_user("U004","Saranya","2424@gmail.com")
    # Test get by email
    user=u1.get_user_by_email("123@gmail.com")
    print("Found user:",user)
    user=u1.get_user_by_email("234@gmail.com")
    print("Found user:",user)
   