from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Logoutdetails:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Details")
        self.root.geometry("1640x670+500+420")
        
        
        
        
if __name__ ==  "__main__":
    root=Tk()
    obj= Logoutdetails(root)
    root.mainloop()