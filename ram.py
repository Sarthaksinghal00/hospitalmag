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
                                       font=("time new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)


        DataframeRight=LabelFrame(Dataframe,bd=5,padx=30,pady=10,relief=RIDGE,
                                       font=("time new roman",12,"bold"),text="Presceription")
        DataframeRight.place(x=990,y=5,width=260,height=350)


    # ===========button frame ================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1330,height=70)
        
        
        # ===========detail  frame ================
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

        self.txtPrescription =Text(DataframeRight,font=("time new roman",12,"bold"),width=22,height=15,padx=1,pady=2)
        self.txtPrescription.grid(row=0,column=0)

        # ======================Buttons=========================

        btnPrescription=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("time new roman",12,"bold"),width=15)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionDate=Button(Buttonframe,text="Prescription Data ",bg="green",fg="white",font=("time new roman",12,"bold"),width=15)
        btnPrescriptionDate.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("time new roman",12,"bold"),width=15)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("time new roman",12,"bold"),width=15)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("time new roman",12,"bold"),width=15)
        btnClear.grid(row=0,column=4) 

        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("time new roman",12,"bold"),width=15)
        btnExit.grid(row=0,column=5)

        # ===================   Table ============================
        # =================== Scroll  bar =========================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital=ttk.Treeview(Detailsframe,columns=("nameofTable","ref","dose",
        "nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)


        scroll_x.config(command=self.hospital.xview)
        scroll_y.config(command=self.hospital.yview)

        self.hospital.heading("nameofTable", text="Name Of Table")
        self.hospital.heading("ref", text="Reference No.")
        self.hospital.heading("dose", text="Dose")
        self.hospital.heading("nooftablets", text="No Of Tablets")
        self.hospital.heading("lot", text="Lot")
        self.hospital.heading("issuedate", text="Issue Date")
        self.hospital.heading("expdate", text="Exp Date")
        self.hospital.heading("dailydose", text="Daily Date")
        self.hospital.heading("storage", text="Storage")
        self.hospital.heading("nhsnumber", text="NHS Number")
        self.hospital.heading("pname", text="Patient Name")
        self.hospital.heading("dob", text="DOB")
        self.hospital.heading("address", text="Address")
        
        self.hospital["show"] = "headings"
        
        self.hospital.column("nameofTable", width=100)
        self.hospital.column("ref", width=100)
        self.hospital.column("dose", width=100)
        self.hospital.column("nooftablets", width=100)
        self.hospital.column("lot", width=100)
        self.hospital.column("issuedate", width=100)
        self.hospital.column("expdate", width=100)
        self.hospital.column("dailydose", width=100)
        self.hospital.column("storage", width=100)
        self.hospital.column("nhsnumber", width=100)
        self.hospital.column("pname", width=100)
        self.hospital.column("dob", width=100)
        self.hospital.column("address", width=100)


        self.hospital.pack(fill=BOTH, expand=1)










       

      













root=Tk()
app=Hospital(root)
root.mainloop()




# conn=mysql.connector.connect(host='localhost',user='root',password="7057",database='new_schema')

# my_cursor=conn.cursor()

# conn.commit()
# conn.close()
# print ("jai shree ram ")

