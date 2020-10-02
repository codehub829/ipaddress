from request import get
ip=get('https:??api.ipify.org').text
print(f"My IP address is :{ip}")
