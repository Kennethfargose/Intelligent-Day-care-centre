from nltk.tokenize import *
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.model_selection import train_test_split
from nltk.stem import PorterStemmer
import pandas as pd
import numpy as np
#import matplotlib as plt
import tkinter
from tkinter import *


#lemmatizer = WordNetLemmatizer()
vect = TfidfVectorizer(stop_words = 'english')
ps = PorterStemmer()


'''corpus = load_files('C://Users/Sneha/Desktop/my docs/NP tech/whatsapp forward detection/Messages/Messages',load_content="true",shuffle="false")
#print (corpus)

data = []
filenames = []
target = []
token = []
final = []
words = []
'''
#load the csv file in python
filename = 'C:/Users/kenne/Desktop/reviews_Baby_5_final_dataset.csv'
data = pd.read_csv (filename)
print("#####################################The Data has been Loaded#################################################")
x = data.drop('ishelpful', axis=1)
#print (x)
y = data['reviewText']
z = data['ishelpful']

data = []
filenames = []
target = []
token = []
final = []
words = []


for i in range(0,56950):
    data.append(y[i].lower())#conversion to lower case
    #print(data)
    target.append(z[i])
    #print(target)
    #filenames.append(y.filenames[i])
      

table = { 'Data' : data,
            'Target' : target
        }

df = pd.DataFrame(table)
#print (df)

#data pre processing
num_df = df["Data"].size
print(num_df)
letters_only = ''  
def data_processing (raw_data):
    letters_only = re.sub("[^a-zA-Z]"," ",raw_data)
    words = letters_only.lower().split()
    stops = set(stopwords.words("english"))#import nltk and nltk.download('stopwords')......... 
    m = [w for w in words if not w in stops]
    return (" ".join(m))
print("data pre-processing done successfully")
          
#clean the data by calling the function above
clean_data = []
data_string = []
new_message = []

for i in range (0,num_df):
    #str(df["Data"][i],"UTF-8")
    #data_string.append(df["Data"][i].decode('windows-1252'))
    clean_data.append(data_processing(df["Data"][i]))
print("data cleaned successfully")

table1 = { 'Data' : clean_data,
            'Target' : target
        }

df1 = pd.DataFrame(table1)
#print(table1)
'''
for i in range (0,num_df):
    clean_data.append(data_processing(df1["Data"][i]))


#preprocessing the description entered by the user
new_message.append(data_processing(message))
print(new_message)

#print(clean_data)
'''

#create a new dataframe column
df1["processed_data"] = clean_data
cols2 = ["processed_data","Target"]
df1 = df1[cols2]
#print(df1)
print("data pre processing and feature extraction complete.....")

    #splitting the training and testing data
train_data,test_data,train_label,test_label = train_test_split(df1.processed_data,df1.Target,test_size=0.3)
    #print (train_data,train_label)
    #print ()
    #print(test_label)

    #TFIDF and feature extraction
vect = TfidfVectorizer(min_df = 5, max_df = 0.8, sublinear_tf = "true", use_idf = "true", analyzer = "word" ,stop_words = "english")
train_dtm = vect.fit_transform(train_data)#this is the training data set

#train_dtm = train_dtm.toarray()

test_dtm = vect.transform(test_data)#this is the testing data set
#test_dtm = test_dtm.toarray()

    #SVM classifier
clf = svm.SVC(kernel = 'linear', C = 1.0)

    #training
print("Training")
clf.fit(train_dtm,train_label)
print("Training complete")


    #testing
print("Testing")
predicted = clf.predict(test_dtm)
    #print(test_dtm,predicted)

    #Accuracy calculations
acc = np.mean(predicted==test_label)
print("Accuracy = ",acc*100)

