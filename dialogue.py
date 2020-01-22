import tkinter as tk


### Module definissant la classe d'une fentre de dialogue
## the cover method should always be coded in the child method or somewhere
## to get the cover we want.

class Dialogue(tk.Toplevel):

    def __init__(self,container,title = None, center = False,
                 offx = 250,offy=250,color =  "#424142"):

        # associate diag win and its container (root or whatever)
        tk.Toplevel.__init__(self,container)
        self.protocol("WM_DELETE_WINDOW",self.cancel)
        if title:
            self.title(title)
        # transient -> place over other win   
        self.transient(container)
        self.container = container
        self.resultat = None
        self.color = color
        # init frame and apply a cover method which should be implemented in
        # child class
        cadre = tk.Frame(self)
        cadre.config(background = color)
        self.initial_focus = self.cover(cadre)
        cadre.pack(padx=10,pady=10)

        focusDefault = self.boitBoutons()
        if not self.initial_focus:
            self.initial_focus = focusDefault

        # mod win -> catch all events
        self.grab_set()
        # place the dialogbox
        self.center_win(center,offx,offy)

        self.initial_focus.focus_set()
        self.wait_window(self)
        


    def center_win(self,center,offx,offy):
        if center :
            # center the dialog box in the screen
            self.update_idletasks()
            wh = self.winfo_width()
            ht = self.winfo_height()
            swh = self.winfo_screenwidth()
            sht = self.winfo_screenheight()
            xtl,ytl = (swh-wh)//2 , (sht-ht)//2
            self.geometry('+'+str(xtl)+'+'+str(ytl))
        else:
            # place relative to the container
            self.geometry("+"+str(self.container.winfo_rootx() + offx) +
                            "+"+str(self.container.winfo_rooty()+offy)   ) 

    def cover(self, master) :
        pass # surcharged method 


    def cancel(self, event = None):
        self.container.focus_set()
        self.destroy()


    def boitBoutons(self):
        boite = tk.LabelFrame(self, text="Valider") 
        boite.config(background = self.color)
        w1 = tk.Button(boite, text = "Add.", width = 10,
                            command = self.ok, default = tk.ACTIVE)
        w1.pack(side=tk.LEFT, padx = 5, pady = 5)       
        
        w2 = tk.Button(boite, text = 'Generate', width=10,
                            command = self.generate_pw)
        w2.pack(side = tk.LEFT, padx=5,pady=5)

        w3 = tk.Button(boite, text = "Cancel", width = 10,
                            command = self.cancel)
        w3.pack(side=tk.LEFT, padx = 5, pady = 5)       
        self.bind("<Return>", self.ok)       
        self.bind("<Escape>", self.cancel)        
        boite.pack()        
        return w1

    def ok(self, event = None):
        self.initial_focus.focus_set()
        self.withdraw()
        self.update_idletasks()
        self.apply()
        self.cancel()
    
    def apply(self):
        pass #should be surcharged

