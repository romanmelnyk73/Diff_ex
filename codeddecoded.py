# *CODED-DECODED text*
key = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890 !,.?*/=+-()"'
text = input('Enter text you want to code : ')
coded = []
for i in text:
    key.find(i)
    coded.append(key.find(i))
print(f'CODED TEXT: {coded}')
decoded = ''
for j in coded:
    decoded += key[j]
print(f'DECODED TEXT: {decoded}')