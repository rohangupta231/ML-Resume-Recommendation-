from tkinter import *
from tkinter import filedialog,scrolledtext
from tkinter.ttk import *
import PyPDF2
from docx import Document
import pandas as pd
import alpha
import test
root = Tk()
root.geometry=('450x600')
root.title('Job Description')
frame = Frame(root)
temp=0
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

global var1
temp=0


def clicked():
    file=filedialog.askopenfilename(parent=root,title='Job Description',filetypes=(("Text File","*.docx"),("All Files","*.*"),("pdf File","*.pdf*")))
    print(file)
    if '.pdf' in file:
        print('pdf file')
        pdfFileObj = open(file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        contents = pageObj.extractText()
        contents = pageObj.extractText()
        textArea.insert('1.0',contents)


    elif '.docx' in file:
        print('.docx file')
        document = Document(file)
        contents = document.paragraphs
        for i in contents:
            textArea.insert('1.0',i.text)

    else:
        print('other')
        f=open(file,'r')
        contents=f.read()
        textArea.insert('1.0',contents)
        f.close()


def click():
    global var1
    data=textArea.get('1.0',END+ '-1c')
    job_description = 'job_description.txt'
    f = open(job_description, "w")
    f.write(data)
    f.close()
    print(data)
    lbl = Label(frame, text="Data uploaded")
    lbl.grid(column=1, row=4,sticky=E)
    var1 = alpha.recommend(job_description,"skills.csv",1)
    print(len(var1))

def next():
    global textArea1
    global var2
    textArea1.delete('1.0',END)
    global temp
    if(temp!=count):

        temp=temp+1

        textArea1.insert('1.0','\nMatched skills : '+ str(var2[temp][2]))
        textArea1.insert('1.0','\nPercentage matched : '+ str(var2[temp][1]))
        textArea1.insert('1.0','\nName : '+ str(var2[temp][0]))
        textArea1.insert('1.0','\nResume : '+ str(temp+1))

def previous():
    global textArea1
    global var2
    global window
    textArea1.delete('1.0',END)
    global temp
    if(temp>0):
        temp = temp-1
        textArea1.insert('1.0','\nMatched skills : '+ str(var2[temp][2]))
        textArea1.insert('1.0','\nPercentage matched : '+ str(var2[temp][1]))
        textArea1.insert('1.0','\nName : '+ str(var2[temp][0]))
        textArea1.insert('1.0','\nResume : '+ str(temp+1))


def recommend():
    global var1
    global var2
    global window
    global count
    global temp
    count =0
    var2 = []
    temp=0


    window = Toplevel(root)
    window.title("Recommended Resumes")
    window.geometry=('450x400')
    k=float(e1.get())
    print("K////////////////////////////",k)
    Label(window, text=" Resumes recommended ").pack(side=TOP)
    global textArea1
    textArea1=scrolledtext.ScrolledText(window,width=70,height=40)
    textArea1.pack(padx=5, pady=10,side=LEFT)
    Button(window,text=" Previous  ",command=previous).pack(padx=5, pady=10,side=LEFT)
    Button(window,text=" Next  ",command=next).pack(padx=5, pady=10,side=LEFT)
    Button(window,text=" TTS  ").pack(padx=5, pady=10,side=LEFT)


    for i in range(len(var1)):
        if var1['perc_match'][i] >= k:
            # var2.append(var1[i])
            var2.append([var1['filename'][i],var1['perc_match'][i],var1['mathced_skills'][i]])
            count+=1
    for i in var2:
        print(i)
    textArea1.insert('1.0','\nMatched skills : '+ str(var2[temp][2]))
    textArea1.insert('1.0','\nPercentage matched : '+ str(var2[temp][1]))
    textArea1.insert('1.0','\nName : '+ str(var2[temp][0]))
    textArea1.insert('1.0','\nResume : '+ str(temp+1))
    Label(window, text="Total number of resumes found: "+str(count)).pack(side=TOP)

    window.mainloop()

def select():
	global folder
	global window1
	folder=filedialog.askdirectory()
	Label(window1, text="Folder Selected").grid(row=4,column=0,sticky=W)


def done():
    global folder,value
    global window1
    global temp
    value=v.get()
    print("value/////////////////////////",value)
    print("Folder////////////////////////",folder)
    test.csvMod(folder,value,'skills.csv')
    window1.destroy()
    root.deiconify()



def upload():
	root.withdraw()
	global window1
	global v
	global value
	print('temp',temp)


	window1=Toplevel(root)
	window1.title("Upload Resumes")
	window1.geometry=('300x400')

	v = IntVar()
	print("V/////////////////////////////",v)
	Label(window1, text="UPLOAD RESUMES").grid(row=0,column=1,sticky=W)
	Label(window1, text="Select folder from PC :").grid(row=1,column=0,sticky=W)
	Button(window1,text=" Choose folder  ",command=select).grid(row=1,column=1,sticky=W)
	Label(window1, text="Choose: ").grid(row=5,column=0,sticky=W)
	r1 = Radiobutton(window1, text="Create New", variable=v, value=1)
	r1.grid(row=5,column=1,sticky=W)
	r2 = Radiobutton(window1, text="Append", variable=v,value=2)
	r2.grid(row=5,column=2,sticky=W)
	Button(window1,text=" Done ",command=done).grid(row=6,column=1)
	window1.mainloop()


Label(frame, text="JOB DESCRIPTION").grid(row=0,column=1,sticky=W)
Button(frame, text="Upload your own resumes",command=upload).grid(row=0,column=2,sticky=W)
Label(frame, text="Select File from PC :").grid(row=1,column=0,sticky=W)
Button(frame,text=" Choose file  ",command=clicked).grid(row=1,column=1,sticky=W)
Label(frame, text=" OR Enter job decription").grid(row=3,column=0,sticky=W)
textArea=scrolledtext.ScrolledText(frame,width=40,height=10)
textArea.grid(row=3,column=1,sticky=W)
Button(frame,text=" Done ",command=click).grid(row=4,column=1)
Label(frame, text=" Enter % match of resumes you want:").grid(row=6,column=0,sticky=W)
e1=Entry(frame)
e1.grid(row=6,column=1,sticky=W)
Button(frame,text=" Recommend Resume ",command=recommend).grid(columnspan=3)
frame.pack()
root.mainloop()
