import requests
from getpass import getpass
 
r=requests.get('https://test.org', auth=('username', getpass()))
print(r.status_code)