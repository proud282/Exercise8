usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "admin"  and passwordInput == "1234":
    print("Done !")
    print("----- iShop -----")  # เพิ่มเอง
    print("1. Ipad  : 20,000THB")  # เพิ่มเอง
    print("2. Iphone : 25,000THB")  # เพิ่มเอง
    print("3. Itax : 1,000THB")
    userSelected = int(input(">>"))
    number = int(input("How many : "))

    if userSelected == 1:
        price1 = 20000
        print(number * price1, "THB")
    elif userSelected == 2:
        price2 = 25000
        print(number * price2, "THB")
    elif userSelected == 3:
        price3 = 1000
        print(number * price3, "THB")

