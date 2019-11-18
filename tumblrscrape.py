import requests

# put the extensions you want to test in here
# ex. url_things = ['one extension', 'another']

url_input = input("Enter urls here, separate by using ',': ")
url_things = []
url_things.append(url_input)

#if you want to look at number-only urls (ex. 384), use a loop
#for x in range(100,999):
#	url_things.append(x)

# name of the text file with the stored extensions
filename = 'available_extensions.txt'

available = []

for t in url_things:
    r = requests.get(f'http://{t}.tumblr.com')
    if r.status_code == 200:
        print(f'{t} Exists')
    elif r.status_code == 404:
        print(f'{t} Is Vacant!')
        available.append(t)
    else:
        print(f'{t}: Status Code {r.status_code}')

with open(filename, 'w') as f:
    f.write('Available extensions:\n\n' + '\n'.join(n for n in available))

print(f'Available extensions saved in "{filename}".')
