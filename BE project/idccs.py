import pandas as pd
import openpyxl
import xlrd
import tkinter
from tkinter import *
#import tkmessagebox

filename ="C:\\Users\\kenne\\Desktop\\dcc_final.xlsx"
data = pd.read_excel(filename)

print (data)

#take preferences from the user

selected =["Name","Address","Region","Ratings","Pricing","Food","Camera","Pre-School"]

print(selected[0])

def helloCallBack():
   print("button clicked")
#take the fields from the UI which the user wants to have filters on

#drop each of the column from data which the user doesn't need and display the list that matches

top = Tk()
# Code to add widgets will go here...


#drop down for regions
mb=  Menubutton( top, text="Click to select Region", relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

Aakurli = IntVar()
Ambernath = IntVar()
Andheri = IntVar()
Bandra = IntVar()
Bhandup = IntVar()
Bhivandi = IntVar()
Borivali = IntVar()
Chandivali = IntVar()
chembur = IntVar()
churchgate = IntVar()
charni_road = IntVar()
colaba = IntVar()
Dombivali = IntVar()
Ghatkopar = IntVar()
Jogeshwari = IntVar()
Juhu = IntVar()
Kandivali = IntVar()
khar = IntVar()
kidzee = IntVar()
Kurla = IntVar()
lalbaug = IntVar()
lokhandwala = IntVar()
lower_parel = IntVar()
Mahim = IntVar()
Malad = IntVar()
marol = IntVar()
mulund = IntVar()
Mumbai = IntVar()
mumbai_central = IntVar()
nalasopara = IntVar()
parel = IntVar()
prabhadevi = IntVar()
sandhurst_road = IntVar()
santacruz = IntVar()
sion = IntVar()
tardeo = IntVar()
thane = IntVar() 
vasai = IntVar()
vikhroli = IntVar()
vile_parle = IntVar()
Virar = IntVar()
vadala = IntVar()
Worli = IntVar() 

mb.menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup",
                          variable=ketchVar )


mb.menu.add_checkbutton ( label="Aakurli",
                          variable=Aakurli )
mb.menu.add_checkbutton ( label="Ambernath",
                          variable=Ambernath )
mb.menu.add_checkbutton ( label="Andheri",
                          variable=Andheri )
mb.menu.add_checkbutton ( label="Bandra ",
                          variable=Bandra )
mb.menu.add_checkbutton ( label="Bhandup",
                          variable=Bhandup )
mb.menu.add_checkbutton ( label="Bhivandi",
                          variable=Bhivandi )
mb.menu.add_checkbutton ( label="Borivali",
                          variable=Borivali )
mb.menu.add_checkbutton ( label="Chandivali",
                          variable=Chandivali )
mb.menu.add_checkbutton ( label="chembur",
                          variable=chembur )
mb.menu.add_checkbutton ( label="churchgate",
                          variable=churchgate )
mb.menu.add_checkbutton ( label="charni road",
                          variable=charni_road )
mb.menu.add_checkbutton ( label="colaba ",
                          variable=colaba )
mb.menu.add_checkbutton ( label="Dombivali",
                          variable=Dombivali )
mb.menu.add_checkbutton ( label="Ghatkopar",
                          variable=Ghatkopar )
mb.menu.add_checkbutton ( label="Jogeshwari",
                          variable=Jogeshwari )
mb.menu.add_checkbutton ( label="Juhu",
                          variable=Juhu )
mb.menu.add_checkbutton ( label="Kandivali",
                          variable=Kandivali )
mb.menu.add_checkbutton ( label="khar",
                          variable=khar )
mb.menu.add_checkbutton ( label="kidzee",
                          variable=kidzee )
mb.menu.add_checkbutton ( label="Kurla",
                          variable=Kurla )
mb.menu.add_checkbutton ( label="lalbaug",
                          variable=lalbaug )
mb.menu.add_checkbutton ( label="lokhandwala",
                          variable=lokhandwala )
mb.menu.add_checkbutton ( label="lower parel",
                          variable=lower_parel )
mb.menu.add_checkbutton ( label="Mahim",
                          variable=Mahim )
mb.menu.add_checkbutton ( label="Malad",
                          variable=Malad )
mb.menu.add_checkbutton ( label="marol",
                          variable=marol )
mb.menu.add_checkbutton ( label="mulund",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="Mumbai",
                          variable=Mumbai )
mb.menu.add_checkbutton ( label="mumbai central",
                          variable=mumbai_central )
mb.menu.add_checkbutton ( label="parel",
                          variable=parel )
mb.menu.add_checkbutton ( label="prabhadevi",
                          variable=prabhadevi )
mb.menu.add_checkbutton ( label="sandhurst road",
                          variable=sandhurst_road )
mb.menu.add_checkbutton ( label="santacruz",
                          variable=santacruz )
mb.menu.add_checkbutton ( label="sion",
                          variable=sion )
mb.menu.add_checkbutton ( label="tardeo",
                          variable=tardeo )
mb.menu.add_checkbutton ( label="thane",
                          variable=ketchVar )
mb.menu.add_checkbutton ( label="vasai",
                          variable=vasai )
mb.menu.add_checkbutton ( label="vikhroli",
                          variable=vikhroli )
mb.menu.add_checkbutton ( label="vile parle",
                          variable=vile_parle )
mb.menu.add_checkbutton ( label="Virar",
                          variable=Virar )
mb.menu.add_checkbutton ( label="vadala",
                          variable=vadala )
mb.menu.add_checkbutton ( label="Worli ",
                          variable=Worli )


#drop down for ratings
mb_ratings=  Menubutton( top, text="Click to Select Ratings", relief=RAISED )
mb_ratings.grid()
mb_ratings.menu =  Menu ( mb_ratings, tearoff = 0 )
mb_ratings["menu"] =  mb_ratings.menu

star_1 = IntVar()
star_2 = IntVar()
star_3 = IntVar()
star_4 = IntVar()
star_5 = IntVar()
star_all = IntVar()


mb_ratings.menu.add_checkbutton ( label="1 star",
                          variable=star_1 )
mb_ratings.menu.add_checkbutton ( label="2 star",
                          variable=star_2 )
mb_ratings.menu.add_checkbutton ( label="3 star",
                          variable=star_3 )
mb_ratings.menu.add_checkbutton ( label="4 star",
                          variable=star_4 )
mb_ratings.menu.add_checkbutton ( label="5 star",
                          variable=star_5 )
mb_ratings.menu.add_checkbutton ( label="All",
                          variable=star_all )


#checkbox for food requirements
top.geometry("500x500")  
food = IntVar()
cctv = IntVar()
preschool = IntVar()

food_req = Checkbutton(top, text = "Food Required", variable = food,
                 onvalue = 1, offvalue = 0, height = 2, width = 10)


cctv_req = Checkbutton(top, text = "CCTV Required", variable = cctv,
                 onvalue = 1, offvalue = 0, height = 2, width = 10)

preschool_req = Checkbutton(top, text = "Pre-School Facility", variable = preschool,
                 onvalue = 1, offvalue = 0, height = 3, width = 15)

submit = Button(top, text ="submit", height = 1, width = 5, command = helloCallBack)

food_req.grid()
cctv_req.grid()
preschool_req.grid()
submit.grid()


top.mainloop()
