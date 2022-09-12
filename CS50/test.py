import requests

url = 'https://w3schools.com/python/demopage.php'

#demonstrate how to use the 'params' parameter:
x = requests.get(url, params = {"model": "Mustang"})

#print the response (the content of the requested file):
print(x.text)

#the file 'demopage.php' looks for a 'model' query string and prints its value.