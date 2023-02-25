    fileobj = open("records.txt" , "r")
    lines=fileobj.readlines()
    line = lines[index].split(":")
    for i in range(5,len(line)):
        print(line[i])
    fileobj.close()
        #projects(index)

def edit_project(index):
    view_projects(index)
    print("Which project do you want to change?")
    order=int(input("Enter project number: "))

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

    fileobj = open("records.txt" , "r")
    file=fileobj.read()
    lines=file.split("\n")
    project=",".join(list)
    (lines[index].split(":"))[order+4] = ":{" + project +"}"
    new_lines="\n".join(lines)
    fileobj.close()
    overwrite_data(new_lines)