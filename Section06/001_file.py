import os

cwd=os.getcwd()
print(cwd)
file=open(f'{cwd}/Section06/sf001.txt','w')
textData="this is sample text data "
file.write(textData)
file.close()