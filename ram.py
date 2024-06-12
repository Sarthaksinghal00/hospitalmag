from tkinter import*
from tkinter import ttk
import random
import time 
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("hospital management system ")
        self.root.geometry("1340x800+0+0")

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="hospital managent system ",fg="red",bg="white",font=("time new roman",50,"bold"))
        lbltitle.pack(side =TOP,fill =X )

        # -----------------------Date frame ---------------------------------

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1330,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                       font=("time new roman",12,"bold"),text="patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)


        DataframeRight=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                       font=("time new roman",12,"bold"),text="Presceription")
        DataframeRight.place(x=990,y=5,width=260,height=350)


    # ===========button frame ================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1330,height=70)
        
        
        # ===========detal  frame ================
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1330,height=90)


        # ============Dateframe left ==========================
        lblNameTablet=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Table Name ",padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox(DataframeLeft,state="readonly", font=("time new roman",12,"bold"),width=33 ) 
        comNameTablet['value']=("Nice","corona vacaaine","ssdcsd","dasdasdasd","dawdasDasdasd","dasdaDAD")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)
        
        lblref=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Refernce number  ",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtref.grid(row=1,column=1)





# root=Tk()
# ob=Hospital(root)
# root.mainloop()




# conn=mysql.connector.connect(host='localhost',user='root',password="7057",database='new_schema')

# my_cursor=conn.cursor()

# conn.commit()
# conn.close()
# print ("jai shree ram ")

