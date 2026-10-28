import time
def TextFile(): #This function is called later on in the code to turn the printed information into a text file. def textfile(): creates the function we want to use.
    with open("InfoPiler.txt", "w") as f:
         f.write(f"----------InfoPiler.exe----------\n")
         f.write(f"----------User Information----------\n")
         f.write(f"First Name: {FName}\n")
         f.write(f"Last Name: {LName}\n")
         f.write(f"Region: {Region}\n")
         f.write(f"Cell Number: {CellNum}\n")
         f.write(f"Email: {Email}\n")
         f.write(f"Gender: {Gender}\n")
         f.write("----------End of User Information----------\n")
         f.write("----------Thank you for using InfoPiler.exe!----------\n")
def InfoPilerResult():
      print("Data will not be written to a text file.") 
      print("----------InfoPiler.exe----------")
      print("H̲e̲r̲e̲ i̲s̲ y̲o̲u̲r̲ c̲o̲d̲e̲:")
      print(f"First Name: {FName}")
      print(f"Last Name: {LName}")
      print(f"Region: {Region}")
      print(f"Cell Number: {CellNum}")
      print(f"Email: {Email}")
      print(f"Gender: {Gender}")
while True:
    print("\n ----------InfoPiler.exe----------")
    print("WARNING! You're about to input the information below")    #UI (What shows up for the user.)
    print("1. First Name:")
    print("2. Last Name:")
    print("3. Region:")
    print("4. Cell Number:")
    print("5. Email:")
    print("6. Gender:")
    Confirm=input("Do you wish to proceed? y/n (No spaces)")
    if Confirm == "y":  #This starts the program. If the user says "n", the program will end.
        FName=input("What is your first name?:")
        LName=input("What is your last name?:")
        Region=input("What is your current region?:")
        CellNum=int(input("What is your Cell Number?:"))
        EmailCombQA=input("Would you like me to combine your firstlast@gmail.com? y/n (No Spaces)")
        if EmailCombQA=="y":              #If user says "y" then first and last will combine.
            print("works")
            CombinedEmail=(f"{FName.lower()}{LName.lower()}@gmail.com")
            UseCombinedEmail=input(f"Would you like to use this email: {CombinedEmail} y/n (No Spaces)")
            if UseCombinedEmail=="y":
                Email=CombinedEmail
            else:
                Email=input("What is your email?")
        else:
            Email=input("What is your email?")
        Gender=input("What is your gender?")
        timelist=["1","2","3","4","5","6","7","8","9","10"]
        CompilingTIme=int(input("How long would you like me to compile your data for? (In seconds 1-10)"))
        print("Compiling Data...") #We're done asking the user things infromaiton related.
        for i in timelist[:CompilingTIme]:
            time.sleep(1)
            print(f"{i} seconds have passed.")
        print("Data compiled successfully!")
        print("Printing...")
        TextPrompt=input("Would you like me to turn your data into a text file? y/n (No Spaces)") #Turns into a text file for easier use.
        if TextPrompt=="y":
            TextFile()
            print("Data has been written to InfoPiler.txt")
            break
        else:
            InfoPilerResult() #This is the second function that prints the info in the terminal.  
            break
    else:
        print("Goodbye! Thank you for using InfoPiler.exe!")
        break