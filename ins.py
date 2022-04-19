import instaloader

ob = instaloader.Instaloader()
user = input("Enter user name: ")

ob.download_profile(user,profile_pic_only=True)
