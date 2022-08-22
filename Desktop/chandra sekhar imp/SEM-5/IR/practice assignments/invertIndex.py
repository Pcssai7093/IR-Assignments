import os
import re

# * using dictionary ds for posting list
postingList=dict()


# * importing stop words
stopWords=[]
file1=open("stopWords.csv",'r',encoding="utf8")
stopWords=file1.read().split(',')


# * setting path for reading files
path="C:/Users/chandra sekhar/Desktop/chandra sekhar imp/SEM-5/IR/practice assignments/th-dataset"
os.chdir(path)


# * function to read file and preprocession and populating as posting list
def read_file(file_path):
    with open(file_path,'r',encoding="utf8") as f:
        words=f.read().split(" ")
        # * removing stopwords
        for str in words:
            if str in stopWords:
                words.remove(str)
        
        # * striping and removing redundaant characters
        str=re.sub("[^a-zA-Z0-9 \n\.]","",str)
        str=str.replace('.',"")
        str=str.strip()
        str=str.replace('.',"")

        # * populating into posting list
        if(postingList.get(str)==None):
            postingList[str]=[f.name.split(path+'/')[1]]
        else:
            postingList.get(str).append(f.name.split(path+'/')[1])
       

# * reading folder and invoking file read function
for file in os.listdir():
    file_path=f"{path}/{file}"
    read_file(file_path)

# * printing posting list
for key,value in postingList.items():
    print(f"{key} {value}")