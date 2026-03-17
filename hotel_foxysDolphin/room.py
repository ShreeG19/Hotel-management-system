from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1640x670+500+420")
        
        # =============== Database connection =============
        self.connect_db()
        
        # =============== variables =============
        self.var_contact = StringVar()
        self.var_Check_in = StringVar()
        self.var_Check_out = StringVar()
        self.var_Room_type = StringVar()
        self.var_AvailableRoom = StringVar()
        self.var_Meal = StringVar()
        self.var_NoOfDays = StringVar()
        self.var_PaidTax = StringVar()
        self.var_SubTotal = StringVar()
        self.var_TotalCost = StringVar()
        
        # ==================== title ====================
        lbl_title = Label(self.root, text="RoomBooking Details", font=("times new roman", 30, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
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
        lableFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="RoomBooking Details", font=("times new roman", 20, "bold"), padx=2)
        lableFrameLeft.place(x=5, y=75, width=510, height=580)
        
        # ======================labels and Entries ======================
        # customer_contact
        lbl_cust_contact = Label(lableFrameLeft, text="Customer Contact :", font=("Arial", 15, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        enty_contact = ttk.Entry(lableFrameLeft, textvariable=self.var_contact, font=("Arial", 14), width=15)
        enty_contact.grid(row=0, column=1, sticky=W, padx=0)
        
        # Fetch data button
        btnfetchData = Button(lableFrameLeft, text="Fetch Data", command=self.fetch_contact, font=("Arial", 11, "bold"), bg="black", fg="gold", width=8)
        btnfetchData.place(x=410, y=2)
        
        # check_in date
        check_in_date = Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Check_in Date :", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = ttk.Entry(lableFrameLeft, textvariable=self.var_Check_in, font=("Arial", 14), width=26)
        txtcheck_in_date.grid(row=1, column=1, sticky=W)
        
        # check_out date
        lbl_Check_out = Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Check_out Date :", padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)
        txtcheck_out_date = ttk.Entry(lableFrameLeft, textvariable=self.var_Check_out, font=("Arial", 14), width=26)
        txtcheck_out_date.grid(row=2, column=1)
        
        # Room type
        lable_RoomType = Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Room Type :", padx=2, pady=6)
        lable_RoomType.grid(row=3, column=0, sticky=W)
        
        self.combo_RoomType = ttk.Combobox(lableFrameLeft, textvariable=self.var_Room_type, font=("Arial", 14), width=24, state="readonly")
        self.combo_RoomType['values'] = ('Luxury', 'Double', 'Single')
        self.combo_RoomType.current(0)
        self.combo_RoomType.grid(row=3, column=1, sticky=W)
        
        # Available Room
        lblRoomAvailable = Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Available Room :", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        self.combo_RoomNo = ttk.Combobox(lableFrameLeft, textvariable=self.var_AvailableRoom, font=("Arial", 14), width=24, state="readonly")
        self.combo_RoomNo['values'] = ('101', '102', '103', '201', '202', '203')
        self.combo_RoomNo.current(0)
        self.combo_RoomNo.grid(row=4, column=1, sticky=W)
        
        # Meal
        lblMeal = Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Meal :", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(lableFrameLeft, textvariable=self.var_Meal, font=("Arial", 14), width=26)
        txtMeal.grid(row=5, column=1)
        
        # No of Days
        lblNoOfDays = Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Number of Days :", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(lableFrameLeft, textvariable=self.var_NoOfDays, font=("Arial", 14), width=26)
        txtNoOfDays.grid(row=6, column=1)
        
        # Paid Tax
        lblPaidTax = Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Paid Tax :", padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)
        txtPaidTax = ttk.Entry(lableFrameLeft, textvariable=self.var_PaidTax, font=("Arial", 14), width=26)
        txtPaidTax.grid(row=7, column=1)
        
        # Sub Total
        lblSubTotal = Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Sub Total :", padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)
        txtSubTotal = ttk.Entry(lableFrameLeft, textvariable=self.var_SubTotal, font=("Arial", 14), width=26)
        txtSubTotal.grid(row=8, column=1)
        
        # Total cost
        lblTotalCost = Label(lableFrameLeft, font=("Arial", 15, "bold"), text="Total Cost :", padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)
        txtTotalCost = ttk.Entry(lableFrameLeft, textvariable=self.var_TotalCost, font=("Arial", 14), width=26)
        txtTotalCost.grid(row=9, column=1)
        
        # ======= bill button ============
        btnBill = Button(lableFrameLeft, text="Bill", command=self.total, font=("Arial", 18, "bold"), bg="black", fg="gold", width=15)
        btnBill.grid(row=10, column=0, padx=16, pady=15, sticky=W)
        
        # ==================== btns ==================
        btn_frame = Frame(lableFrameLeft, bd=2, relief=RIDGE)
        btn_frame.place(x=15, y=445, width=458, height=91)
        
        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnAdd.grid(row=0, column=0, padx=1)
        
        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnUpdate.grid(row=0, column=1, padx=1)
        
        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnDelete.grid(row=1, column=0, padx=2)
        
        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("Arial", 17, "bold"), bg="black", fg="gold", width=15)
        btnReset.grid(row=1, column=1, padx=2)
        
        # ============= RightSide Images ==============        
        try:
            img3 = Image.open("/home/kalilinux/Documents/V S code files/Projects_for/hotel_foxysDolphin/images/room_img2.jpg")
            img3 = img3.resize((300, 220), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)
            lilimg = Label(self.root, image=self.photoimg3, bd=0.5, relief=RIDGE)
            lilimg.place(x=900, y=65, width=280, height=220)
            
            img5 = Image.open("/home/kalilinux/Documents/V S code files/Projects_for/hotel_foxysDolphin/images/room_img1.jpg")
            img5 = img5.resize((300, 220), Image.Resampling.LANCZOS)
            self.photoimg5 = ImageTk.PhotoImage(img5)
            lilimg = Label(self.root, image=self.photoimg5, bd=0.5, relief=RIDGE)
            lilimg.place(x=1180, y=65, width=255, height=220)
            
            img4 = Image.open("/home/kalilinux/Documents/V S code files/Projects_for/hotel_foxysDolphin/images/room_img3.jpg")
            img4 = img4.resize((300, 220), Image.Resampling.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)
            lilimg = Label(self.root, image=self.photoimg4, bd=0.5, relief=RIDGE)
            lilimg.place(x=1435, y=65, width=200, height=220)
        except:
            pass
        
        # ==================== table frame search system ==================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("times new roman", 20, "bold"), padx=2)
        Table_Frame.place(x=520, y=280, width=1110, height=375)
        
        lblSearchBy = Label(Table_Frame, text="Search Ref :", font=("Arial", 15, "bold"), bg="black", fg="gold")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2, pady=2)
        
        self.search_var = StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("Arial", 15), width=20, state="readonly")
        combo_search["values"] = ("Contact Number", "Check-In Date")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2, pady=2)
        
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("Arial", 14), width=26)
        txtSearch.grid(row=0, column=2, padx=2, pady=2)
        
        btnSearch = Button(Table_Frame, text="Search", command=self.search, font=("Arial", 14, "bold"), bg="black", fg="gold", width=8)
        btnSearch.grid(row=0, column=3, padx=1)
        
        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=("Arial", 14, "bold"), bg="black", fg="gold", width=8)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        # ==================== show table frame ==================
        detail_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        detail_table.place(x=0, y=50, width=1100, height=293)

        scroll_x = ttk.Scrollbar(detail_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detail_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(detail_table, columns=("customer_contact", "Check_in", "Check_out", "Room_type", "AvailableRoom", "Meal", "NoOfDays", "PaidTax", "SubTotal", "TotalCost"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("customer_contact", text="Contact")
        self.room_table.heading("Check_in", text="Check-in")
        self.room_table.heading("Check_out", text="Check-out")
        self.room_table.heading("Room_type", text="Room Type")
        self.room_table.heading("AvailableRoom", text="Available Room")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("NoOfDays", text="No Of Days")
        self.room_table.heading("PaidTax", text="Paid Tax")
        self.room_table.heading("SubTotal", text="Sub Total")
        self.room_table.heading("TotalCost", text="Total Cost")

        self.room_table["show"] = "headings"

        self.room_table.column("customer_contact", width=100)
        self.room_table.column("Check_in", width=100)
        self.room_table.column("Check_out", width=100)
        self.room_table.column("Room_type", width=100)
        self.room_table.column("AvailableRoom", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("NoOfDays", width=100)
        self.room_table.column("PaidTax", width=100)
        self.room_table.column("SubTotal", width=100)
        self.room_table.column("TotalCost", width=100)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)
        
        # Load data on startup
        self.fetch_data()
    
    # =============== FIXED DATABASE CONNECTION ===============
    def connect_db(self):
        """Initialize database connection with proper error handling"""
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='pythonuser',
                password='mypassword',  #  CHANGE THIS TO YOUR ACTUAL PASSWORD
                database='management',
                autocommit=True  #  Auto commit changes
            )
            self.cursor = self.conn.cursor()
            print(" Database connected successfully!")
        except mysql.connector.Error as err:
            print(f" Database connection failed: {err}")
            messagebox.showerror("Database Error", f"Cannot connect to database:\n{err}\n\nFix: Run these MySQL commands:\n\nCREATE USER 'pythonuser'@'localhost' IDENTIFIED BY 'mypassword';\nGRANT ALL ON management.* TO 'pythonuser'@'localhost';\nFLUSH PRIVILEGES;")
            self.conn = None
            self.cursor = None
    
    # === add data ===
    def add_data(self):
        if self.var_contact.get() == "" or self.var_Check_in.get() == "":
            messagebox.showerror("Error", "Contact and Check-in date are mandatory!", parent=self.root)
            return
        
        if not self.conn or not self.conn.is_connected():
            messagebox.showerror("Error", "Database not connected!", parent=self.root)
            return
            
        try:
            query = """INSERT INTO room (Contact, Check_in, Check_out, Room_type, AvailableRoom, 
                      Meal, NoOfDays, PaidTax, SubTotal, TotalCost) 
                      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            values = (
                self.var_contact.get(),
                self.var_Check_in.get(),
                self.var_Check_out.get(),
                self.var_Room_type.get(),
                self.var_AvailableRoom.get(),
                self.var_Meal.get(),
                self.var_NoOfDays.get(),
                self.var_PaidTax.get(),
                self.var_SubTotal.get(),
                self.var_TotalCost.get()
            )
            self.cursor.execute(query, values)
            self.fetch_data()
            messagebox.showinfo("Success", " Customer booking added successfully!", parent=self.root)
            self.reset()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f" Add failed: {str(err)}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Something went wrong: {str(es)}", parent=self.root)
    
    # === fetch data ===
    def fetch_data(self):
        if not self.conn or not self.conn.is_connected():
            return
        try:
            self.cursor.execute("SELECT * FROM room")
            rows = self.cursor.fetchall()
            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("", END, values=i)
        except Exception as es:
            print(f"Fetch error: {es}")
    
    # === get cursor ===
    def get_cuersor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        
        self.var_contact.set(row[0])
        self.var_Check_in.set(row[1])
        self.var_Check_out.set(row[2])
        self.var_Room_type.set(row[3])
        self.var_AvailableRoom.set(row[4])
        self.var_Meal.set(row[5])
        self.var_NoOfDays.set(row[6])
        self.var_PaidTax.set(row[7])
        self.var_SubTotal.set(row[8])
        self.var_TotalCost.set(row[9])
    
    # ================== update ==================
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please select a record to update", parent=self.root)
            return
        
        if not self.conn or not self.conn.is_connected():
            messagebox.showerror("Error", "Database not connected!", parent=self.root)
            return
            
        try:
            query = """UPDATE room SET Check_in=%s, Check_out=%s, Room_type=%s, AvailableRoom=%s, 
                      Meal=%s, NoOfDays=%s, PaidTax=%s, SubTotal=%s, TotalCost=%s WHERE Contact=%s"""
            values = (
                self.var_Check_in.get(),
                self.var_Check_out.get(),
                self.var_Room_type.get(),
                self.var_AvailableRoom.get(),
                self.var_Meal.get(),
                self.var_NoOfDays.get(),
                self.var_PaidTax.get(),
                self.var_SubTotal.get(),
                self.var_TotalCost.get(),
                self.var_contact.get()
            )
            self.cursor.execute(query, values)
            self.fetch_data()
            messagebox.showinfo("Success", " Record updated successfully!", parent=self.root)
            self.reset()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f" Update failed: {str(err)}", parent=self.root)
    
    # === Delete ===
    def mDelete(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please select a record to delete", parent=self.root)
            return
        
        mDelete = messagebox.askyesno("Confirm Delete", "Do you want to delete this booking?", parent=self.root)
        if mDelete:
            if not self.conn or not self.conn.is_connected():
                messagebox.showerror("Error", "Database not connected!", parent=self.root)
                return
            try:
                query = "DELETE FROM room WHERE Contact=%s"
                self.cursor.execute(query, (self.var_contact.get(),))
                self.fetch_data()
                self.reset()
                messagebox.showinfo("Success", " Record deleted successfully!", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f" Delete failed: {str(err)}", parent=self.root)
    
    # === Reset ===
    def reset(self):
        self.var_contact.set("")
        self.var_Check_in.set("")
        self.var_Check_out.set("")
        self.var_Room_type.set("Luxury")
        self.var_AvailableRoom.set("101")
        self.var_Meal.set("")
        self.var_NoOfDays.set("")
        self.var_PaidTax.set("")
        self.var_SubTotal.set("")
        self.var_TotalCost.set("")
    
    # ================ Fetch customer data ==============
    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
            return
        if not self.conn or not self.conn.is_connected():
            messagebox.showerror("Error", "Database not connected!", parent=self.root)
            return
        try:
            query = "SELECT name FROM customer WHERE mobile=%s"
            self.cursor.execute(query, (self.var_contact.get(),))
            row = self.cursor.fetchone()
            
            if row is None:
                messagebox.showerror("Not Found", " This contact number not found!", parent=self.root)
            else:
                messagebox.showinfo("Success", f" Customer Found: {row[0]}", parent=self.root)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f" Database error: {str(err)}", parent=self.root)
    
    # search system
    def search(self):
        if self.txt_search.get() == "":
            messagebox.showerror("Error", "Please enter search term", parent=self.root)
            return
        if not self.conn or not self.conn.is_connected():
            messagebox.showerror("Error", "Database not connected!", parent=self.root)
            return
        try:
            search_by = self.search_var.get()
            search_text = self.txt_search.get()
            
            if search_by == "Contact Number":
                query = "SELECT * FROM room WHERE Contact LIKE %s"
            else:
                query = "SELECT * FROM room WHERE Check_in LIKE %s OR Check_out LIKE %s"
            
            self.cursor.execute(query, ('%' + search_text + '%',))
            rows = self.cursor.fetchall()
            
            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("", END, values=i)
            else:
                self.fetch_data()  # Show all if no results
                messagebox.showinfo("No Results", "No matching records found")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f" Search failed: {str(err)}", parent=self.root)
    
    # ========== billing section =========
    def total(self):
        if self.var_Check_in.get() == "" or self.var_Check_out.get() == "":
            messagebox.showerror("Error", "Please enter Check-in and Check-out dates (dd/mm/yyyy)", parent=self.root)
            return
        
        try:
            inDate = datetime.strptime(self.var_Check_in.get(), "%d/%m/%Y")
            outDate = datetime.strptime(self.var_Check_out.get(), "%d/%m/%Y")
            days = abs((outDate - inDate).days)
            if days == 0:
                days = 1
            self.var_NoOfDays.set(str(days))
        except:
            messagebox.showerror("Error", "Please enter valid dates (dd/mm/yyyy)", parent=self.root)
            return
        
        meal = self.var_Meal.get()
        room_type = self.var_Room_type.get()
        
        if meal == "" or room_type == "":
            messagebox.showerror("Error", "Please enter Meal and select Room Type", parent=self.root)
            return
        
        # Pricing logic
        meal_price = 0
        if meal == "Breakfast":
            meal_price = 600
        elif meal == "Lunch":
            meal_price = 1000
        elif meal == "Dinner":
            meal_price = 1000
        
        if room_type == "Luxury":
            room_price = 12000
        elif room_type == "Double":
            room_price = 8000
        elif room_type == "Single":
            room_price = 4000
        
        subtotal = (meal_price + room_price) * days
        tax = subtotal * 0.1
        total = subtotal + tax
        
        self.var_PaidTax.set(f"Rs. {tax:.2f}")
        self.var_SubTotal.set(f"Rs. {subtotal:.2f}")
        self.var_TotalCost.set(f"Rs. {total:.2f}")

if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
