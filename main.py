from customer import Customer, Pull
import tkinter as tk

root = tk.Tk()
root.geometry("800x800")

pull = Pull()

def clear_root():
    for widget in root.winfo_children():
        widget.destroy()

def search_by(entry: str, type: str):
    clear_root()
    root.title("Search By Name")
    main_frame = tk.Frame(root)
    main_frame.pack(expand = True, anchor = "n")

    top_row = tk.Frame(main_frame)
    top_row.pack(pady = 5)

    back_btn =  tk.Button(top_row, command = start_screen, text = "Back", font = ("Times New Roman", 10), relief = "flat", activebackground="gray", bg = "#044f8c")
    back_btn.pack(padx = 10)

    row1 = tk.Frame(main_frame)
    row1.pack(pady = 20)
    
    customer_list = pull.customers()
    if type == "name":
        nothing = True
        for customer in customer_list:
            if entry.lower() in customer["name"].lower():
                name = customer["name"]
                id = customer["id"]
                number = pull.get("number", id)
                button = tk.Button(row1, text = f"{name} | {number}", font = ("Times New Roman", 10), relief = "flat", activebackground="gray", bg = "#044f8c")
                button.pack(pady = 2)
                nothing = False
    
        if nothing:
            label = tk.Label(row1, text = f"Sorry, No results for: {entry}", font = ("Times New Roman", 25))
            label.pack(pady = 50)

    elif type == "number":
        nothing = True
        for customer in customer_list:
            id = customer["id"]
            number = pull.get("number", id)
            if entry.lower() in number.lower():
                name = customer["name"]
                button = tk.Button(row1, text = f"{name} | {number}", font = ("Times New Roman", 10), relief = "flat", activebackground="gray", bg = "#044f8c")
                button.pack(pady = 2)
                nothing = False
    
        if nothing:
            label = tk.Label(row1, text = f"Sorry, No results for this number: {entry}", font = ("Times New Roman", 25))
            label.pack(pady = 50)

    elif type == "email":
        nothing = True
        for customer in customer_list:
            id = customer["id"]
            email = pull.get("email", id)
            if entry.lower() in email.lower():
                name = customer["name"]
                number = pull.get("number", id)
                button = tk.Button(row1, text = f"{name} | {number}", font = ("Times New Roman", 10), relief = "flat", activebackground="gray", bg = "#044f8c")
                button.pack(pady = 2)
                nothing = False
    
        if nothing:
            label = tk.Label(row1, text = f"Sorry, No results for this email: {entry}", font = ("Times New Roman", 25))
            label.pack(pady = 50)

def add_customer():
    clear_root()
    root.title("New Customer")
    #not finished



def start_screen():
    clear_root()
    root.title("Customer Database")
    main_frame = tk.Frame(root)
    main_frame.pack(expand = True, anchor = "n")

    row1 = tk.Frame(main_frame)
    row1.pack(pady = 50)

    label = tk.Label(row1, text = "Customer Database", font = ("Times New Roman", 25))
    label.pack()

    row2 = tk.Frame(main_frame)
    row2.pack(pady = 20)

    customer_lookup_entry = tk.Entry(row2, font = ("Arial", 16))
    customer_lookup_entry.pack(side = "left")

    lookup_name_btn = tk.Button(row2,command = lambda: search_by(customer_lookup_entry.get(), "name"), height=1, text = "Search Name", font = ("Times New Roman", 11), relief = "flat", activebackground="gray", bg = "#044f8c")
    lookup_name_btn.pack(side = "left", padx = 2)

    lookup_number_btn = tk.Button(row2, command = lambda: search_by(customer_lookup_entry.get(), "number"), height=1, text = "Search Number", font = ("Times New Roman", 11), relief = "flat", activebackground="gray", bg = "#044f8c")
    lookup_number_btn.pack(side = "left", padx = 2)

    lookup_email_btn = tk.Button(row2, command = lambda: search_by(customer_lookup_entry.get(), "email"), height=1, text = "Search Email", font = ("Times New Roman", 11), relief = "flat", activebackground="gray", bg = "#044f8c")
    lookup_email_btn.pack(side = "left", padx = 2)

    row3 = tk.Frame(main_frame)
    row3.pack(pady = 20)

    new_customer_btn = tk.Button(row3, command = add_customer, text = "Add Customer +", font = ("Times New Roman", 20), relief = "flat", activebackground="gray", bg = "#044f8c")
    new_customer_btn.pack()

    row4 = tk.Frame(main_frame)
    row4.pack(pady = 20)

    pull_list_btn = tk.Button(row4, text = "Pull List", font = ("Times New Roman", 20), relief = "flat", activebackground="gray", bg = "#044f8c")
    pull_list_btn.pack(pady = 10)



def main():
    start_screen()
    root.mainloop()
    


if __name__ == "__main__":
    main()