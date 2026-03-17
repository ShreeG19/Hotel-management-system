from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DiningArea:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Details")
        self.root.geometry("1640x670+500+420")
        
    # ===================== variable =================
        self.var_orderID = StringVar()
        x = random.randint(10000,999999)
        self.var_orderID.set(str(x))
        
        self.var_cust_name = StringVar()
        self.var_mobile = StringVar()
        self.var_foodType = StringVar()

        
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
        lbl_orderID = Label(lableFrameLeft, text="Customer Ref :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_orderID.grid(row=0, column=0, sticky=W)
        enty_orderID = ttk.Entry(lableFrameLeft, textvariable=self.var_ref, font=("Arial", 14, "bold"), width=26, state="readonly")
        enty_orderID.grid(row=0, column=1)
        
        # cust name
        lbl_cust_name = Label(lableFrameLeft, text="Customer Name :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)
        txt_cust_name = ttk.Entry(lableFrameLeft, textvariable=self.var_cust_name, font=("Arial", 14, "bold"), width=26)
        txt_cust_name.grid(row=1, column=1)
        
        # mobile number
        lbl_mobile = Label(lableFrameLeft, text="Mobile Number :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=4, column=0, sticky=W)
        txt_mobile = ttk.Entry(lableFrameLeft, textvariable=self.var_mobile, font=("Arial", 14, "bold"), width=26)
        txt_mobile.grid(row=4, column=1)
        
        # FoodType
        lbl_foodType = Label(lableFrameLeft, text="Gender :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_foodType.grid(row=2, column=0, sticky=W)
        combo_foodType = ttk.Combobox(lableFrameLeft, textvariable=self.var_gender, font=("Arial", 14), width=22, state="readonly")
        combo_foodType['values'] = ("South Indian","North Indian", "Itlics", "Chines","France","Korean")
        combo_foodType.current(0)
        combo_foodType.grid(row=2, column=1)
        
        
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
        
        
        
        
        
        
        
        
    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomno.get() == "" or self.var_roomtype.get() == "":
            messagebox.showerror("Error", "All fields are mandatory", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO details (floor, RoomNo, order) VALUES (%s, %s, %s)", (
                    self.var_floor.get(),
                    self.var_roomno.get(),
                    self.var_order.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Food Ordered Successfully", parent=self.root)
                self.reset()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
    
    # === Fetch data ===
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM diningarea")
            rows = my_cursor.fetchall()
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.close()
        except:
            pass
    
    # === Get cursor ===
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_order.set(row[2])
    
    # === Update ===
    def update(self):
        if self.var_roomno.get() == "":
            messagebox.showerror("Error", "Please select a order to update", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE details SET RoomNo=%s, floor=%s, order=%s WHERE orderID=%s", (
                self.var_roomno.get(),
                self.var_floor.get(),
                self.var_order.get(),
                self.var_orderID.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "food order Updated Successfully", parent=self.root)
            self.reset()
        except Exception as es:
            messagebox.showwarning("Warning", f"Update failed: {str(es)}", parent=self.root)
    
    # === Delete ===
    def mDelete(self):
        if self.var_roomno.get() == "":
            messagebox.showerror("Error", "Please select a order ID to delete", parent=self.root)
            return
            
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to Delete this Order Details", parent=self.root)
        if mDelete > 0:
            try:
                conn = mysql.connector.connect(host="localhost", user="pythonuser", password="mypassword", database="management")
                my_cursor = conn.cursor()
                query = "DELETE FROM diningarea WHERE orderID=%s"
                value = (self.var_roomno.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset()
                messagebox.showinfo("Success", "order deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Delete failed: {str(es)}", parent=self.root)
    
    # === Reset ===
    def reset(self):
        self.var_orderID.set("")
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_order.set("")

if __name__ == "__main__":
    root = Tk()
    obj = DiningArea(root)
    root.mainloop()