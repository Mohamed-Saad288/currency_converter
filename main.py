from tkinter import *
from tkinter import messagebox
from tkinter import ttk


root = Tk()
root.title("Currency Converter")
root.geometry('500x500')
root.iconbitmap("C:\\Users\\LORD TRADE\\PycharmProjects\\Currency Converter\\image\\flying-money.ico")

# Create Taps
my_notebook = ttk.Notebook()
my_notebook.pack(pady='5')

# Create Two Frames
currency_frame = Frame(my_notebook,width=480,height=480,bg='DarkSlateGray')
conversion_frame = Frame(my_notebook,width=480,height=480,bg='DarkSlateGray')
currency_frame.pack(fill='both',expand=1)
conversion_frame.pack(fill='both',expand=1)


# Add Our Taps
my_notebook.add(currency_frame,text='Currencies')
my_notebook.add(conversion_frame,text='Convert')

# Disable 2nd App
my_notebook.tab(1,stat='disabled')
# Currency Stuff
def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning('WARNING','You Did Not Fill Out The Filedes')
    else:
        # Disabled entry boxs
        home_entry.config(stat='disabled')
        conversion_entry.config(stat='disabled')
        rate_entry.config(stat='disabled')
        # Enable Tab
        my_notebook.tab(1, stat='normal')
        #Change Tab Filed
        amount_label.config(text=f'Amount of {home_entry.get()} To {conversion_entry.get()}')
        converted_label.config(text=f'Equals The Many {converted_entry.get()}')
        convert_button.config(text=f'Convert From {home_entry.get()}')
def unlock():
    # Enable Entry Boxs
    home_entry.config(stat='normal')
    conversion_entry.config(stat='normal')
    rate_entry.config(stat='normal')
    #Disable Tab
    my_notebook.tab(1, stat='disable')



home = LabelFrame(currency_frame,text="Home Currency",bg='DarkSlateGray',fg='white')
home.pack(pady=20)

# Home Currency Entry box
home_entry = Entry(home,font=("Helvetica",24))
home_entry.pack(pady=10,padx=10)

# conversion currency Frame

conversion = LabelFrame(currency_frame,text='Conversion Currency',bg='DarkSlateGray',fg='white')
conversion.pack(pady=20)

# Convert To Label
conversion_label = Label(conversion,text="Currency to Convert to...",bg='DarkSlateGray',fg='Linen',font=('bold',18))
conversion_label.pack(pady=10)

# Convert to Entry
conversion_entry = Entry(conversion,font=("Helvetica",24))
conversion_entry.pack(pady=10 , padx=10)

# Rate Label
rate_label = Label(conversion,text="Current Conversion Rate...",bg='DarkSlateGray',fg='Linen',font=('bold',18))
rate_label.pack(pady=10)

# Rate Entry
rate_entry = Entry(conversion,font=("Helvetica",24))
rate_entry.pack(pady=10,padx=10)

# Button Frame
button_frame = Frame(currency_frame,bg='DarkSlateGray')
button_frame.pack(pady=10)

# Create buttons
lock_button = Button(button_frame,text='Lock',command=lock,bg='DarkViolet',fg='Linen',bd=0,width=12,font=('bold',12))
lock_button.grid(row=0,column=0,padx=10)

unlock_button = Button(button_frame,text='Unlock',command=unlock,bg='DodgerBlue',fg='Linen',bd=0,width=12,font=('bold',12))
unlock_button.grid(row=0,column=1,padx=10)


# Conversion Stuff
def convert():
    # Clear Converted Entry Box
    conversion_entry.delete(0,END)
    # Convert
    conversion = float(rate_entry.get()) * float(amount_entry.get())
    # Convert two Decimals
    conversion = round(conversion,1)
    # Add Commas
    conversion = '{:,}'.format(conversion)
    # Update Entry Box
    converted_entry.insert(0,f'${conversion}')

def clear():
    amount_entry.delete(0,END)
    converted_entry.delete(0,END)



amount_label = LabelFrame(conversion_frame,text="Amount to Convert",bg='DarkSlateGray',fg='white',font=('bold',15))
amount_label.pack(pady=20)

# Entry Box For Amount
amount_entry = Entry(amount_label,font=("Helvetica",24))
amount_entry.pack(pady=10,padx=10)

# Convert Button
convert_button = Button(amount_label,text="Convert",command=convert,bg='DarkViolet',fg='Linen',bd=0,width=22,font=('bold',12))
convert_button.pack(pady=20)

# Equals Frame
converted_label = LabelFrame(conversion_frame,text='Converted Currency',bg='DarkSlateGray',font=('bold',15),fg='white')
converted_label.pack(pady=20)

# Converted Entry
converted_entry = Entry(converted_label,font=("Helvetica",24),bd=0,bg='systembuttonface')
converted_entry.pack(pady=10,padx=10)

# Clear Button
clear_button = Button(conversion_frame,text='Clear',command=clear,bg='DodgerBlue',fg='Linen',bd=0,width=12,font=('bold',12))
clear_button.pack(pady=20)

# Fake Label For Spacing
spacer = Label(conversion_frame,text='',width=68,bg='DarkSlateGray')
spacer.pack()

root.mainloop()


