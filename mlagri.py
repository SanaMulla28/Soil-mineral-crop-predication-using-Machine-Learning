
from tkinter import *
import csv
import Rabi
import kharif
import Summer
window=Tk()
#<img src="argi.jpg" width="200px" height="200px" img src="C:/Users/LENOVO/Downloads/agri.jpg"> 
window.title("Prediction")
window.geometry("480x480")
#window.config(bg='Lightgreen')
#bg = PhotoImage(file = "C:/Users/LENOVO/Downloads/argi/agri.png") 
#Label = Label(window, image=bg)
#Label.place(x=0,y=0) 
lb=Label(window, text='')
lb.place(relx=0.4, rely=0.5, anchor=CENTER)
def moist():
    Label(window, text="season").place(relx=0.6, rely=0.7, anchor=CENTER)
def ident():
    
    Label(w1, text='welcome').pack()
def values():
    global lbl
    #lbl=Label(window, text="Analyzing....")
    #lbl.pack()
    global n,p,k
    n=en.get()
    p=ep.get()
    k=ek.get()
    print(n,p,k)
    r=csv.reader(open("../inputs/test.csv"))
    lines=list(r)
    print(lines)
    lines[1]=[n,p,k]
    with open ("../inputs/test.csv",'w',newline='') as writeFile:
            wr=csv.writer(writeFile)
            wr.writerows(lines)
    r=csv.reader(open("../inputs/test.csv"))
    lines=list(r)
    print(lines)
    try:
        if(season==1):
            re=kharif.main()
            print(re)
            global lb
            lb.configure(text=re)
        elif(season==2):
            re=Rabi.main()
            lb.configure(text=re)
            print(re)
        elif(season==3):
            re=Summer.main()
            lb.configure(text=re)
            print(re)
    except:
        lb.config(text="Please select the season").place(relx=0.4, rely=0.5, anchor=CENTER)
    
    #if __name__ == "__main__":
        #main()
def val():
        global season
        season=var.get()
        print(season)


  
# Add image file
     
Label(window, text="NORTHERN DRY AGRO-CLIMATIC ZONE OF KARANATAKA", font='ARIALBLACK').place(relx=0.015, anchor=NW)
window.geometry("400x400")

# Display image
Label(window, text="PREDICTION OF CROP", font='Helveica 20 bold').grid(row=0, column=5,padx=25,pady=25)
Label(window, text="").grid(row=0, column=0)
Label(window, text="").grid(row=1, column=0)
Label(window, text="").grid(row=2, column=0)
Label(window, text="NUTRIENT VALUES").grid(row=3, column=0)
Label(window, text="SEASONS").grid(row=3, column=3)
var = IntVar()
R1 = Radiobutton(window, text="Monsoon", variable=var, value=1,command=val, indicatoron=0, width=8)
R1.grid(row=4, column=3)
R2 = Radiobutton(window, text="  Rainy  ", variable=var, value=2,command=val, indicatoron=0, width=8)
R2.grid(row=5, column=3)
R3 = Radiobutton(window, text=" Summer ", variable=var, value=3,command=val,indicatoron=0,width=8)
R3.grid(row=6, column=3)
Label(window, text="Enter the value of N").grid(row=4, column=0)
en=Entry(window, width=15)
en.grid(row=4, column=1)
Label(window, text="Enter the value of P").grid(row=5, column=0)
ep=Entry(window, width=15)
ep.grid(row=5, column=1)
Label(window, text="Enter the value of K").grid(row=6, column=0)
ek=Entry(window, width=15)
ek.grid(row=6, column=1)
btn=Button(window, text="Enter", command=values, width=10).grid(row=7, column=2)
window.mainloop()


# In[ ]:




