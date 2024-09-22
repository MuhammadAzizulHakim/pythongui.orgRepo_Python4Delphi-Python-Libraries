import requests
 
r = requests.get('https://api.github.com/users', auth=('your username', 'your personal access token'))
 
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())