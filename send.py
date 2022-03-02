import requests

url = 'http://localhost:5000/svo'
myobj = {'text': 'La trompette est un instrument à vent.'}
x = requests.post(url, data = myobj)

# curl -sF file=@"sample.pdf" http://localhost:5000/documents

# print(x.text)
print(x.text.encode("utf-8").decode("unicode_escape"))