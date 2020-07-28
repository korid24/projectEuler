import os
for filename in os.listdir():
    new_name = filename.replace('(', '').replace(')','_')
    os.rename(filename, new_name)
