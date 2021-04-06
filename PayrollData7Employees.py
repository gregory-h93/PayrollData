print("This program will ask for the number of employees, up to seven, \n" +
      "and their hourly wages then calculate their payroll data.")
print()

def toFixed(value, digits):
    return "%.*f" % (digits, value)

while True:    #This simulates a Do Loop
    emp = 0
    print("Enter in the number of employees: ")
    numEmp = int(input())
    while numEmp < 0 or numEmp > 7:
        print("Invalid input! Number of employees must be greater than or equal to 0 and less than or equal to 7!")
        print("Enter in the number of employees: ")
        numEmp = int(input())
    hours = [0] * (7)
    payRate = [0] * (7)
    wages = [0] * (7)
    
    index = 0
    empID = [0] * (7)
    
    empID[0] = 56588
    empID[1] = 45201
    empID[2] = 78951
    empID[3] = 87775
    empID[4] = 84512
    empID[5] = 13028
    empID[6] = 75804
    
    for emp in range(0, numEmp - 1 + 1, 1):
        print("Enter the hours worked by employee #" + str(empID[index]) + ": ")
        hours[index] = int(input())
        while hours[index] < 0:
            print("Invalid input! Please enter a number greater than 0!" +
                  " Enter the hours worked by employee #" + str(empID[index]) + ": ")
            
            hours[index] = int(input())
        print("Enter the pay rate for employee #" + str(empID[index]) + ": ")
        payRate[index] = float(input())
        while payRate[index] < 0:
            print("Invalid input! Please enter a number greater than 0!" +
                  " Enter the pay rate for employee #" + str(empID[index]) + ": ")
            payRate[index] = float(input())
        index = index + 1
        
    print("PAYROLL DATA")
    print("=============")
    for index in range(0, numEmp - 1 + 1, 1):
        wages[index] = hours[index] * payRate[index]
        print("Employee #" + str(empID[index]) + " gross wages: $" + toFixed(wages[index],2))
    print("Would you like to run another payroll calculation? (Y/N)")
    again = input()
    while again != "Y" and again != "y" and again != "N" and again != "n":
        print("Please enter in (Y/N). Would you like to run the program again? (Y/N)")
        again = input()
    if not(again == "Y" or again == "y"): break   #Exit loop
print("You have chosen to end the program. Goodbye!")
