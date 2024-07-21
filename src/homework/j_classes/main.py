from class_a import die

def main():
    d = die()
    print("The Great Dice")
    print("1 : Test my Luck")
    print("2 : Exit")

    TimetoChoose = int(input("Enter your Choice : " ))

    while(TimetoChoose != 2):
        

        if TimetoChoose == 1:
            d.roll()
            print(d)           
        else:
            print("Don't be silly, chose to play or walk away..!")

        print("\nThe Great Dice") ## Use this method \n to fool the user into thinking this is a cohesive menu system. 
        print("1 : Test my Luck")
        print("2 : Exit")

        TimetoChoose = int(input("Enter your Choice : " ))

main()