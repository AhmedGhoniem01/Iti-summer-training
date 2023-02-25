from tempfile import tempdir


def int_input(message):
    value = input(message)
    if(value.isdigit()):
        return value
    else:
        print("Make sure you enter numeric values!")
        int_input()

def str_input(message):
    value = input(message)
    if(value.isalpha()):
        return value
    else:
        print("Make sure you enter string values only with no numbers!")
        str_input()

# def date_input(message):
#     date = input(message)
#     if():
        

def append_data(data):
    fileobj = open("records.txt","a")
    user = (":".join(data)) + "\n"
    fileobj.write(user)
    fileobj.close()

def user_register():
    data=[]
    fname=str_input("Enter your first name: ")
    data.append(fname)
    lname=str_input("Enter your last name: ")
    data.append(lname)
    email=input("Enter your email: ")   #email validation
    data.append(email)

    password=input("Enter your password: ")
    confirm_password=input("Enter password again: ")
    while(confirm_password != password):
        print("Make sure you re enter the same password!")
        confirm_password=input("Enter password again: ")
    data.append(confirm_password)

    validated_numbers = ["010" , "012" , "011" , "015"]
    phone=int_input("Enter mobile number: ")
    while( (phone[:3] not in validated_numbers) or (len(phone) != 11) ):
        print("Make sure you enter a egyptian phone number 0f [11] digits")
        phone=int_input("Enter mobile number again: ")
    data.append(phone)
    append_data(data)
    bool,index=email_search(email)
    projects(index)

def email_search(email):
    fileobj = open("records.txt","r")
    lines = fileobj.readlines()
    for x in range(0,len(lines)):
        line = lines[x].split(":")
        if(line[2] == email):
            fileobj.close()
            return [True , x]   #multiple values
    fileobj.close()
    return [False,-1]

def password_correct(password,index):
    fileobj = open("records.txt","r")
    lines = fileobj.readlines()
    line = lines[index]
    value = ( line.split(":") )[3]
    if (password == value):
        return True
    else:
        return False

def overwrite_data(new_lines):
    fileobj = open("records.txt","w")
    fileobj.write(new_lines)
    fileobj.close()


def append_project(index,list):   #overwrite data and rewrite it
    fileobj = open("records.txt" , "r")
    file=fileobj.read()
    lines=file.split("\n")
    project=",".join(list)
    lines[index] = lines[index] + ":{" + project +"}"
    new_lines="\n".join(lines)
    fileobj.close()
    overwrite_data(new_lines)

def input_project():
    list=[]
    title=str_input("Enter the project's title: ")
    list.append(title)
    details=input("Enter the project's details: ")
    list.append(details)
    total_target=int_input("Enter the project's total target: ")
    list.append(total_target)
    start_time=input("Enter the project's start date [DD-MM-YYYY]: ") #date
    list.append(start_time)
    end_time=input("Enter the project's end date [DD-MM-YYYY]: ")   #date
    list.append(end_time)
    return list
   
def add_project(index):
    list=input_project()
    append_project(index,list)
    projects(index)

def view_projects(index):
    fileobj = open("records.txt" , "r")
    lines=fileobj.readlines()
    line = lines[index].split(":")
    for i in range(5,len(line)):
        print(line[i])
    fileobj.close()
    projects(index)

def del_project(index):
    fileobj=open("records.txt","r")
    data=fileobj.read()
    fileobj.close()
    lines=data.split("\n")
    line=lines[index]
    _projects=(line.split(":"))[5:]  #list each element is a string
    name=input("Enter project name: ")
    for i in range(0,len(_projects)):
        if(name in _projects[i]):
            temp=_projects[i]
            _projects[i]=""
            data=data.replace(temp,_projects[i])        
            found=True
            break
    
    overwrite_data(data)
    if(found):
        print("Project is deleted")
    else:
        print("Project doesn't exist")
    projects(index)


def edit_project(index):
    name=input("Enter project name to edit: ")
    list="{" + ",".join(input_project()) + "}"
    fileobj=open("records.txt","r")
    data=fileobj.read()
    fileobj.close()
    lines=data.split("\n")
    line=lines[index]
    _projects=(line.split(":"))[5:]  #list each element is a string
    for i in range(0,len(_projects)):
        if(name in _projects[i]):
            temp=_projects[i]
            _projects[i]=list
            data=data.replace(temp,_projects[i]) 
            found=True
            break
    
    overwrite_data(data)
    if(found):
        print("Project is edited")
    else:
        print("Project doesn't exist")
    projects(index)
    


def projects(index):
    print("1.Create new project \n2.View my projects \n3.Edit a project \n4.Delete a project \n5.Search for project")
    task=input("Enter the number of option you want to do: ")
    if(task=="1"):
        add_project(index)
    if(task=="2"):
        view_projects(index)
    if(task=="3"):
        edit_project(index)
    if(task=="4"):
        del_project(index)
        

def user_login():
    email=input("Enter your email: ")   #email validation
    state , index= email_search(email)   #multiple values
    if(state):  
        password=input("Enter your password: ")
        while(not password_correct(password,index)):
            print("Wrong password for the user!")
            password=input("Enter your password again: ")
        projects(index)
    else:
        print("[Email doesn't exist], try with another email or you can register with new email")
        main()
    
def main():
    print("----- Crowd Funding System ----- ")
    task=input("tap 'r' for registeration , tap 'l' to login: , tap 'x' for exit: ")
    if(task=="r"):
        user_register()
    elif(task=="l"):
        user_login()
    elif(task=="x"):
        exit()
    else:
        print("Make sure you enter a proper option!")
        main()

main()