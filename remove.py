import requests
import random

n = random.choice([1,2,3,4,5,6,7,8,9])
num = str(n)
path = input("Enter the path of the image: ")
response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open(path, 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'KRAwgLBL583cxtaZ5UdQf32k'},
    )
if response.status_code == requests.codes.ok:
    with open('no-bg'+ num +'.png', 'wb') as out:
     out.write(response.content)
else:
    print("Error:", response.status_code, response.text)
