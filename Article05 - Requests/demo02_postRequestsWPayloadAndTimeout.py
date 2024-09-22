import requests
 
payload1 = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data=payload1)
print(r.text)
 
payload2 = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload2)
print(r1.text)
 
payload3 = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload3)
print(r2.text)