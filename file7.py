s_username="nandhini"
s_password="12345"
uname=input("Enter value for username")
password=input("Enter value for password")
def validate():
    if(s_username==uname and s_password==password):
        print("Correct")
    else:
        print("Wrong")
validate()