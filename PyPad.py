from tkinter import *
from tkinter import font
from tkinter import filedialog

root = Tk("PyPad")
root.title("PyPad")
root.attributes('-alpha', 0.9)

text = Text(root, wrap='word', undo=True)
text.grid(sticky='nsew')

# Create a font object for text styling
current_font_family = 'Arial'
current_font_size = 12
text_font = font.Font(family=current_font_family, size=current_font_size)
text.configure(font=text_font)

def change_font_for_selection(font_family):
    global current_font_family
    current_font_family = font_family
    selected_text = text.tag_ranges(SEL)
    if selected_text:
        text.tag_add("selected_font", "sel.first", "sel.last")
        text.tag_configure("selected_font", font=(font_family, current_font_size))


def toggle_bold():
    current_tags = text.tag_names("sel.first")
    if "bold" in current_tags:
        text.tag_remove("bold", "sel.first", "sel.last")
    else:
        text.tag_add("bold", "sel.first", "sel.last")
        text.tag_configure("bold", font=(current_font_family, current_font_size, 'bold'))

def toggle_italic():
    current_tags = text.tag_names("sel.first")
    if "italic" in current_tags:
        text.tag_remove("italic", "sel.first", "sel.last")
    else:
        text.tag_add("italic", "sel.first", "sel.last")
        text.tag_configure("italic", font=(current_font_family, current_font_size, 'italic'))

def toggle_underline():
    current_tags = text.tag_names("sel.first")
    if "underline" in current_tags:
        text.tag_remove("underline", "sel.first", "sel.last")
    else:
        text.tag_add("underline", "sel.first", "sel.last")
        text.tag_configure("underline", font=(current_font_family, current_font_size, 'underline'))

def saveas():
    try:
        t = text.get("1.0", "end-1c")
        savelocation = filedialog.asksaveasfilename()
        file1 = open(savelocation, "w+")
        file1.write(t)
        file1.close()
    except:
        print("File not saved!")
        pass

button_font = font.Font(family='Arial', size=10, weight='bold')

button_frame = Frame(root)
button_frame.grid(sticky='ew')

Button(button_frame, text="Save As", command=saveas, font=button_font, bg='#e05141', fg='#ffffff', activebackground='#ffffff', activeforeground='#e05141', padx=10, pady=5, borderwidth=2).pack(side='right')
Button(button_frame, text="Bold", command=toggle_bold).pack(side='left')
Button(button_frame, text="Italic", command=toggle_italic).pack(side='left')
Button(button_frame, text="Underline", command=toggle_underline).pack(side='left')

# Dropdown menu for font selection
font_menu = Menubutton(button_frame, text="Font")
font_menu.menu = Menu(font_menu, tearoff=0)
font_menu["menu"] = font_menu.menu

fonts = ["Arial", "Courier", "Times New Roman", "Verdana"]
for f in fonts:
    font_menu.menu.add_command(label=f, command=lambda f=f: change_font_for_selection(f))

font_menu.pack(side='left')



root.mainloop()