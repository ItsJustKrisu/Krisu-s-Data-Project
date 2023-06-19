import csv
import math
from tkinter import *
from tkinter import ttk


# method to display the edit window
def manipulate_data(file_path, width_input, height_input):
    # method to overwrite the data back to the CSV File
    def save_data():
        with open(file_path, 'w', newline='') as input_file:  # opens the file in write mode
            writer = csv.writer(input_file)  # creates a writer object of input file
            writer.writerows(data)  # writes all the rows to the file

    # method made to edit the cells of the data
    def edit_cell(event):
        selected_item = table.focus()  # gets the value from the cell that is selected from the table
        if selected_item:
            cell_column = int(table.identify_column(event.x).lstrip('#')) - 1
            cell_row = int(table.index(selected_item))  # retrieves the location of the selected item
            edit_entry = Entry(window, width=12)  # creates a widget used for the input used in an edition
            edit_entry.insert(0, table.set(selected_item, cell_column))  # sets the default value for the entry widget
            # on the return key press, calls the save method to update the selected cell with an edited entry
            edit_entry.bind('<Return>', lambda e: save_edited_cell(edit_entry, cell_row, cell_column))
            edit_entry.place(relx=0, rely=0, relwidth=1, relheight=1)  # places the widget
            edit_entry.focus_set()  # focuses on it
            edit_entry.selection_range(0, END)  # makes the entry writeable

    # method used to save the edited cell data
    def save_edited_cell(entry, r, c):
        edited_value = entry.get()  # gets the value from the entry
        data[r + 1][c] = edited_value  # replaces the edited value in the data (r + 1 to account for the header row)
        entry.destroy()  # gets rid of the entry
        table.set(table.get_children()[r], column=c, value=edited_value)  # update the value in the table

    window_width = width_input
    window_height = height_input

    # creates the window
    window = Tk()
    window.title("CSV Data Editor")
    window.resizable(True, True)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = math.floor((screen_width - window_width) / 2)
    y = math.floor((screen_height - window_height) / 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # reading the data with the csv library
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    # creates a tree view widget used as a table for the window
    table = ttk.Treeview(window, selectmode='browse')
    table['columns'] = tuple(range(len(data[0])))
    table.pack()

    for i, heading in enumerate(data[0]):  # adding the columns to the table
        table.column(i, width=100, anchor='center')
        table.heading(i, text=heading)

    for row in data[1:]:  # adds rows to the table
        if any(cell.strip() for cell in row):
            table.insert('', 'end', values=row)

    table.bind('<Double-1>', edit_cell)  # makes the cells doubly clickable and editable

    save_button = Button(window, text="Save", command=save_data)  # button made to save the data
    save_button.pack()

    window.mainloop()
