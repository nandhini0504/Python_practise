s_username="EMC"
s_password="123"
uname=input("Enter value for username")
password=input("Enter value for password")

def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False
a=validate()
print(a)
