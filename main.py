import tkinter
from tkinter import *
from tkinter import ttk
import pandas as pd
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# verisetini tanımlama
df = pd.read_csv("rows.csv", dtype={"Date received": object, "Product": object, "Sub-product": object, "Issue": object,
                                    "Sub-issue": object, "Consumer complaint narrative": object,
                                    "Company public response": object, "Company": object, "State": object,
                                    "ZIP code": object, "Tags": object, "Consumer consent provided?": object,
                                    "Submitted via": object, "Date sent to company": object,
                                    "Company response to consumer": object, "Timely response?": object,
                                    "Consumer disputed?": object, "Complaint ID": int, "dtype": object})
# Sütun düzenleme
df = df.drop(
    ['Date received', 'Sub-product', 'Sub-issue', 'Consumer complaint narrative', "Company public response", "Tags",
     "Consumer consent provided?", "Date sent to company", "Submitted via", "Company response to consumer",
     "Timely response?", "Consumer disputed?"], axis=1)

# Noktalama kaldırma
df['Product'] = df['Product'].str.replace(r'[^\w\s]+', '', regex=True)
df['Issue'] = df['Issue'].str.replace(r'[^\w\s]+', '', regex=True)
df['Company'] = df['Company'].str.replace(r'[^\w\s]+', '', regex=True)
df['State'] = df['State'].str.replace(r'[^\w\s]+', '', regex=True)
df['ZIP code'] = df['ZIP code'].str.replace(r'[^\w\s]+', '', regex=True)

# stopword kaldırma
stop = set(stopwords.words('english'))

df['NewProduct'] = df['Product'].str.lower().str.split()
df['NewProduct'] = df['NewProduct'].apply(lambda x: " ".join([item for item in x if item not in stop]))
df['NewIssue'] = df['Issue'].str.lower().str.split()
df['NewIssue'] = df['NewIssue'].apply(lambda x: " ".join([item for item in x if item not in stop]))
df['NewCompany'] = df['Company'].str.lower().str.split()
df['NewCompany'] = df['NewCompany'].apply(lambda x: " ".join([item for item in x if item not in stop]))

# Stopword içeren eski sütünları kaldırma
df.drop('Issue', inplace=True, axis=1)
df.drop('Product', inplace=True, axis=1)
df.drop('Company', inplace=True, axis=1)

# Null değer kaldıma
df.dropna(inplace=True)


cumlo = []
benzerlo = []
cumlolo=[]

cumlop=[]
cumlolop=[]
benzerlop=[]

# Issueler arası benzerlik hesabı
def Issuebenzo():
    k = 0
    p = 0
    for i in df['NewIssue'].head(250):
        p += 1
        for j in df['NewIssue'].head(10000):
            k += 1
            c = 0
            for s in range(len(str(j).split())):
                for a in range(len(str(i).split())):
                    if str(j).split()[s] == str(i).split()[a]:
                        c += 1
                        break
            if len(str(j).split()) > len(str(i).split()):
                print(str(p) + "ile" + str(k) + " benzerlik =" + "%" + str(100 * (c / len(str(j).split()))))
                print("cümleler=" + str(j) + "////" + str(i))
                cumlo.append(str(p) + "ile" + str(k))
                cumlolo.append(str(j) + "////" + str(i))
                benzerlo.append(100 * (c / len(str(j).split())))
            elif len(str(i).split()) > len(str(j).split()):
                print(str(p) + "ile" + str(k) + " benzerlik =" + "%" + str(100 * (c / len(str(i).split()))))
                print("cümleler=" + str(j) + "////" + str(i))
                cumlo.append(str(p) + "ile" + str(k))
                cumlolo.append(str(j) + "////" + str(i))
                benzerlo.append(100 * (c / len(str(i).split())))

            else:
                print(str(p) + "ile" + str(k) + " benzerlik =" + "%" + str(100 * (c / len(str(j).split()))))
                print("cümleler=" + str(j) + "////" + str(i))
                cumlo.append(str(p) + "ile" + str(k))
                cumlolo.append(str(j) + "////" + str(i))
                benzerlo.append(100 * (c / len(str(j).split())))

        k = 0


Issuebenzo()

# Productlar arası benzerlik hesabı
def productbenzo():
    l = 0
    m = 0

    for i in df['NewProduct'].head(250):
        m += 1
        for j in df['NewProduct'].head(10000):
            l += 1
            d = 0
            for s in range(len(str(j).split())):
                for a in range(len(str(i).split())):
                    if str(j).split()[s] == str(i).split()[a]:
                        d += 1
                        break
            if len(str(j).split()) > len(str(i).split()):
                print(str(m) + "ile" + str(l) + " benzerlik =" + "%" + str(100 * (d / len(str(j).split()))))
                print("cümleler=" + str(j) + "////" + str(i))
                cumlop.append(str(m) + "ile" + str(l))
                cumlolop.append(str(j) + "////" + str(i))
                benzerlop.append(100 * (d / len(str(j).split())))
            elif len(str(i).split()) > len(str(j).split()):
                print(str(m) + "ile" + str(l) + " benzerlik =" + "%" + str(100 * (d / len(str(i).split()))))
                print("cümleler=" + str(j) + "////" + str(i))
                cumlop.append(str(m) + "ile" + str(l))
                cumlolop.append(str(j) + "////" + str(i))
                benzerlop.append(100 * (d / len(str(i).split())))
            else:
                print(str(m) + "ile" + str(l) + " benzerlik =" + "%" + str(100 * (d / len(str(j).split()))))
                print("cümleler=" + str(j) + "////" + str(i))
                cumlop.append(str(m) + "ile" + str(l))
                cumlolop.append(str(j) + "////" + str(i))
                benzerlop.append(100 * (d / len(str(j).split())))
        l = 0


productbenzo()

benzerlo1=[]
cumlo1=[]
cumlolo1=[]

benzerlo2=[]
cumlo2=[]
cumlolo2=[]

benzerlo3=[]
cumlo3=[]
cumlolo3=[]

benzerlo4=[]
cumlo4=[]
cumlolo4=[]

#Issuelerde Benzerlik aralıklarına göre ayrıştırma
def benzogetir():
    for i in range(len(cumlo)):
        if benzerlo[i] >= 0 and benzerlo[i]<= 25:
            benzerlo1.append(benzerlo[i])
            cumlo1.append(cumlo[i])
            cumlolo1.append(cumlolo[i])
        elif benzerlo[i] >= 25 and benzerlo[i]<= 50:
            benzerlo2.append(benzerlo[i])
            cumlo2.append(cumlo[i])
            cumlolo2.append(cumlolo[i])
        elif benzerlo[i] >= 50 and benzerlo[i] <= 75:
            benzerlo3.append(benzerlo[i])
            cumlo3.append(cumlo[i])
            cumlolo3.append(cumlolo[i])
        elif benzerlo[i] >= 75 and benzerlo[i] <= 100:
            benzerlo4.append(benzerlo[i])
            cumlo4.append(cumlo[i])
            cumlolo4.append(cumlolo[i])

benzogetir()

benzerlop1=[]
cumlop1=[]
cumlolop1=[]

benzerlop2=[]
cumlop2=[]
cumlolop2=[]

benzerlop3=[]
cumlop3=[]
cumlolop3=[]

benzerlop4=[]
cumlop4=[]
cumlolop4=[]

#Productlarda Benzerlik aralıklarına göre ayrıştırma

def benzopgetir():
    for i in range(len(cumlop)):
        if benzerlop[i] >= 0 and benzerlop[i]<= 25:
            benzerlop1.append(benzerlop[i])
            cumlop1.append(cumlop[i])
            cumlolop1.append(cumlolop[i])
        elif benzerlop[i] >= 25 and benzerlop[i]<= 50:
            benzerlop2.append(benzerlop[i])
            cumlop2.append(cumlop[i])
            cumlolop2.append(cumlolop[i])
        elif benzerlop[i] >= 50 and benzerlop[i] <= 75:
            benzerlop3.append(benzerlop[i])
            cumlop3.append(cumlop[i])
            cumlolop3.append(cumlolop[i])
        elif benzerlop[i] >= 75 and benzerlop[i] <= 100:
            benzerlop4.append(benzerlop[i])
            cumlop4.append(cumlop[i])
            cumlolop4.append(cumlolop[i])

benzopgetir()

print(df.info())
#tkinter kodları
tk = Tk()
tk.title("Yazlab1.2")
tk.geometry("600x450")
tk.configure(bg='#ffa3cf')
name = Label(tk, text="Product Giriniz:", fg="#000000").grid(row=0, column=0)
e1 = Entry(tk).grid(row=0, column=1)
Aname = Label(tk, text="Issue Giriniz:", fg="#000000").grid(row=2, column=0)
e2 = Entry(tk).grid(row=2, column=1)
Bname = Label(tk, text="Company Giriniz:", fg="#000000").grid(row=3, column=0)
e5 = Entry(tk).grid(row=3, column=1)
Cname = Label(tk, text="State Giriniz:", fg="#000000").grid(row=4, column=0)
e3 = Entry(tk).grid(row=4, column=1)
Dname = Label(tk, text="ZIP code Giriniz:", fg="#000000").grid(row=5, column=0)
e4 = Entry(tk).grid(row=5, column=1)

labelTop = tkinter.Label(tk,
                         text="Karşılaştırma yapmak istediğiniz sütunu seçiniz.")
labelTop.grid(column=0, row=7)

comboExample = ttk.Combobox(tk,
                            values=[
                                "Seçiniz",
                                "Product",
                                "Issue",
                                "Company",
                                "State",
                                "ZIP code",
                                "Complaint ID"])
print(dict(comboExample))
comboExample.grid(column=1, row=7)
comboExample.current(0)
print(comboExample.current(), comboExample.get())
print(comboExample.current(), comboExample.get())
kname = Label(tk, text="Benzerlik oranı Giriniz:", fg="#000000").grid(row=6, column=0)
e6 = Entry(tk).grid(row=6, column=1)
t1 = tkinter.Text(height=100, width=125,bg="purple",fg="white")
t1.grid(row=13,column=0)

#Issueları yazdırma
def getir():
 t1.delete(0.0,tkinter.END)
 for i in range(len(cumlo1)):
  t1.insert(tkinter.END,"\n"+cumlo1[i]+" benzerlik="+str(benzerlo1[i])+"Issues:"+cumlolo1[i])
def getir2():
 t1.delete(0.0,tkinter.END)
 for i in range(len(cumlo2)):
  t1.insert(tkinter.END,"\n"+cumlo2[i]+" benzerlik="+str(benzerlo2[i])+"Issues:"+cumlolo2[i])
def getir3():
 t1.delete(0.0,tkinter.END)
 for i in range(len(cumlo3)):
  t1.insert(tkinter.END,"\n"+cumlo3[i]+" benzerlik="+str(benzerlo3[i])+"Issues:"+cumlolo3[i])
def getir4():
 t1.delete(0.0,tkinter.END)
 for i in range(len(cumlo4)):
  t1.insert(tkinter.END,"\n"+cumlo4[i]+" benzerlik="+str(benzerlo4[i])+"Issues:"+cumlolo4[i])
secname = Label(tk, text="Issue:", fg="#000000").grid(row=8, column=1)
submit = Button(tk, text="%0-%25", fg="#000000", activebackground="purple", activeforeground="white",command=getir).grid(row=8, column=2)
submit2 = Button(tk, text="%25-%50", fg="#000000", activebackground="purple", activeforeground="white",command=getir2).grid(row=8, column=3)
submit3 = Button(tk, text="%50-%75", fg="#000000", activebackground="purple", activeforeground="white",command=getir3).grid(row=8, column=4)
submit4 = Button(tk, text="%75-%100", fg="#000000", activebackground="purple", activeforeground="white",command=getir4).grid(row=8, column=5)

#Productları yazdırma
def getirp():
 t1.delete(0.0,tkinter.END)
 for i in range(len(cumlop1)):
  t1.insert(tkinter.END,"\n"+cumlop1[i]+" benzerlik="+str(benzerlop1[i])+"Products:"+cumlolop1[i])
def getirp2():
 t1.delete(0.0,tkinter.END)
 for i in range(len(cumlop2)):
  t1.insert(tkinter.END,"\n"+cumlop2[i]+" benzerlik="+str(benzerlop2[i])+"Products:"+cumlolop2[i])
def getirp3():
 t1.delete(0.0,tkinter.END)
 for i in range(len(cumlop3)):
  t1.insert(tkinter.END,"\n"+cumlop3[i]+" benzerlik="+str(benzerlop3[i])+"Products:"+cumlolop3[i])
def getirp4():
 t1.delete(0.0,tkinter.END)
 for i in range(len(cumlop4)):
  t1.insert(tkinter.END,"\n"+cumlop4[i]+" benzerlik="+str(benzerlop4[i])+"Products:"+cumlolop4[i])
secnamep = Label(tk, text="Product:", fg="#000000").grid(row=9, column=1)
submitp = Button(tk, text="%0-%25", fg="#000000", activebackground="purple", activeforeground="white",command=getirp).grid(row=9, column=2)
submitp2 = Button(tk, text="%25-%50", fg="#000000", activebackground="purple", activeforeground="white",command=getirp2).grid(row=9, column=3)
submitp3 = Button(tk, text="%50-%75", fg="#000000", activebackground="purple", activeforeground="white",command=getirp3).grid(row=9, column=4)
submitp4 = Button(tk, text="%75-%100", fg="#000000", activebackground="purple", activeforeground="white",command=getirp4).grid(row=9, column=5)

tk.mainloop()
