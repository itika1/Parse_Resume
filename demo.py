import PyPDF2
import re
import os
import pandas as pd 
import fitz 
import spacy
path = "C:/Users/Itika.Sarkar/.vscode/File_Operation/CV_Folder/" # This is our folder where all CVs are stored
Name=[]
Qualification=[]
#The following are some keywords that has been found in CVs who are holding PG degree 
m='M.Tech'
p='Post Graduate'
g='PG'
e='MEng'
o='Master of'
n='MBA'
for fp in os.listdir(path):
    pdfFileObj = open(os.path.join(path, fp), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for i in range(0,pdfReader.getNumPages()):
        name= pdfReader.getPage(i).extractText().strip().split("\n")[0]
    Name.append(name)

for fp in os.listdir(path):
    pdfFileObj = open(os.path.join(path, fp), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for i in range(0,pdfReader.getNumPages()):
        PageObj = pdfReader.getPage(i)
        Text = PageObj.extractText()
        if re.search(m,Text) or re.search(p,Text) or re.search(g, Text) or re.search(e, Text) or re.search(o, Text) or re.search(n,Text):
            Q='PG'
            break
        else:
            Q='UG'
    Qualification.append(Q)
result = pd.DataFrame({'Name': Name, 'Qualification': Qualification})
result= result.to_csv('Result.csv', index=False)
