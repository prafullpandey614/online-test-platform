from tkinter import *
import webbrowser
root = Tk(screenName="Prafull Forms")
root.geometry("1000x2000")
def newTest():
    koot = Tk()
    Label(koot,text="This Page is Under Construction ",bg="black",fg="cyan").pack()
    koot.geometry("1000x2000")
    url = "https://admin.typeform.com/accounts/01FD6BJYK94V213A3Q0NYEEXYQ/workspaces/pGC6Hx"

    def test_maker():
        webbrowser.open(url,new=6)
    def swarajya():
        soot = Tk()
        soot.geometry("1000x1000")
        def entry_quest(no_of_questions):
        #    no_of_questions = int(no_of_questions)
            boot = Tk()
            boot.geometry("1000x1000")
            framee = Frame(boot)
          #  Label(framee,text="Enter the number of questions").pack()
           # no = Entry.get(boot).pack()
            
           # boot.config(bg="black")
            dicto = {}
            def listing():
  #     no = int(no)
                for i in range(3):
                    f = Frame(boot)
                    Label(f,text= "enter the question").pack()
                    que = Entry(f).pack()
                    opt_1= Entry(f).pack()
                    opt_2= Entry(f).pack() 
                    opt_3= Entry(f).pack() 
                    opt_4= Entry(f).pack() 
                     
                 #   Button(f,text="save question",bg='black').pack()  
                    def save_quest(q,opt_1,opt_2,opt_3,opt_4):
                        dicto[que:[opt_1,opt_2,opt_3,opt_4]]
                    Button(f,text="save",command=lambda : save_quest(que,opt_4,opt_3,opt_2,opt_1)).pack()
                    f.pack()
            listing()    
            def save_in_txt(dicto):
                list_file = open("devenum.txt","w")
                print(dicto)
                dicto = str(dicto)
                list_file.write(dicto)
                list_file.close()

                
            
            Button(framee ,text="Save All Questions",bg="black",fg="CYAN",command= lambda: save_in_txt(dicto)).pack()
            framee.pack()
            boot.mainloop()
        Label(soot,text="Name Of Organisation").pack()
        NameOfOgn = Entry(soot).pack()
        Label(soot,text=" Description of test").pack()
        des = Entry(soot).pack()
        Label(soot,text="No of Questions  ").pack()
        no_of_questions= Entry(soot).pack()
        
        soot.config(bg="Black")
        Button(soot,text="Next",bg="yellow",fg="black",command=lambda :entry_quest(no_of_questions)).pack()
        soot.mainloop()
    Button(koot,text="Click here to create your first test",command= test_maker).pack()
    Button(koot,text="swarajya",bg="white",command=swarajya).pack()
    koot.config(bg="black")
    koot.mainloop()   
Label(text="Prafull Forms",font="comicsansms 18 bold",bg= "blue",fg="black").pack()
Button(root,text="Create New Test ", bg="Yellow",command = newTest).pack(padx=30)
root.title("Prafull Forms")
root.config(bg="black")
#window = Tk.Toplevel(root)
root.mainloop()