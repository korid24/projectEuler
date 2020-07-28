import os
for filename in os.listdir():
    new_name = filename.replace('(', '').replace(')','_')
    if filename[0] == '(':
        os.rename(filename, new_name)
