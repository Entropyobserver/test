
pin = ""
count = 0
while pin !="4321":
    pin = input("PIN: ")
    count += 1
    if pin == "4321":
        if count == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print("Correct! It took you" ,count,"attempts")
    else:
        print("Wrong")   
