#Reality
#Progarammed by Beau Saunders (BJS)
#This program / code is copyrighted and therefor cannot be copied at any time!
#Version 0.1
#Windows Compatible
#Start of program.
 
import time
import os
 
global jobList, balance
 
jobList = ("Cashier")
 
balance = ("£" + "10")
 
#This clears the shell: os.system('cls')
 
def jobCentre():
 
    print("Cash : " + balance)
 
    print("\nWelcome to the job centre!\n")
    print("Here you can choose which job you would like to do\n")
    jobListAsk = input("If you would like to see the current, available jobs, type 'jobs'. If not type 'next' ").upper()
 
    if jobListAsk == "JOBS":
 
        print("Here is the current available jobs: \n")
 
        print(jobList)
 
        jobChoose = input("Type the name of your chosen job when you are ready ")
 
        if jobChoose == "CASHIER":
 
            print("You have chosen the job as a cashier!")
 
    elif jobListAsk == "NEXT":
 
        jobQuitAsk = input("If you would like to quit your current job and choose a new one type 'quit'. If not type 'bye' to leave the Job Centre.").upper()
 
        if jobQuitAsk == "QUIT":
 
            print("You have now quit your job, here is the job list: ")
 
            print(jobList)
 
        elif jobQuitAsk == "BYE":
 
            print("Thank you for visiting the job centre, bye!")
             
            openWorld()
 
        else:
 
            print("Something went wrong, the Job Centre will re-open")
 
            time.sleep(3)
 
            os.system('cls')
 
            time.sleep(1)
 
            jobCentre()
 
    else:
 
        print("Something went wrong, the Job Centre will re-open")
 
        time.sleep(3)
 
        os.system('cls')
 
        time.sleep(1)
 
        jobCentre()
 
def openWorld():
 
    print("OUTSIDE")
 
 
     
 
def firstMenu():
 
    print("\t\t\t\t     REALITY\n")
 
    time.sleep(2)
     
    print("This game is made from pure code and not one part of this program was made in a game engine. \n")
 
    time.sleep(3)
 
    ready = input("Ready to start? Type Y ").upper()
 
    if ready == "Y":
 
        os.system('cls')
 
        jobCentre()
 
    else:
 
        print("Something went wrong, the program will now start again")
 
        time.sleep(3)
 
        os.system('cls')
 
        time.sleep(1)
 
        firstMenu()
     
firstMenu()
