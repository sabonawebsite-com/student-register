from tkinter import*
root=Tk()
root.title("Bru")
root.geometry("400x400")
label=Label(root,text="Full Name")
label.grid(row=0,column=0)
entry=Entry(root)
entry.grid(row=0,column=1)
label1=Label(root,text="Id Number")
label1.grid(row=1,column=0)
entry1=Entry(root)
entry1.grid(row=1,column=1)
label2=Label(root,text="Nationality")
label2.grid(row=2,column=0)
entry2=Entry(root)
entry2.grid(row=2,column=1)
label3=Label(root,text="Region")
label3.grid(row=3,column=0)
entry3=Entry(root)
entry3.grid(row=3,column=1)
label4=Label(root,text="Zone")
label4.grid(row=4,column=0)
entry4=Entry(root)
entry4.grid(row=4,column=1)
label5=Label(root,text="Phone Number")
label5.grid(row=5,column=0)
entry5=Entry(root)
entry5.grid(row=5,column=1)
label6=Label(root,text="Stream Natural Science")
label6.grid(row=6,column=0)
label7=Label(root,text="Academic Year")
label7.grid(row=7,column=0)

label8=Label(root,text="Sex")
checkbox=Checkbutton(root,text="male")
checkbox.grid(row=8,column=0)
checkbox1=Checkbutton(root,text="fiemale")
checkbox1.grid(row=8,column=1)
label9=Label(root,text="Class Year")
label9.grid(row=9,column=0)
checkbox2=Checkbutton(root,text="1st year") 
checkbox2.grid(row=10,column=0)
checkbox3=Checkbutton(root,text="2nd year")
checkbox3.grid(row=10,column=1)
checkbox4=Checkbutton(root,text="3rd year")
checkbox4.grid(row=10,column=2)
checkbox5=Checkbutton(root,text="4th year")
checkbox5.grid(row=10,column=3)
label10=Label(root,text="Program")
label10.grid(row=11,column=0)
checkbox6=Checkbutton(root,text="remedial")
checkbox6.grid(row=12,column=0)
checkbox7=Checkbutton(root,text="undergraduate")
checkbox7.grid(row=12,column=1)
checkbox8=Checkbutton(root,text="postgraduate")
checkbox8.grid(row=12,column=2)
label11=Label(root,text="Semiester")
label11.grid(row=13,column=0)
checkbox9=Checkbutton(root,text="1st")
checkbox9.grid(row=14,column=0)
checkbox10=Checkbutton(root,text="2nd")
checkbox10.grid(row=14,column=1)
checkbox11=Checkbutton(root,text="3rd")
checkbox11.grid(row=14,column=2)
label12=Label(root,text="Academic Type")
label12.grid(row=15,column=0)
checkbox12=Checkbutton(root,text="Regular")
checkbox12.grid(row=16,column=0)
checkbox13=Checkbutton(root,text="Weekend")
checkbox13.grid(row=16,column=1)
checkbox14=Checkbutton(root,text="summer")
checkbox14.grid(row=16,column=2)

root.mainloop()
