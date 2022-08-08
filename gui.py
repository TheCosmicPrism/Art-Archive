import tkinter as TK
from tkinter import ttk
import ttkthemes




class main_app():
    def __init__(self) -> None:
        pass
    
    def main_win():
        pass
    

root = TK.Tk()
root.minsize(560, 480)
style = TK.ttk.Style()
root.title("Art Archive")
root_menu = TK.Menu(root)
root.config(menu=root_menu)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)

#Hierarchical treeview-----
#database_frame = ttk.Frame()
#database_frame.columnconfigure(0, weight=1)
#database_frame.pack()
database_treeview = ttk.Treeview(root, columns="database_tree", show="headings")
database_treeview.heading("database_tree", text="Database Tree")

database_treeview.grid(column=0, row=0)
ttk.Button(text="gg")
#menu items-----
#file menu item
file_menu = TK.Menu(root_menu)
root_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
#edit menu item
edit_menu = TK.Menu(root_menu)
root_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy")
#search menu item
search_menu = TK.Menu(root_menu)
root_menu.add_cascade(label="Search", menu=search_menu)
search_menu.add_cascade(label="Find Item")
#view menu item
view_menu = TK.Menu(root_menu)
root_menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Unfold all tree")
view_menu.add_command(label="Fold all tree")
#settings menu item
setting_menu = TK.Menu(root_menu)
root_menu.add_cascade(label="Settings", menu=setting_menu)
setting_menu.add_command(label="Preferences")
#Window menu item
window_menu = TK.Menu(root_menu)
root_menu.add_cascade(label="Window", menu=window_menu)
window_menu.add_command(label="Sort by")
window_menu.add_separator()
window_menu.add_command(label="Windows...")
#help menu item
help_menu = TK.Menu(root_menu)
root_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Manual")
help_menu.add_separator()
help_menu.add_command(label="Debug info")
help_menu.add_command(label="About")



