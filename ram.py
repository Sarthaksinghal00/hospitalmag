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

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Dr.Akshay Sahe",fg="red",bg="white",font=("time new roman",50,"bold"))
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
        
        lblDose=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Dose ",padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtDose.grid(row=2,column=1)

        
        lblTab=Label(DataframeLeft,font=("time new roman",12,"bold"),text="No of tablets ",padx=2,pady=6)
        lblTab.grid(row=3,column=0,sticky=W)
        txtTab=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtTab.grid(row=3,column=1)
        
        lblLot=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Lot",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtLot.grid(row=4,column=1)
        
        lblIssueDate=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Issue Date ",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtIssueDate.grid(row=5,column=1)
        
        lblExpDate =Label(DataframeLeft,font=("time new roman",12,"bold"),text="Exp Date ",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)
        
        lblDailyDose=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Daily Dose",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)
        
        lblSideEffect=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Side Effect ",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)
# ///////////// 2 part of the datafram left ====
        lblFurtherInfo=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Further Information ",padx=2,pady=6)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBp=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Blood Pressure",padx=2,pady=6)
        lblBp.grid(row=1,column=2,sticky=W)
        txtBp=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtBp.grid(row=1,column=3)
        
        lblStorage=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Storage Advice",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Medication",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Patient Id",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhs=Label(DataframeLeft,font=("time new roman",12,"bold"),text="NHS Number",padx=2,pady=6)
        lblNhs.grid(row=5,column=2,sticky=W)
        txtNhs=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtNhs.grid(row=5,column=3)

        lblPatientName=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Patient Name",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtPatientName.grid(row=6,column=3)

        lblDOB=Label(DataframeLeft,font=("time new roman",12,"bold"),text="D O B",padx=2,pady=6)
        lblDOB.grid(row=7,column=2,sticky=W)
        txtDOB=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtDOB.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("time new roman",12,"bold"),text="Patient Address",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("time new roman",12,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3)

        # ===================DAteFram right====================




       

      













root=Tk()
ob=Hospital(root)
root.mainloop()




# conn=mysql.connector.connect(host='localhost',user='root',password="7057",database='new_schema')

# my_cursor=conn.cursor()

# conn.commit()
# conn.close()
# print ("jai shree ram ")

