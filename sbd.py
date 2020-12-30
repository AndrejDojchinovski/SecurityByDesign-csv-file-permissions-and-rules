import csv
import pandas as pd
import sys

def start_setup():

    import csv
    login_Option = input("Choose login option  \n Enter 1 for Guest \n Enter 2 for User \n Enter 3 for Superuser \n Enter 4 for Administrator \n")
    login_Number = int(login_Option)

    logIn = False
    correct_login_found = False

    # Importing the data
    df = pd.read_csv('sbd.csv')

    # Login Option 1 - Guest

    if login_Number == 1:
        csvfile = open('sbd.csv')
        reader = csv.reader(csvfile)

        print("\nLogin as Guest")
        print("Please enter your credentials")
        username = input("\nUser ID:")
        password = input("Password:")

        for row in reader:
            if row[0] == username and row[1] == password and row[8] == "Guest":
                correct_login_found = True
                claims = row
                break

        if correct_login_found == False:
            print("Bad login details!")
            print("")
            start_setup()
        else:
            print("\nWelcome", claims[3])
            print("You are now logged in! \n")
            print("Your data")
            print("______________________________")
            print("User ID: ", claims[0])
            print("Account number: ", claims[2])
            print("First Name: ", claims[3])
            print("Last Name: ", claims[4])
            print("Age: ", claims[5])
            print("Current Funds: ", claims[6])
            print("Account Year: ", claims[7])
            print("User Type: ", claims[8])
            print("Account Type: ", claims[9])
            print("______________________________")
            print("Press enter to log out of system, enter any word to quit")
            #print(claims)

    ####################################################################################################################
    # Login Option 2 - User

    elif login_Number == 2:
        csvfile = open('sbd.csv')
        reader = csv.reader(csvfile)

        print("\nLogin as User")
        print("Please enter your credentials")
        username = input("\nUser ID:")
        password = input("Password:")

        for row in reader:
            if row[0] == username and row[1] == password and row[8] == "User":
                correct_login_found = True
                claims = row
                break

        if correct_login_found == False:
            print("Bad login details!")
            print("")
            start_setup()
        else:
            print("\nWelcome", claims[3])
            print("You are now logged in! \n")
            print("Your data ")
            print("______________________________")
            print("User ID: ", claims[0])
            print("Account number: ", claims[2])
            print("First Name: ", claims[3])
            print("Last Name: ", claims[4])
            print("Age: ", claims[5])
            print("Current Funds: ", claims[6])
            print("Account Year: ", claims[7])
            print("User Type: ", claims[8])
            print("Account Type: ", claims[9])
            print("______________________________")
            print("Press enter to log out of system, enter any word to quit")
            #print(claims)

    ####################################################################################################################
    # Login Option 3 - Superuser

    elif login_Number == 3:
        csvfile = open('sbd.csv')
        reader = csv.reader(csvfile)

        print("\nLogin as Superuser")
        print("Please enter your credentials")

        username = input("\nUser ID:")
        password = input("Password:")

        for row in reader:
            if row[0] == username and row[1] == password and row[8] == "Superuser":
                correct_login_found = True
                claims = row
                break

        if correct_login_found == False:
            print("Bad login details! ")
            print("")
            start_setup()
        else:
            print("\nWelcome", claims[3])
            print("You are now logged in!")

            data = input("\nEnter 1 to create new user \nEnter 2 to view the data of all Users and Guests \n")
            data_Number = int(data)

            if data_Number == 1:
                while (1):
                    with open('sbd.csv', 'a', newline='') as f:
                        w = csv.writer(f, quoting=csv.QUOTE_ALL)
                        print("\nCreating new user")
                        User_ID = input("User ID: ")
                        Password = input("Password: ")
                        Account_Number = input("Account Number: ")
                        First_Name  = input("First Name: ")
                        Last_Name  = input("Last Name: ")
                        Age = input("Age: ")
                        Current_Funds = input("Current Funds: ")
                        Account_Year = input("Account Year: ")

                        print("\nEnter 1 for Guest, Enter 2 for User")
                        UserType = input("User Type: ")
                        User_Type = int(UserType)
                        if User_Type == 1:
                            User_Type = "Guest"
                        elif User_Type == 2:
                            User_Type = "User"

                        print("\nEnter 1 for Cheque, Enter 2 for Saving, Enter 3 for Student")
                        AccountType = input("Account Type: ")
                        Account_Type = int(AccountType)
                        if Account_Type == 1:
                            Account_Type = "Cheque"
                        elif Account_Type == 2:
                            Account_Type = "Saving"
                        elif Account_Type == 3:
                            Account_Type = "Student"

                        w.writerow([User_ID, Password, Account_Number, First_Name, Last_Name, Age, Current_Funds, Account_Year, User_Type, Account_Type])
                        print("You have added a new user!")
                        #print([User_ID, Password, Account_Number, First_Name, Last_Name, Age, Current_Funds, Account_Year, User_Type, Account_Type])
                        print("\nThe data of the newly created user ")
                        print("______________________________")
                        print("User ID: ",User_ID)
                        print("Password: ", Password)
                        print("Account number: ", Account_Number)
                        print("First Name: ", First_Name)
                        print("Last Name: ", Last_Name)
                        print("Age: ", Age)
                        print("Current Funds: ", Current_Funds)
                        print("Account Year: ", Account_Year)
                        print("User Type: ", User_Type)
                        print("Account Type: ", Account_Type)
                        print("______________________________")
                        print("Press enter to log out of system, enter any word to quit")
                        break

            elif data_Number == 2:
                print("")
                print("Your data")
                print("______________________________")
                print("")
                print("User ID: ", claims[0])
                print("Account number: ", claims[2])
                print("First Name: ", claims[3])
                print("Last Name: ", claims[4])
                print("Age: ", claims[5])
                print("Current Funds: ", claims[6])
                print("Account Year: ", claims[7])
                print("User Type: ", claims[8])
                print("Account Type: ", claims[9])
                print("______________________________")

                #print(claims)

                print("")
                print("Guests and Users data ")
                df = df[~df.iloc[:,8].str.contains('Superuser') & ~df.iloc[:,8].str.contains('Admin')]
                print(df)
                print("Press enter to log out of system, press q to quit")

            else:
                print("Error, please enter 1 or 2")
                print("")
                start_setup()
    ####################################################################################################################
    # Login Option 4 - Administrator

    elif login_Number == 4:
        csvfile = open('sbd.csv')
        reader = csv.reader(csvfile)

        print("\nLogin as Admin")
        print("Please enter your credentials")

        username = input("Username:")
        password = input("Password:")

        for row in reader:
            if row[0] == username and row[1] == password and row[8] == "Admin":
                correct_login_found = True
                claims = row
                break

        if correct_login_found == False:
            print("Bad login details!")
            print("")
            start_setup()
        else:
            print("\nWelcome", claims[3])
            print("You are now logged in!")
            data = input("\nEnter 1 to create new Superuser \nEnter 2 to view the data of all Superusers \n")
            data_Number = int(data)

            if data_Number == 1:
                while (1):
                    with open('sbd.csv', 'a', newline='') as f:
                        w = csv.writer(f, quoting=csv.QUOTE_ALL)
                        print("\nCreating new Superuser")
                        User_ID = input("User ID: ")
                        Password = input("Password: ")
                        Account_Number = input("Account Number: ")
                        First_Name  = input("First Name: ")
                        Last_Name  = input("Last Name: ")
                        Age = input("Age: ")
                        Current_Funds = input("Current Funds: ")
                        Account_Year = input("Account Year: ")
                        User_Type = "Superuser"

                        print("\nEnter 1 for Cheque, Enter 2 for Saving, Enter 3 for Student")
                        AccountType = input("Account Type: ")
                        Account_Type = int(AccountType)
                        if Account_Type == 1:
                            Account_Type = "Cheque"
                        elif Account_Type == 2:
                            Account_Type = "Saving"
                        elif Account_Type == 3:
                            Account_Type = "Student"

                        w.writerow([User_ID, Password, Account_Number, First_Name, Last_Name, Age, Current_Funds, Account_Year, User_Type, Account_Type])
                        print("You have added a new Superuser!")
                        # print([User_ID, Password, Account_Number, First_Name, Last_Name, Age, Current_Funds, Account_Year, User_Type, Account_Type])
                        print("\nThe data of the newly created Superuser ")
                        print("______________________________")
                        print("User ID: ", User_ID)
                        print("Password: ", Password)
                        print("Account number: ", Account_Number)
                        print("First Name: ", First_Name)
                        print("Last Name: ", Last_Name)
                        print("Age: ", Age)
                        print("Current Funds: ", Current_Funds)
                        print("Account Year: ", Account_Year)
                        print("User Type: ", User_Type)
                        print("Account Type: ", Account_Type)
                        print("______________________________")
                        print("Press enter to log out of system, press q to quit")
                        break

            elif data_Number == 2:
                print("")
                print("Your data ")
                print("")
                print("User ID: ", claims[0])
                print("Account number: ", claims[2])
                print("First Name: ", claims[3])
                print("Last Name: ", claims[4])
                print("Age: ", claims[5])
                print("Current Funds: ", claims[6])
                print("Accou2nt Year: ", claims[7])
                print("User Type: ", claims[8])
                print("Account Type: ", claims[9])
                #print(claims)

                print("")
                print("Other's superusers data")
                df = df[~df.iloc[:,8].str.contains('User') & ~df.iloc[:,8].str.contains('Guest') & ~df.iloc[:,8].str.contains('Admin')]
                print(df)
                print("Press enter to log out of system, press q to quit")
            else:
                print("Press enter to log out of system, press q to quit")
                start_setup()

    else:
        print("\nPlease enter a number between 1 and 4!")
        start_setup()


start_setup()
while True:
    closeProgram = input("")
    if closeProgram == "":
        start_setup()
    elif closeProgram == "q":
        exit()
    else:
        exit()

