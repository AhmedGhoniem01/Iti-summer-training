import re
name=""
email=""
while(name==""):
    name=input("Enter valid name: ")
    if(name.isdigit()):
        name=''
while(email==""):
    email=input("Enter valid email: ")
    if not (re.search(r"[A-z0-9\.]+@([A-z])+\.(com|net)" , email)):
        email=""
print("NAME: " +name+", EMAIL: "+email)