import re
x='from 7990satyam200@gmail.com'
words=x.split()
email=words[1]
pieces=email.split('@')
print(pieces[1])
