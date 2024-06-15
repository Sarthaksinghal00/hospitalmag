from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1340x800+0+0")

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Dr. Akshay Sahe", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # -----------------------Data frame---------------------------------

        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1330, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE, font=("times new roman", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=5, padx=30, pady=10, relief=RIDGE, font=("times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=260, height=350)

        # ===========button frame===============
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1330, height=70)

        # ===========detail frame===============
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1330, height=90)

        # ============Dateframe left==========================
        lblNameTablet = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Tablet Name", padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0, sticky=W)

        comNameTablet = ttk.Combobox(DataframeLeft, state="readonly", font=("times new roman", 12, "bold"), width=33)
        comNameTablet['value'] = ("Nice", "Corona Vaccine", "Paracetamol", "Aspirin", "Ibuprofen")
        comNameTablet.current(0)
        comNameTablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Reference Number", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Dose", padx=2, pady=6)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtDose.grid(row=2, column=1)

        lblTab = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="No of Tablets", padx=2, pady=6)
        lblTab.grid(row=3, column=0, sticky=W)
        txtTab = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtTab.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Lot", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtLot.grid(row=4, column=1)

        lblIssueDate = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Issue Date", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Exp Date", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Daily Dose", padx=2, pady=6)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Side Effect", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtSideEffect.grid(row=8, column=1)

        # ///////////// 2nd part of the DataFrame left ====
        lblFurtherInfo = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Further Information", padx=2, pady=6)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtFurtherInfo.grid(row=0, column=3)

        lblBp = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Blood Pressure", padx=2, pady=6)
        lblBp.grid(row=1, column=2, sticky=W)
        txtBp = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtBp.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Storage Advice", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Medication", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Patient ID", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhs = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="NHS Number", padx=2, pady=6)
        lblNhs.grid(row=5, column=2, sticky=W)
        txtNhs = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtNhs.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Patient Name", padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtPatientName.grid(row=6, column=3)

        lblDOB = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="D.O.B", padx=2, pady=6)
        lblDOB.grid(row=7, column=2, sticky=W)
        txtDOB = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtDOB.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Patient Address", padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        txtPatientAddress.grid(row=8, column=3)

        # Prescription text area
        self.txtPrescription = Text(DataframeRight, font=("times new roman", 12, "bold"), width=37, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ==================== Button Functions =========================

        def iPrescription():
            self.txtPrescription.insert(END, "Name of Tablets:\t\t\t" + comNameTablet.get() + "\n")
            self.txtPrescription.insert(END, "Reference No:\t\t\t" + txtref.get() + "\n")
            self.txtPrescription.insert(END, "Dose:\t\t\t" + txtDose.get() + "\n")
            self.txtPrescription.insert(END, "Number of Tablets:\t\t\t" + txtTab.get() + "\n")
            self.txtPrescription.insert(END, "Lot:\t\t\t" + txtLot.get() + "\n")
            self.txtPrescription.insert(END, "Issue Date:\t\t\t" + txtIssueDate.get() + "\n")
            self.txtPrescription.insert(END, "Expiry Date:\t\t\t" + txtExpDate.get() + "\n")
            self.txtPrescription.insert(END, "Daily Dose:\t\t\t" + txtDailyDose.get() + "\n")
            self.txtPrescription.insert(END, "Storage Advice:\t\t\t" + txtStorage.get() + "\n")
            self.txtPrescription.insert(END, "Blood Pressure:\t\t\t" + txtBp.get() + "\n")
            self.txtPrescription.insert(END, "Patient Name:\t\t\t" + txtPatientName.get() + "\n")
            self.txtPrescription.insert(END, "Date of Birth:\t\t\t" + txtDOB.get() + "\n")
            self.txtPrescription.insert(END, "Patient Address:\t\t\t" + txtPatientAddress.get() + "\n")

        def iPrescriptionData():
            conn = mysql.connector.connect(host="localhost", user="root", password="your_password", database="hospital")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                comNameTablet.get(),
                txtref.get(),
                txtDose.get(),
                txtTab.get(),
                txtLot.get(),
                txtIssueDate.get(),
                txtExpDate.get(),
                txtDailyDose.get(),
                txtStorage.get(),
                txtBp.get(),
                txtPatientName.get(),
                txtDOB.get(),
                txtPatientAddress.get(),
                txtFurtherInfo.get(),
                txtSideEffect.get(),
                txtNhs.get(),
                txtMedicine.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Data inserted successfully")

        def iDelete():
            comNameTablet.set("")
            txtref.delete(0, END)
            txtDose.delete(0, END)
            txtTab.delete(0, END)
            txtLot.delete(0, END)
            txtIssueDate.delete(0, END)
            txtExpDate.delete(0, END)
            txtDailyDose.delete(0, END)
            txtStorage.delete(0, END)
            txtBp.delete(0, END)
            txtPatientName.delete(0, END)
            txtDOB.delete(0, END)
            txtPatientAddress.delete(0, END)
            txtFurtherInfo.delete(0, END)
            txtSideEffect.delete(0, END)
            txtNhs.delete(0, END)
            txtMedicine.delete(0, END)
            self.txtPrescription.delete("1.0", END)

        def iExit():
            iExit = messagebox.askyesno("Hospital Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        # ==================== Buttons =========================

        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("times new roman", 12, "bold"), width=23, command=iPrescription)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("times new roman", 12, "bold"), width=23, command=iPrescriptionData)
        btnPrescriptionData.grid(row=0, column=1)

        btnDelete = Button(Buttonframe, text="Delete", bg="red", fg="white", font=("times new roman", 12, "bold"), width=23, command=iDelete)
        btnDelete.grid(row=0, column=2)

        btnExit = Button(Buttonframe, text="Exit", bg="red", fg="white", font=("times new roman", 12, "bold"), width=23, command=iExit)
        btnExit.grid(row=0, column=3)

        # ==================== Details Frame =========================

        scroll_x = Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("nameoftablets", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose", "storage", "bp", "patientname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Expiry Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("bp", text="Blood Pressure")
        self.hospital_table.heading("patientname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Patient Address")

        self.hospital_table["show"] = "headings"
        self.hospital_table.column("nameoftablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("bp", width=100)
        self.hospital_table.column("patientname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()
