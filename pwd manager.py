Title = input("Enter The Account Type:")
EMail = input("Enter The Email:")
UserName = input("Enter The Username:")
Password = input("Enter The Password:")


if __name__ == "__main__":

    file = open(Title + ".txt","a")
    file.write("Plattform:" +Title + "\n")
    file.write("E-Mail:" + EMail + "\n")
    file.write("UserName:" + UserName + "\n")
    file.write("Password:" + Password + "\n")
    file.close()
