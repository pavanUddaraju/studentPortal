# This method handles user request and provides the required information
def handleUserRequest(n, studentsData):
    if n != 1 and n != 2:
        print("Invalid request")
        return
    index = -1
    print("Enter student register number")
    regNum = int(input())
    for entry in range(len(studentsData)):
        if studentsData[entry][1] == regNum:
            index = entry
    if index == -1:
        print("Register number not found")
        return
    if n == 1:
        print(studentsData[index])
    else:
        print("select the field you want to change\n1. Name\n2. phone Number\n3. Branch")
        selectedValue = int(input())
        if selectedValue == 1:
            print("Enter name")
            name = input()
            studentsData[index][0] = name
        elif selectedValue == 2:
            print("Enter Phone Number to update")
            phoneNum = input()
            studentsData[index][3] = phoneNum
        elif selectedValue == 3:
            print("Enter branch to update")
            branch = input()
            studentsData[index][2] = branch
        else:
            print("Invalid request")
            return
        
# main method holds input dataset        
def main():
    print("Welcome to Student Portal\nSelect your request")
    studentsData = [["name1", 171, "ECE", "94947868"], ["name2", 172, "EEE", "6281655"]]
    while(1):
        print("Enter 1 to display data\nEnter 2 to update data")
        n = int(input())
        handleUserRequest(n, studentsData)
        print("press y to continue or n to exit")
        flowPoint = input()
        if flowPoint == 'n':
            print("Thanks for using student Portal")
            break
            
#method call to trigger the flow            
main()
