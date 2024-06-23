def main():
        print("Homework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum Odd Numbers")
        print("3 - Exit")

        option = int(input("Enter your choice"))
        ThoseChoices(option)

def ThoseChoices(option):
       if option == 1:
              Factorial()
       elif option == 2:
              SumOddNumbers()
       elif option == 3:
              exit()
       else:
              print("Invalid option inserted : Returning to main menu...")
              main()
       
     
def Factorial():
    import repetition
    num = int(input("Enter a number in the range 0 and 10 with 10 not inclusive."))
    if num > 0 and num < 10:
           print("The factor of", num, "is: ",repetition.get_factorial(num))
    else:
           print("Invalid numbers inserted : Please insert a number within a range of 0 - 10 with 10 being non inclusive.")

def SumOddNumbers():
       import repetition
       num = int(input("Enter a number in the range 0 and 100 with 100 not inclusive."))
       if num > 0 and num < 100:
              print("The sum of", num, "is: ",repetition.sum_odd_numbers(num))
       else:
              print("Invalid numbers inserted : Please insert a number within a range of 0 - 100 with 100 being non inclusive.")
        
def Exit():
       ReallyReally = input("Do you wish to exit? : Press [y] to quit [n] to continue")
       if ReallyReally == "y":
              print("Exiting..")
       elif ReallyReally == "n":
              print("Returning to Main Menu...")
              main()
       else:
              "Invalid option : Press [y] to quit, press [n] to continue."
              
            