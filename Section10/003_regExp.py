import re


'''
. anything  -but not new lines

+ one or more of

* zero or more of

? zero or one of
'''
email="atul@google.com"


express='[a-z\.]+'
print(re.findall(express,email))