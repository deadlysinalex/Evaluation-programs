#deal or no Deal
print("there are 10 cases." +"\n"
      "You are trying to get as much money from the banker as possible")

def deal_or_no_deal():
    my_list = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
    choice = int(input("Please insert the higest amount of cases you want to get rid of" + "\n"
                       "This will get rid of the smaller case values!: "))
    if(choice == 1):
        average = float((500 + 1000 + 5000 + 10000 + 25000 + 50000 + 100000 + 500000 + 1000000)/9)
        offer = float(input("The banker is offering you: $"))
        print(average)
        if(average > offer):
            print("leave it!")
            print(str(my_list[1:10]) + " are the remaining values")
        else:
            print("Take the deal")
            print("you made $" + str(offer)+"!")
    elif(choice == 2):
        average = float((1000 + 5000 + 10000 + 25000 + 50000 + 100000 + 500000 + 1000000)/8)
        offer = float(input("The banker is offering you: $"))
        print(average)
        if(average > offer):
            print("leave it!")
            print(str(my_list[2:10]) + " are the remaining values")
        else:
            print("Take the deal")
            print("you made $" + str(offer)+"!")
    elif(choice == 3):
        average = float((5000 + 10000 + 25000 + 50000 + 100000 + 500000 + 1000000)/7)
        offer = float(input("The banker is offering you: $"))
        print(average)
        if(average > offer):
            print("leave it!")
            print(str(my_list[3:10]) + " are the remaining values")
        else:
            print("Take the deal")
            print("you made $" + str(offer)+"!")
                
    elif(choice == 4):
        average = float((10000 + 25000 + 50000 + 100000 + 500000 + 1000000)/6)
        offer = float(input("The banker is offering you: $"))
        print(average)
        if(average > offer):
            print("leave it!")
            print(str(my_list[4:10]) + " are the remaining values")
        else:
            print("Take the deal")
            print("you made $" + str(offer)+"!")

    elif(choice == 5):
        average = float((25000 + 50000 + 100000 + 500000 + 1000000)/5)
        offer = float(input("The banker is offering you: $"))
        print(average)
        if(average > offer):
            print("leave it!")
            print(str(my_list[5:10]) + " are the remaining values")
        else:
            print("Take the deal")
            print("you made $" + str(offer)+"!")
                
    elif(choice == 6):
        average = float((50000 + 100000 + 500000 + 1000000)/4)
        offer = float(input("The banker is offering you: $"))
        print(average)
        if(average > offer):
            print("leave it!")
            print(str(my_list[6:10]) + " are the remaining values")
        else:
            print("Take the deal")
            print("you made $" + str(offer)+"!")

    elif(choice == 7):
        average = float((100000 + 500000 + 1000000)/3)
        offer = float(input("The banker is offering you: $"))
        print(average)
        if(average > offer):
            print("leave it!")
            print(str(my_list[7:10]) + " are the remaining values")
        else:
            print("Take the deal")
            print("you made $" + str(offer)+"!")

    elif(choice == 8):
        average = float((500000 + 1000000)/2)
        offer = float(input("The banker is offering you: $"))
        print(average)
        if(average > offer):
            print("leave it!")
            print(str(my_list[8:10]) + " are the remaining values")
        else:
            print("Take the deal")
            print("you made $" + str(offer)+"!")

    elif(choice == 9):
        average = float((1000000)/1)
        offer = float(input("The banker is offering you: $"))
        print(average)
        if(average > offer):
            print("leave it!")
            print(str(my_list[9:10]) + " is the remaining values")
        else:
            print("Take the deal")
            print("you made $" + str(offer)+"!")
    elif(choice == 10):
        average = float(0)
        offer = float(input("The banker is offering you: $"))
        print(average)
        print("Take the deal")
        print("you made $" + str(offer)+"!")
    else:
        print("goodbye")
        
        

deal_or_no_deal()
