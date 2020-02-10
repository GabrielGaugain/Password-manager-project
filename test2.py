import tkinter.tix as tk

r= tk.Tk()
r.title("test scrolled window")
sw= tk.ScrolledWindow(r, scrollbar=tk.Y) # just the vertical scrollbar
sw.pack(fill=tk.BOTH, expand=1)
for i in range(10):
    e= tk.Entry(sw.window)
    e.pack()
r.mainloop()