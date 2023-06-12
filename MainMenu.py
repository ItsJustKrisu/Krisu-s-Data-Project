import math
import tkinter
from tkinter import filedialog
import EditWindow
import VisualizeWindow


# A method created to make browsing files to find the CSV files easier
def select_csv_file():
    global file_path
    # Gives an easy-to-use file explorer that will look for the files with an .csv extension only
    file_path = tkinter.filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    file_path_label.config(text=file_path)  # changes the label to represent the current chosen path


# A method made to open the window for visualization of selected data
def visualize_selected_file():
    if file_path:
        # Opens the visualize window for the selected file, and with the current resolution
        VisualizeWindow.visualize_data(file_path, window_width, window_height)
    else:
        print("No file is chosen!")


# A method made to open the window for edition of selected data files
def edit_selected_file():
    if file_path:
        # opens the edit_window for easy manipulation of the data files
        EditWindow.manipulate_data(file_path, window_width, window_height)
    else:
        print("No file is chosen!")


window = tkinter.Tk()  # creates a new window
window.title("Krisu's Data Analysis!")  # sets up a title of the window
window.resizable(False, False)  # sets the window as not resizable

window_width = 900
window_height = 600
screen_width = window.winfo_screenwidth()  # gets
screen_height = window.winfo_screenheight()
x = math.floor((screen_width - window_width) / 2)
y = math.floor((screen_height - window_height) / 2)
# sets up the general geometry of the window (it's a starting position, and size)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

text_label = tkinter.Label(window, text="Krisu's Basic Data App !?")  # sets the basic title label
text_label.config(font=("Sans", 25))  # makes the font bigger
text_label.pack()  # packs the component

file_path = ""  # initializes an empty value for the file path
file_path_label = tkinter.Label(window, text=file_path)  # creates a label to show the last chosen path
file_path_label.pack()

button_frame = tkinter.Frame(window)  # creates a frame, that will hold the buttons
button_frame.pack()


# creates a button made for selecting the file through the file browser
open_button = tkinter.Button(button_frame, text="Select File", command=select_csv_file)
open_button.pack(side="left")  # packs the button in a horizontal line

# creates a button that will open the edit window for the chosen file
edit_button = tkinter.Button(button_frame, text="Edit File", command=edit_selected_file)
edit_button.pack(side="left")

# creates a button that will open the visualization window for the chosen file
visualize_button = tkinter.Button(button_frame, text="Visualize File", command=visualize_selected_file)
visualize_button.pack(side="left")

window.mainloop()  # creates a main loop of the window, that will be the main runtime of the program
