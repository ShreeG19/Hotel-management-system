from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom
from tkinter import messagebox  # ✅ FIXED: Added messagebox import
from logout import Logoutdetails

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospitality System")
        self.root.geometry("1913x1500+0+0")

        #  ======================img1 ======================
        try:  # ✅ FIXED: Added try-except for images
            img1 = Image.open("/home/kalilinux/Documents/V S code files/Projects_for/hotel_foxysDolphin/images/img1.jpg")
            img1 = img1.resize((1913, 300), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)
            lilimg = Label(self.root, image = self.photoimg1, bd=4, relief = RIDGE)
            lilimg.place(x=0, y=0, width=1913, height=250)
        except:
            pass
        
        #  ======================logo ======================
        try:
            img2 = Image.open("/home/kalilinux/Documents/V S code files/Projects_for/hotel_foxysDolphin/images/logo.png")
            img2 = img2.resize((270, 250), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            lilimg = Label(self.root, image = self.photoimg2, bd=4, relief = RIDGE)
            lilimg.place(x=0, y=0, width=270, height=250)
        except:
            pass
        
        #  ==================== title ====================
        lbl_title = Label(self.root,text="Hotel Foxy's Dolphin",font=("times new roman", 40, "bold"),bg="black",fg="gold",bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=250, width=1913, height=60)
        
        #  ==================== main frame ====================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0, y=310, width=1913, height=720)

        #  ==================== menu ====================
        lbl_menu = Label(main_frame,text="MENU",font=("times new roman", 20, "bold"),bg="black",fg="gold",bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=270)
        
        #  ==================== btn frame ====================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0, y=40, width=310, height=225)
        
        cust_btn=Button(btn_frame,text="CUSTOMER", command=self.Cust_details, width=24 ,font=("times new roman", 14, "bold"),bg="black",fg="gold",bd=4, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)
        
        room_btn=Button(btn_frame,text="ROOM", command=self.roombooking, width=24 ,font=("times new roman", 14, "bold"),bg="black",fg="gold",bd=4, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)
        
        details_btn=Button(btn_frame,text="DETAILS", command=self.detailsRoom, width=24 ,font=("times new roman", 14, "bold"),bg="black",fg="gold",bd=4, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)
        
        dining_btn=Button(btn_frame,text="DINING AREA", width=24 ,font=("times new roman", 14, "bold"),bg="black",fg="gold",bd=4, cursor="hand2")
        dining_btn.grid(row=3, column=0, pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT", command=self.Logout, width=24 ,font=("times new roman", 14, "bold"),bg="black",fg="gold",bd=4, cursor="hand2")  # ✅ FIXED: Added command
        logout_btn.grid(row=4, column=0, pady=1)       
        
        #  ==================== right side image ====================     
        try:
            img3 = Image.open("/home/kalilinux/Documents/V S code files/Projects_for/hotel_foxysDolphin/images/img3.jpg")
            img3 = img3.resize((1650, 700), Image.Resampling.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)
            lilimg1 = Label(main_frame, image = self.photoimg3, bd=4, relief = RIDGE)
            lilimg1.place(x=255, y=0, width=1650, height=700)
        except:
            pass
        
        #  ==================== bottom image ====================     
        try:
            img4 = Image.open("/home/kalilinux/Documents/V S code files/Projects_for/hotel_foxysDolphin/images/img4.jpg")
            img4 = img4.resize((255, 220), Image.Resampling.LANCZOS)
            self.photoimg4 = ImageTk.PhotoImage(img4)
            lilimg1 = Label(main_frame, image = self.photoimg4, bd=4, relief = RIDGE)
            lilimg1.place(x=0, y=265, width=255, height=220)
        except:
            pass
        
        try:
            img5 = Image.open("/home/kalilinux/Documents/V S code files/Projects_for/hotel_foxysDolphin/images/img5.jpg")
            img5 = img5.resize((255, 220), Image.Resampling.LANCZOS)
            self.photoimg5 = ImageTk.PhotoImage(img5)
            lilimg1 = Label(main_frame, image = self.photoimg5, bd=4, relief = RIDGE)
            lilimg1.place(x=0, y=480, width=255, height=220)
        except:
            pass
        
    def Cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)    

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
        
    def detailsRoom(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)
    
    def DiningArea(self):
        self.new_window=Toplevel(self.root)
        self.app=DiningArea(self.new_window)
        
    def Logout(self):  # ✅ FIXED: Added missing Logout method
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.root.destroy()

if __name__ ==  "__main__":
    root=Tk()
    obj= HotelManagementSystem(root)
    root.mainloop()