import requests
# generating headers
# code header
code = """
n=int(input())
for i in range(0,n):
    print(i)
"""
# input header
input_str = """dsa
"""
# combining the header with a cool name
payload = {'code': code, 'input_str': input_str}

# requesting the data with the payloads
r = requests.get('http://192.168.1.24:1212/compile/', params=payload)

# printing the json output
print(r.json())

# printing the error Code
print(r.status_code)