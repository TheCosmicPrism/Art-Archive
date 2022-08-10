import tkinter as TK
from tkinter import Tk, ttk
import ttkthemes
from fileFetch import fileFetcher




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
#root row and cols configs
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)


#Hierarchical treeview-----
database_HierTreeview = ttk.Treeview(root)
#database_HierTreeview.heading("database_tree", text="Database Tree")

#data--#todo generate the data to be added in a way to reflect the data in fileDisplay Hierarchical treeview
database_HierTreeview.insert("", "0", "item1", text=("demo",))
database_HierTreeview.insert("", "1", "item2", text=("deme",))
database_HierTreeview.insert("", "2", "item3", text=("dmmm",))
database_HierTreeview.insert("", "end", "item4", text=("domo",))
database_HierTreeview.insert("item1", "end", "demo C1", text="demo C1")
database_HierTreeview.insert("item1", "end", "demo C2", text="demo C1")
database_HierTreeview.insert("item2", "end", "demo C3", text="demo C2")
database_HierTreeview.insert("item3", "end", "demo C4", text="demo C1")
database_HierTreeview.move('item2', 'item1', 'end') 
database_HierTreeview.move('item3', 'item1', 'end')
#--
database_HierTreeview.grid(column=0, row=0, sticky="ns")

#FileDisplay-----#todo generate cols dynamically after the data is collected
file_frame = ttk.Frame(root)
file_TV_catagories = []
file_cols = ["file_name", "file_entry_date", "file_type"]
#cols and rows config
file_frame.columnconfigure(0, weight=1)
file_frame.columnconfigure(1, weight=0)
file_frame.rowconfigure(0, weight=1)
file_frame.rowconfigure(1, weight=0)

database_fileTreeview = ttk.Treeview(file_frame, columns=file_cols, show="headings")
#genrating the names of the columns of the File Treeview
for colId in file_cols:
    long_text = str()
    tx = colId.capitalize().split("_")
    for word in tx:
        long_text = long_text + " " + word
    database_fileTreeview.heading(colId, text=long_text)

#data--#todo generate the data to be added

database_fileTreeview.insert("", "0", "item01", values=("demo...","doodo", "dede"))
database_fileTreeview.insert("", "1", "item02", values=("femo","foofo", "fefe"))
database_fileTreeview.insert("item01", "end", "item01.1", values=("memo","moomo", "meme"))
#--
database_fileTreeview.grid(column=0, row=0, sticky="nsew")
#Infobar-----
infoBar_frame = ttk.Frame(file_frame)
info_currentTask_progressBar = ttk.Progressbar(infoBar_frame,maximum=100.0, orient="horizontal", value=35.0)
info_currentTask_name = ttk.Entry(infoBar_frame, width=40)
info_saveStatus = ttk.Entry(infoBar_frame, width=5)

infoBar_frame.columnconfigure(0, weight=1)
infoBar_frame.columnconfigure(1, weight=1)
infoBar_frame.columnconfigure(2, weight=1)
infoBar_frame.rowconfigure(0, weight=1)

info_currentTask_progressBar.grid(column=0, row=0, sticky="ew")
info_currentTask_name.grid(column=1, row=0, sticky="ew")
info_saveStatus.grid(column=2, row=0, sticky="ew")
infoBar_frame.grid(column=0, row=1, sticky="ew")
#-----
file_frame.grid(column=1, row=0, sticky="nsew")


#menu items-----
#file menu item
file_menu = TK.Menu(root_menu, tearoff=False)
root_menu.add_cascade(label="File", menu=file_menu)

#sub menu New
sub_file_menu = TK.Menu(file_menu, tearoff=False)
#tip lambda make the funchen not work by itself, #todo read about Lambda
sub_file_menu.add_command(label="New file path", command= lambda :fileFetcher.SetFilePath())
sub_file_menu.add_command(label="New database")
file_menu.add_cascade(label="New...", menu=sub_file_menu)
#--
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")

file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
#edit menu item
edit_menu = TK.Menu(root_menu, tearoff=False)
root_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy")
#search menu item
search_menu = TK.Menu(root_menu, tearoff=False)
root_menu.add_cascade(label="Search", menu=search_menu)
search_menu.add_cascade(label="Find Item")
#view menu item
view_menu = TK.Menu(root_menu, tearoff=False)
root_menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Unfold all tree")
view_menu.add_command(label="Fold all tree")
#settings menu item
setting_menu = TK.Menu(root_menu, tearoff=False)
root_menu.add_cascade(label="Settings", menu=setting_menu)
setting_menu.add_command(label="Preferences")
#Window menu item
window_menu = TK.Menu(root_menu, tearoff=False)
root_menu.add_cascade(label="Window", menu=window_menu)
window_menu.add_command(label="Sort by")
window_menu.add_separator()
window_menu.add_command(label="Windows...")
#help menu item
help_menu = TK.Menu(root_menu, tearoff=False)
root_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Manual")
help_menu.add_separator()
help_menu.add_command(label="Debug info")
help_menu.add_command(label="About")



