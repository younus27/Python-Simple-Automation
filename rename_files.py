import os
import pdfplumber

def rename(directory):
    count = 0
    for name in os.listdir(directory):
        count+=1
        print(name)
        try:
            os.rename(os.path.join(directory,name), os.path.join(directory,str(count)+".xml"))
        except:
            pass
            

path = input("Enter the file path:\t")

try:
    rename(path)
    
except:
    print("invalid path")