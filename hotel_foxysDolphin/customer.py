from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1640x670+500+420")
        
        # ===================== variable =================
        self.var_ref = StringVar()
        x = random.randint(1000000,99999999)
        self.var_ref.set(str(x))
        
        self.var_cust_name = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()
        
        # ==================== title ====================
        lbl_title = Label(self.root, text="Add Customer Details", font=("times new roman", 30, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1640, height=60)
        
        # ======================logo ======================
        try:
            img2 = Image.open("/home/kalilinux/Documents/V S code files/Projects_for/hotel_foxysDolphin/images/logo.png")
            img2 = img2.resize((100, 54), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            lilimg = Label(self.root, image=self.photoimg2, bd=0.5, relief=RIDGE)
            lilimg.place(x=4, y=2, width=100, height=54)
        except:
            pass
        
        # ======================lableFrame ======================
        lableFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 20, "bold"), padx=2)
        lableFrameLeft.place(x=5, y=75, width=490, height=580)
        
        # ======================lables and Entries ======================
        # cust_ref
        lbl_cust_ref = Label(lableFrameLeft, text="Customer Ref :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        enty_ref = ttk.Entry(lableFrameLeft, textvariable=self.var_ref, font=("Arial", 14, "bold"), width=26, state="readonly")
        enty_ref.grid(row=0, column=1)
        
        # cust name
        lbl_cust_name = Label(lableFrameLeft, text="Customer Name :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)
        txt_cust_name = ttk.Entry(lableFrameLeft, textvariable=self.var_cust_name, font=("Arial", 14, "bold"), width=26)
        txt_cust_name.grid(row=1, column=1)
        
        # gender combobox
        lbl_gender = Label(lableFrameLeft, text="Gender :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=2, column=0, sticky=W)
        combo_gender = ttk.Combobox(lableFrameLeft, textvariable=self.var_gender, font=("Arial", 14), width=22, state="readonly")
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=2, column=1)
        
        # Post Code
        lbl_post = Label(lableFrameLeft, text="Post Code :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_post.grid(row=3, column=0, sticky=W)
        txt_post = ttk.Entry(lableFrameLeft, textvariable=self.var_post, font=("Arial", 14, "bold"), width=26)
        txt_post.grid(row=3, column=1)
        
        # mobile number
        lbl_mobile = Label(lableFrameLeft, text="Mobile Number :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=4, column=0, sticky=W)
        txt_mobile = ttk.Entry(lableFrameLeft, textvariable=self.var_mobile, font=("Arial", 14, "bold"), width=26)
        txt_mobile.grid(row=4, column=1)
        
        # Email
        lbl_email = Label(lableFrameLeft, text="Email ID :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_email.grid(row=5, column=0, sticky=W)
        txt_email = ttk.Entry(lableFrameLeft, textvariable=self.var_email, font=("Arial", 14, "bold"), width=26)
        txt_email.grid(row=5, column=1)
        
        # nationality
        lbl_nationality = Label(lableFrameLeft, text="Nationality :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_nationality.grid(row=6, column=0, sticky=W)
        combo_nationality = ttk.Combobox(lableFrameLeft, textvariable=self.var_nationality, font=("Arial", 14), width=22, state="readonly")
        combo_nationality['values'] = ("India", "Non-Indian")
        combo_nationality.current(0)
        combo_nationality.grid(row=6, column=1)
        
        # idproof type combobox
        lbl_id_proof = Label(lableFrameLeft, text="ID Proof :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_id_proof.grid(row=7, column=0, sticky=W)
        combo_id_proof = ttk.Combobox(lableFrameLeft, textvariable=self.var_id_proof, font=("Arial", 14), width=22, state="readonly")
        combo_id_proof['values'] = ("Aadhaar Card", "Passport", "ID card", "Driving Licence", "PAN Card")
        combo_id_proof.current(0)
        combo_id_proof.grid(row=7, column=1)
           
        # id number
        lbl_id_number = Label(lableFrameLeft, text="ID Number :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_id_number.grid(row=8, column=0, sticky=W)
        txt_id_number = ttk.Entry(lableFrameLeft, textvariable=self.var_id_number, font=("Arial", 14, "bold"), width=26)
        txt_id_number.grid(row=8, column=1)

        # address
        lbl_address = Label(lableFrameLeft, text="Address :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_address.grid(row=9, column=0, sticky=W)
        txt_address = ttk.Entry(lableFrameLeft, textvariable=self.var_address, font=("Arial", 14, "bold"), width=26)
        txt_address.grid(row=9, column=1)
        
        # ==================== btns ==================
        btn_frame = Frame(lableFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=425, width=458, height=91)
        
        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("Arial", 18, "bold"), bg="black", fg="gold", width=15)
        btnAdd.grid(row=0, column=0, padx=1)
        
        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("Arial", 18, "bold"), bg="black", fg="gold", width=15)
        btnUpdate.grid(row=0, column=1, padx=1)
        
        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("Arial", 18, "bold"), bg="black", fg="gold", width=15)
        btnDelete.grid(row=1, column=0, padx=2)
        
        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("Arial", 18, "bold"), bg="black", fg="gold", width=15)
        btnReset.grid(row=1, column=1, padx=2)
        
        # ==================== table frame search system ==================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 20, "bold"), padx=2)
        Table_Frame.place(x=520, y=75, width=1110, height=580)
        
        lblSearchBy = Label(Table_Frame, text="Search Ref :", font=("Arial", 15, "bold"), bg="black", fg="gold")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2, pady=2)
        
        self.search_var = StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("Arial", 15), width=20, state="readonly")
        combo_search['values'] = ("Mobile Number", "Ref Number")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2, pady=2)
        
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("Arial", 14, "bold"), width=26)
        txtSearch.grid(row=0, column=2, padx=2, pady=2)
        
        btnSearch = Button(Table_Frame, text="Search", command=self.search, font=("Arial", 18, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)
        
        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=("Arial", 18, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        # ==================== show table frame ==================
        detail_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        detail_table.place(x=0, y=50, width=1100, height=493)
        scroll_x = ttk.Scrollbar(detail_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_table, orient=VERTICAL)
        
        self.Cust_Details_Table = ttk.Treeview(detail_table, columns=("ref", "name", "gender", "post", "mobile", "email", "nationality", "id_proof", "id_number", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="Post Code")
        self.Cust_Details_Table.heading("mobile", text="Mobile No")
        self.Cust_Details_Table.heading("email", text="Email-ID")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("id_proof", text="ID Proof")
        self.Cust_Details_Table.heading("id_number", text="ID Number")
        self.Cust_Details_Table.heading("address", text="Address")
        
        self.Cust_Details_Table["show"] = "headings"
        
        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=150)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("id_proof", width=120)
        self.Cust_Details_Table.column("id_number", width=120)
        self.Cust_Details_Table.column("address", width=150)
        
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()
        
    def add_data(self):
        if not all([self.var_mobile.get(), self.var_id_number.get(), self.var_address.get(), 
                   self.var_cust_name.get(), self.var_gender.get(), self.var_post.get(), 
                   self.var_nationality.get()]):
            messagebox.showerror("Error", "All fields are mandatory", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO customer (ref, name, gender, post, mobile, email, nationality, id_proof, id_number, address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been inserted", parent=self.root)
                self.reset()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
                
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM customer")
            rows = my_cursor.fetchall()
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.close()
        except:
            pass
        
    def get_cuersor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]
        
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_post.set(row[3])
        self.var_mobile.set(row[4])
        self.var_email.set(row[5])
        self.var_nationality.set(row[6])
        self.var_id_proof.set(row[7])
        self.var_id_number.set(row[8])
        self.var_address.set(row[9])
    
    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please Enter Mobile Number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE customer SET name=%s, gender=%s, post=%s, mobile=%s, email=%s, nationality=%s, id_proof=%s, id_number=%s, address=%s WHERE ref=%s", (
                    self.var_cust_name.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get(),
                    self.var_ref.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "Record Updated Successfully", parent=self.root)
                self.reset()
            except Exception as es:
                messagebox.showwarning("Warning", f"Update failed: {str(es)}", parent=self.root)
            
    def mDelete(self):
        if self.var_ref.get() == "":
            messagebox.showerror("Error", "Please select a record to delete", parent=self.root)
            return
            
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to Delete this customer", parent=self.root)
        if mDelete > 0:
            try:
                conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
                my_cursor = conn.cursor()
                query = "DELETE FROM customer WHERE ref=%s"
                value = (self.var_ref.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset()
                messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Delete failed: {str(es)}", parent=self.root)
    
    def reset(self):
        x = random.randint(1000000, 99999999)
        self.var_ref.set(str(x))
        self.var_cust_name.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_id_number.set("")
        self.var_address.set("")
   
    def search(self):
        if self.txt_search.get() == "":
            messagebox.showerror("Error", "Please enter search term", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor = conn.cursor()
            search_by = self.search_var.get()
            
            if search_by == "Mobile Number":
                query = "SELECT * FROM customer WHERE mobile LIKE %s"
            else:
                query = "SELECT * FROM customer WHERE ref LIKE %s"
                
            my_cursor.execute(query, ('%' + self.txt_search.get() + '%',))
            rows = my_cursor.fetchall()
            
            if len(rows) != 0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert("", END, values=i)
            else:
                messagebox.showinfo("Info", "No records found")
            
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Search failed: {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
