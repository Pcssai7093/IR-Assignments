import os
class list:
    def __init__(self,docId):
        self.docId=docId
        self.list=None

class listhead:
    def __init__(self,word):
        self.word=word
        self.list=None

path="C:/Users/chandra sekhar/Desktop/chandra sekhar imp/SEM-5/IR/practice assignments/th-dataset"
os.chdir(path)
invertedIndex=[]

def read_file(file_path):
    with open(file_path,'r',encoding="utf8") as f:
        print(f.read())
        print("\n")


for file in os.listdir():
    file_path=f"{path}\{file}"
    read_file(file_path)