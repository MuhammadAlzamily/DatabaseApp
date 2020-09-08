from tkinter import * 
from tkinter import ttk
import tkinter
import sqlite3
def connecting():
	conn = sqlite3.connect("customers.db")
	c = conn.cursor()
	sql = """
		CREATE TABLE IF NOT EXISTS customers(

			first_name text,
			last_name text,
			email text,
			country text,
			phone_number integer


		)

	"""
	c.execute(sql)
	conn.commit()
	c.close()

connecting()


def show_customers():
	conn = sqlite3.connect("Customers.db")
	c = conn.cursor()
	c.execute("SELECT * FROM customers")
	rows = c.fetchall()
	for row in rows:
		tr.insert("",tkinter.END,values=row)
	conn.commit()
	conn.close()

def add_to_db():
	global fname_box,lname_box,email_box,country_box,phone_box
	conn = sqlite3.connect("Customers.db")
	c = conn.cursor()
	fname = fname_box.get()
	lname = lname_box.get()
	email = email_box.get()
	country = country_box.get()
	phone = phone_box.get()


	sql = """

		INSERT INTO customers(first_name,last_name,email,country,phone_number)VALUES(?,?,?,?,?)

	"""
	vals = (fname,lname,email,country, phone)
	c.execute(sql,vals)
	conn.commit()
	c.close()
	fname_box.delete(0,END)
	lname_box.delete(0,END)
	email_box.delete(0,END)
	country_box.delete(0,END)
	phone_box.delete(0,END)




root = Tk()
root.title("Database App")
root.geometry("1000x700")


#LABELS AND ENTRIES

frame1 = LabelFrame(root,text="Adding Users")
frame1.pack(fill="both")
fname_label = Label(frame1,text="First Name")
fname_label.grid(row=0,column=0,padx=15)
fname_box = ttk.Entry(frame1)
fname_box.grid(row=0,column=1,padx=20)
lname_label = Label(frame1,text="Last Name")
lname_label.grid(row=1,column=0,padx=15)
lname_box = ttk.Entry(frame1)
lname_box.grid(row=1,column=1,padx=20,pady=20)
email_label = Label(frame1,text="Email Address")
email_label.grid(row=2,column=0,padx=15)
email_box = ttk.Entry(frame1)
email_box.grid(row=2,column=1,padx=20)
country_label = Label(frame1,text="Country")
country_label.grid(row=3, column=0,padx=15)
country_box = ttk.Entry(frame1)
country_box.grid(row=3,column=1,pady=20)
phone_label = Label(frame1,text="Phone Number")
phone_label.grid(row=4,column=0,padx=15)
phone_box = ttk.Entry(frame1)
phone_box.grid(row=4,column=1)
add_btn = Button(frame1,text="Add",relief='flat',width=15,bg='green',fg='white',command=add_to_db)
view_btn = Button(frame1,text="View",relief='flat',width=15,bg='blue',fg='white',command=show_customers)
add_btn.grid(row=5,column=0,pady=15,padx=15)
view_btn.grid(row=5,column=1)

frame2 = LabelFrame(root,text="Customers Data")
frame2.pack()
tr = ttk.Treeview(frame2,column=('First Name,','Last Name','Email','Country','Phone Number'),show='headings')
tr.heading("#1", text="First Name")
tr.heading("#2", text="Last Name")
tr.heading("#3", text="Email")
tr.heading("#4",text="Country")
tr.heading("#5",text="Phone Number")
tr.pack(fill="both")

root.mainloop()