import webbrowser
from instabot import Bot
bot =Bot()

def bts():
 print(" 1.login\n","2.upload_image\n","3.upload_video\n","4.download_video\n","5.download_image\n","6.download_stories\n")
 a = int(input("Enter Your Choese:"))
 if(a==1):
    x = input("Enter Your Username:")
    y = input("Enter Your Password:")
    bot.login(username=x,password=y)
    ct()
 elif(a==2):
    img = input("Enter Image Name With extention:")
    cpt = input("Enter Your Caption:")
    bot.upload_photo(img,caption=cpt)
    ct()
 elif(a==3):
    vid = input("Enter Video Name With extention:")
    bot.upload_video(vid)
    ct()
 elif(a==4):
    post_url=input("Enter post URL:")
    download_url="https://api.instagram.com/oembed/?url="+post_url
    chrome_path = '"C:\\Program Files\\Mozilla Firefox\\firefox.exe"%s'
    webbrowser.open(download_url)
    uname = input("Enter Media_id:")
    bot.download_photo(uname)
    ct()
 elif(a==5):
    post_url=input("Enter post URL:")
    download_url="https://api.instagram.com/oembed/?url="+post_url
    chrome_path = '"C:\\Program Files\\Mozilla Firefox\\firefox.exe"%s'
    webbrowser.open(download_url)
    sname = input("Enter Media_id:")
    bot.download_video(sname)
    ct()
 elif(a==6):
    aname = input("Enter UserName:")
    bot.download_stories(aname)
    ct()
 else:
    print("Invalid Input")
    bts()

def ct():
    ch = str(input("Do You Want To Continue....(y/n):"))
    while(ch=="y"):
        bts()
    else:
        print("Visit Agine.........")
bts()
ct()
