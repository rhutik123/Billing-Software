from tkinter import *
from tkinter import messagebox
import os
import random
class bill_app():
    def __init__(self, root):
        self.root=root
        self.root.title("Billing system")
        self.root.geometry("1366x768+0+0")
        bg_color = "#074463"
        title = Label(self.root, text = "Bill Software", bd=10, bg=bg_color, fg="white", relief=GROOVE, font=("monospace", 30, "bold")).pack(fill=X)

        #### variables #############################

        ##### cosmatics ##################
        self.soap = IntVar()
        self.face_creame = IntVar()
        self.face_wash = IntVar()
        self.hair_spray = IntVar()
        self.hair_gel = IntVar()
        self.lotion = IntVar()
        
        ##### grocery ##################
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        
        ##### cold drinks ##################
        self.maza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.thumps_up = IntVar()
        self.limca = IntVar()
        self.sprit = IntVar()

        ###### bill menu ###################
        self.total_cosmatic_price = IntVar()
        self.total_grocery_price = IntVar()
        self.total_drinks_price = IntVar()

        self.cosmatic_tax = IntVar()
        self.grocery_tax = IntVar()
        self.drinks_tax = IntVar()

        ######### customer details ###########
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()

        ## customer details Frame ########
        f1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("monospace", 15, "bold"),fg="gold", bg=bg_color)
        f1.place(x=0,y=80, relwidth=1)

        cname_lbl = Label(f1, bg=bg_color, fg="white", text = "Customer name", font=("monospace",15,"bold")).grid(row=0, column=0,padx=20,pady=5)
        cname_txt = Entry(f1, textvariable=self.c_name, font="monospace 15", width=15,bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)
        
        cphn_lbl = Label(f1, bg=bg_color, fg="white", text = "Phone No.", font=("monospace",15,"bold")).grid(row=0, column=2,padx=20,pady=5)
        cphn_txt = Entry(f1, textvariable=self.c_phone, font="monospace 15", width=15,bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)
        
        c_bill_lbl = Label(f1, bg=bg_color, fg="white", text = "Bill Number", font=("monospace",15,"bold")).grid(row=0, column=4,padx=20,pady=5)
        c_bill_txt = Entry(f1, textvariable=self.bill_no, font="monospace 15", width=15,bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(f1, text="Search", command=self.search_bill, width=10, bd=7, relief=GROOVE, font="monospace 15 bold").grid(row=0, column=6,padx=10,pady=10)


        ###### cosmatic frame ###################

        f2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmatics", font=("monospace", 15, "bold"), fg="gold", bg=bg_color)
        f2.place(x=5, y=185,width=325, height=380)

        bath_lbl = Label(f2, text="Bath Soap", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10,sticky="w")

        bath_txt = Entry(f2, width=10, textvariable=self.soap, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        
        face_cream_lbl = Label(f2, text="Face Cream", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10,sticky="w")

        face_cream_txt = Entry(f2, width=10, textvariable=self.face_creame, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        
        face_w_lbl = Label(f2, text="Face wash", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10,sticky="w")

        face_w_txt = Entry(f2, width=10, textvariable=self.face_wash, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        
        hair_s_lbl = Label(f2, text="Hair Spray", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10,sticky="w")

        hair_s_txt = Entry(f2, width=10, textvariable=self.hair_spray, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        
        hair_g_lbl = Label(f2, text="Hair Gel", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10,sticky="w")

        hair_g_txt = Entry(f2, width=10, textvariable=self.hair_gel, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        
        body_lbl = Label(f2, text="Body lotion", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10,sticky="w")

        body_txt = Entry(f2, width=10, textvariable=self.lotion, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)


        ###### grocery frame ###################

        f3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("monospace", 15, "bold"), fg="gold", bg=bg_color)
        f3.place(x=340, y=185,width=325, height=380)

        g1_lbl = Label(f3, text="Rice", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10,sticky="w")

        g1_txt = Entry(f3, width=10, textvariable=self.rice, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        
        g2_lbl = Label(f3, text="Food Oil", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10,sticky="w")

        g2_txt = Entry(f3, width=10, textvariable=self.food_oil, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        
        g3_lbl = Label(f3, text="Daal", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10,sticky="w")

        g3_txt = Entry(f3, width=10, textvariable=self.daal, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        
        g4_lbl = Label(f3, text="Wheat", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10,sticky="w")

        g4_txt = Entry(f3, width=10, textvariable=self.wheat, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        
        g5_lbl = Label(f3, text="Sugar", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10,sticky="w")

        g5_txt = Entry(f3, width=10, textvariable=self.sugar, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        
        g6_lbl = Label(f3, text="Tea", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10,sticky="w")

        g6_txt = Entry(f3, width=10, textvariable=self.tea, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)


        ###### cold drinks frame ###################

        f4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("monospace", 15, "bold"), fg="gold", bg=bg_color)
        f4.place(x=675, y=185,width=325, height=380)

        c1_lbl = Label(f4, text="Maza", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10,sticky="w")

        c1_txt = Entry(f4, width=10, textvariable=self.maza, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        
        c2_lbl = Label(f4, text="Coke", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10,sticky="w")

        c2_txt = Entry(f4, width=10, textvariable=self.coke, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        
        c3_lbl = Label(f4, text="Frooti", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10,sticky="w")

        c3_txt = Entry(f4, width=10, textvariable=self.frooti, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        
        c4_lbl = Label(f4, text="Thumps Up", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10,sticky="w")

        c4_txt = Entry(f4, width=10, textvariable=self.thumps_up, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
        
        c5_lbl = Label(f4, text="Limca", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10,sticky="w")

        c5_txt = Entry(f4, width=10, textvariable=self.limca, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        
        c6_lbl = Label(f4, text="Sprite", font=("monospace", 14, "bold"), bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10,sticky="w")

        c6_txt = Entry(f4, width=10, textvariable=self.sprit, font=("monospace", 14, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        f5 = Frame(self.root,bd=10, relief=GROOVE)
        f5.place(x=1010, y=185, width=355, height=380)

        bill_title = Label(f5, text="Bill Area", font="monospace 15 bold", bd=7, relief=GROOVE).pack(fill=X)

        scroll_y = Scrollbar(f5, orient=VERTICAL)
        self.textarea = Text(f5,font=('monospace',10),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        #### Button Frame #######################

        f6 = LabelFrame(self.root, bd=6, relief=GROOVE, text="Bill Menu", font=("monospace", 15, "bold"), fg="gold", bg=bg_color)
        f6.place(x=0, y=560,relwidth=1, height=140)

        m1_lbl = Label(f6, text="Total Cosmatic price", bg=bg_color, fg="white", font=("monospace",12, "bold")).grid(row=0, column=0, padx=10, pady=1, sticky="w")
        m1_txt = Entry(f6, width=18, textvariable=self.total_cosmatic_price, font="monospace 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=1, padx=10, pady=1)
        
        m2_lbl = Label(f6, text="Total Grocery price", bg=bg_color, fg="white", font=("monospace",12, "bold")).grid(row=1, column=0, padx=10, pady=1, sticky="w")
        m2_txt = Entry(f6, width=18, textvariable=self.total_grocery_price, font="monospace 10 bold", bd=7, relief=SUNKEN).grid(row=1,column=1, padx=10, pady=1)
        
        m3_lbl = Label(f6, text="Total Cold drinks price", bg=bg_color, fg="white", font=("monospace",12, "bold")).grid(row=2, column=0, padx=10, pady=1, sticky="w")
        m3_txt = Entry(f6, width=18, textvariable=self.total_drinks_price, font="monospace 10 bold", bd=7, relief=SUNKEN).grid(row=2,column=1, padx=10, pady=1)

        n1_lbl = Label(f6, text="Cosmatic Tax", bg=bg_color, fg="white", font=("monospace",12, "bold")).grid(row=0, column=2, padx=10, pady=1, sticky="w")
        n1_txt = Entry(f6, width=18, textvariable=self.cosmatic_tax, font="monospace 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=3, padx=10, pady=1)
        
        n2_lbl = Label(f6, text="Grocery Tax", bg=bg_color, fg="white", font=("monospace",12, "bold")).grid(row=1, column=2, padx=10, pady=1, sticky="w")
        n2_txt = Entry(f6, width=18, textvariable=self.grocery_tax, font="monospace 10 bold", bd=7, relief=SUNKEN).grid(row=1,column=3, padx=10, pady=1)
        
        n3_lbl = Label(f6, text="Cold drinks Tax", bg=bg_color, fg="white", font=("monospace",12, "bold")).grid(row=2, column=2, padx=10, pady=1, sticky="w")
        n3_txt = Entry(f6, width=18, textvariable=self.drinks_tax, font="monospace 10 bold", bd=7, relief=SUNKEN).grid(row=2,column=3, padx=10, pady=1)

        btn_f = Frame(f6, bd=7, relief=GROOVE,bg='#2475B0')
        btn_f.place(x=790)

        total_btn = Button(btn_f, text="Total", command=self.total,bg="cadetblue", fg="white", bd=3, pady=15, width=9, font="monospace 12 bold").grid(row=0, column=0, padx=5, pady=5)
        
        gbill_btn = Button(btn_f, text="Generate Bill", command=self.generate_bill, bg="cadetblue", fg="white", bd=3, pady=15, width=11, font="monospace 12 bold").grid(row=0, column=1, padx=5, pady=5)
        
        clear_btn = Button(btn_f, text="Clear", command=self.clear, bg="cadetblue", fg="white", bd=3, pady=15, width=9, font="monospace 12 bold").grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, text="Exit", command=self.exit, bg="cadetblue", fg="white", bd=3, pady=15, width=9, font="monospace 12 bold").grid(row=0, column=3, padx=5, pady=5)

        self.welcome_bill()

    def total(self):
        self.total_c_p = float(
                                (self.soap.get()*20)+
                                (self.face_creame.get()*60)+
                                (self.face_wash.get()*80)+
                                (self.hair_spray.get()*90)+
                                (self.hair_gel.get()*120)+
                                (self.lotion.get()*150)
                            )
        self.total_cosmatic_price.set(self.total_c_p)

        self.total_g_p = float(
                                (self.rice.get()*34)+
                                (self.food_oil.get()*40)+
                                (self.daal.get()*35)+
                                (self.wheat.get()*60)+
                                (self.sugar.get()*34)+
                                (self.tea.get()*60)
                            )
        self.total_grocery_price.set(self.total_g_p)

        self.total_d_p = float(
                                (self.maza.get()*40)+
                                (self.coke.get()*35)+
                                (self.frooti.get()*20)+
                                (self.thumps_up.get()*60)+
                                (self.limca.get()*30)+
                                (self.sprit.get()*40)
                            )
        self.total_drinks_price.set(self.total_d_p)

        self.total_c_t = self.total_c_p * 0.15
        self.cosmatic_tax.set(round((self.total_c_t),2))
        
        self.total_g_t = self.total_g_p * 0.10
        self.grocery_tax.set(round((self.total_g_t),2))
        
        self.total_d_t = self.total_d_p * 0.15
        self.drinks_tax.set(round((self.total_d_t),2))
    
    def total_price(self):
        self.price = float(
                            self.total_cosmatic_price.get()+
                            self.total_grocery_price.get()+
                            self.total_drinks_price.get()+
                            self.cosmatic_tax.get()+
                            self.grocery_tax.get()+
                            self.drinks_tax.get()
                        )
        return self.price

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.x = random.randint(1000,9999)
        self.bill_no.set(self.x)
        self.textarea.insert(END,"\t Welcome to bhoir retails\n")
        self.textarea.insert(END,f"\nBill no. : {self.bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer name : {self.c_name.get()}")
        self.textarea.insert(END,f"\nCustomer phone : {self.c_phone.get()}")
        self.textarea.insert(END,"\n=======================================")
        self.textarea.insert(END,"\nProducts\t\tQTY\t\tPrice")
        self.textarea.insert(END,"\n=======================================")
    def generate_bill(self):
        if self.c_phone.get=="" or self.c_name.get()=="":
            messagebox.showerror("Error", "Customer name and phone number are must!!")
        elif self.total_cosmatic_price.get()==0.0 and self.total_grocery_price.get()==0.0 and self.total_drinks_price.get()==0.0:
            messagebox.showerror("Error", "No products purchased")
        else:
            self.total()
            self.welcome_bill()
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\nBath Soap\t\t{self.soap.get()}\t\tRs. 20")
            if self.face_creame.get()!=0:
                self.textarea.insert(END,f"\nFace Creame\t\t{self.face_creame.get()}\t\tRs. 60")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\nFace Wash\t\t{self.face_wash.get()}\t\tRs. 80")
            if self.hair_spray.get()!=0:
                self.textarea.insert(END,f"\nHair Spray\t\t{self.hair_spray.get()}\t\tRs. 90")
            if self.hair_gel.get()!=0:
                self.textarea.insert(END,f"\nHair Gel\t\t{self.hair_gel.get()}\t\tRs. 120")
            if self.lotion.get()!=0:
                self.textarea.insert(END,f"\nBody Lotion\t\t{self.lotion.get()}\t\tRs. 150")
            
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\nRice\t\t{self.rice.get()}\t\tRs. 34")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\nFood Oil\t\t{self.food_oil.get()}\t\tRs. 40")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\nDaal\t\t{self.daal.get()}\t\tRs. 35")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\nWheat\t\t{self.wheat.get()}\t\tRs. 60")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\nSugar\t\t{self.sugar.get()}\t\tRs. 34")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\nTea\t\t{self.tea.get()}\t\tRs. 60")
            
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\nMaza\t\t{self.maza.get()}\t\tRs. 40")
            if self.coke.get()!=0:
                self.textarea.insert(END,f"\nCoke\t\t{self.coke.get()}\t\tRs. 35")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\nFrooti\t\t{self.frooti.get()}\t\tRs. 20")
            if self.thumps_up.get()!=0:
                self.textarea.insert(END,f"\nThumps Up\t\t{self.thumps_up.get()}\t\tRs. 60")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\nLimca\t\t{self.limca.get()}\t\tRs. 30")
            if self.sprit.get()!=0:
                self.textarea.insert(END,f"\nSprite\t\t{self.sprit.get()}\t\tRs. 40")
            
            self.textarea.insert(END,"\n---------------------------------------")
            if self.cosmatic_tax.get()!=str(0.0):
                self.textarea.insert(END,f"\nTotal Cosmatic Tax :\t\t\t{self.cosmatic_tax.get()}")
            
            if self.grocery_tax.get()!=str(0.0):
                self.textarea.insert(END,f"\nTotal Grocery Tax : \t\t\t{self.grocery_tax.get()}")
            
            if self.drinks_tax.get()!=str(0.0):
                self.textarea.insert(END,f"\nTotal Cold drinks Tax : \t\t\t{self.drinks_tax.get()}")
            self.textarea.insert(END,"\n---------------------------------------")
            
            self.textarea.insert(END,f"\nTotal Rs : \t\t\t\t{self.total_price()}")

            self.textarea.insert(END,"\n---------------------------------------")
            self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save", "Do you want to save bill?")
        if op > 0:
            self.bill_data = self.textarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
        else:
            return
    
    def search_bill(self):
        present = 'no'
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.bill_no.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0', END)
                for a in f1:
                    self.textarea.insert(END,a)
                f1.close()
                present = 'yes'
        if present=='no':
            messagebox.showerror("Error", "Bill not Found")

    def clear(self):
        self.welcome_bill()
        ##### cosmatics ##################
        self.soap.set(0)
        self.face_creame.set(0)
        self.face_wash.set(0)
        self.hair_spray.set(0)
        self.hair_gel.set(0)
        self.lotion.set(0)
        
        ##### grocery ##################
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)
        
        ##### cold drinks ##################
        self.maza.set(0)
        self.coke.set(0)
        self.frooti.set(0)
        self.thumps_up.set(0)
        self.limca.set(0)
        self.sprit.set(0)

        ###### bill menu ###################
        self.total_cosmatic_price.set(0)
        self.total_grocery_price.set(0)
        self.total_drinks_price.set(0)

        self.cosmatic_tax.set(0)
        self.grocery_tax.set(0)
        self.drinks_tax.set(0)

        ######### customer details ###########
        self.c_name.set("")
        self.c_phone.set("")
    
    def exit(self):
        m = messagebox.askyesno("Exit", "Do you really want to exit?")
        if m > 0:
            self.root.destroy()
        else:
            return
        
    

root=Tk()
obj=bill_app(root)
root.mainloop()