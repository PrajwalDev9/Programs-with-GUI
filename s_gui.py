
from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox


class Store(object):


    def __init__(self,item,amount,price):
        
        self.item = item
        self.amount =amount
        self.price = price
       


class Library:
    def __init__(self,root):
        self.root=root
        self.root.title("Store Management System")
        self.root.geometry("920x520+0+0")
        self.root.configure(background='powder blue')


        Item=StringVar()
        Amount=IntVar()
        Price=IntVar()
        

        def iReset():
            Item.set("")
            Amount.set("")
            Price.set("")
          
            
        def iReset2():
            self.bookdisplydata.delete("1.0",END)
           
        def iExit():
            iExit=tkinter.messagebox.askyesno("Shop Management System","Confirm You want to exit?")
            if iExit > 0:
                root.destroy()
                return
            
        def iSubmit():
            iSubmit=tkinter.messagebox.askyesno("Shop management","Is there another item? Press Yes or No")
            total=0
            if iSubmit < 1:
                total += Amount.get()*Price.get()
                self.bookdisplydata.insert(END,"Total:"+str(total))
                return
                
                

            
        

        def idisplayall():
            
                
            book_list=[]
            item=Item.get()
            
            if type(item)==str and item!=None and len(item)>=4: # VALIDTION OF INPUT
                item= item
                
        
            else:
                tkinter.messagebox.showerror("Input not valid","Please enter valid Item")
                return
                    
                
                
            amount=Amount.get()
            if type(amount)==int and b_author!=None : # VALIDTION OF INPUT
                    amount= amount

        
            else:
                tkinter.messagebox.showerror("Input not valid","Please enter valid Amount!!")
                return
                    
            
                        

            
            b_title=BookTitle.get()
            if type(b_title)==str and b_title!=None and len(b_title)>=4: # VALIDTION OF INPUT
                    b_title= b_title

        
            else:
                tkinter.messagebox.showerror("Input not valid","Please enter valid book title!!")
                return
                
        
            
            
            if  book_list == []:
                tkinter.messagebox.showerror("Input not valid","First insert the record")
                
                 
            else:
                for i in book_list:
                    self.bookdisplydata.insert(END,"Book ID:"+i.b_id+"\n"+"Book Author:"+i.b_author+"\n"+"Book Title:"+i.b_title+"\n"+"Book Publication:"+i.b_publication+"\n")
                
                
            

                
            










            
                    #===================Frame==================
        #main frame
        MainFrame = Frame(self.root)
        MainFrame.grid()

        
        #Title frame
        TitleFrame = Frame(MainFrame,width=1350,padx=20,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle=Label(TitleFrame,width=39,font=('arial',25,'bold'),text="\tShop Management System\t",padx=12)
        self.lblTitle.grid()

        #button frame
        ButtonFrame=Frame(MainFrame,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        # frame
        DataFrame=Frame(MainFrame,bd=20,width=1100,height=50,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        #add book label frame
        DataFrameLEFT = LabelFrame(DataFrame,bd=10,width=400,height=320,padx=20,relief=RIDGE,font=('arial',12,'bold'))
        DataFrameLEFT.pack(side=LEFT)

        
        #addbook text display
        
        DataFrameRIGHT = LabelFrame(DataFrame,bd=10,width=400,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'))
        DataFrameRIGHT.pack(side=RIGHT)

        #===================widget=========================================================================================================================
        
        self.bookdisplydata=Text(DataFrameRIGHT,font=('arial',14,'bold'),width=30,height=12,padx=8,pady=20)
        self.bookdisplydata.grid(row=0,column=0)

        """
        ListOfBooks=['c','c++','java','computer network','Python','System enginerring',
                     'c','c++','java','computer network','Python','System enginerring',
                     'c','c++','java','computer network','Python','System enginerring']


        for i in ListOfBooks:
            
            self.bookdisplydata.insert(END,i)
        """
        #=======================================================================================================
        

      
        #===================widget=========================================================================================================================

        self.lblItem = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Item:",padx=2,pady=2)
        self.lblItem.grid(row=0,column=0,sticky=W)
        self.txtItem = Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Item,width= 25)
        self.txtItem.grid(row=0,column=1)
        

        
            

            
           


        self.lblAmount = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Amount:",padx=2,pady=2)
        self.lblAmount.grid(row=1,column=0,sticky=W)
        self.txtAmount=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Amount,width=25)
        self.txtAmount.grid(row=1,column=1)

        self.lblPrice = Label(DataFrameLEFT,font=('arial',12,'bold'),text="Price:",padx=2,pady=2)
        self.lblPrice.grid(row=2,column=0,sticky=W)
        self.txtPrice=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Price,width=25)
        self.txtPrice.grid(row=2,column=1)

        
            
       #====================================================================================================================

        
        









        

        #=============================Buttons==================================================================
       
        self.btnReset=Button(ButtonFrame,text="Reset",font=('arial',12,'bold'),width=19,bd=4,command=iReset)
        self.btnReset.grid(row=0,column=2)

        self.btnExit=Button(ButtonFrame,text="Exit",font=('arial',12,'bold'),width=18,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=3)

        self.btnSubmit=Button(ButtonFrame,text="Submit",font=('arial',12,'bold'),width=18,bd=4,command=iSubmit)
        self.btnSubmit.grid(row=0,column=1)
        
        

        
        
        
        
        


        

        
        



        
if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()
    
