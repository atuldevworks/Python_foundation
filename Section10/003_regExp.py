import re


'''
. anything  but not new lines

+ one or more of

* zero or more of

? zero or one of
'''


'''
metacharacters


   used to drop the special meeaning of character following it
[]  represeent a character class
^   Matches the beginning 
$   matches the end
.   Matches any character except new line
|   Means OR 
?   Matches zero or one occurance
*   any number of occurances
+   one or more occureances
{}  Indicate the numberof occurences of a preceding regex to match
()  enclose a group of regex

'''
# a="mango is sweet fruit. it @ is generally of yellow color , and also in green color."


# match=re.search(r"\.",a)
# print(match)

# match=re.finditer(r"[@]",a)
# for i in match:
#     print(i)
    
    
# print(re.search(r"[a]",a))

# print(re.search(r"^t",a))
# print(re.search(r"color.$",a))


pattern=".*"
data="atul@gmail.com"


x=re.findall(pattern,data)
print(x)
