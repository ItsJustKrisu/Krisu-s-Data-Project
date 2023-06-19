import math
import tkinter as tk
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class VariableSelector:  # a small class made to store the options of the variable to create the plots
    def __init__(self, options):
        self.options = options  # stores the header options
        self.selected = None  # stores the stored selector, with the default of None

    def select_variable(self, variable):
        self.selected = variable  # updates the selected variable with the chosen variable form the window


def visualize_data(data_path, width_input, height_input):
    data = pd.read_csv(data_path)  # reads csv with the help of panda

    window_width = width_input  # sets the window height and width
    window_height = height_input

    window = tk.Tk()  # creates and modifies the window
    window.title("Data Visualization")
    window.resizable(False, False)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = math.floor((screen_width - window_width) / 2)
    y = math.floor((screen_height - window_height) / 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    fig, ax = plt.subplots()  # creates a figure, and axes of the plot

    canvas = FigureCanvasTkAgg(fig, master=window)  # creates a widget that draws the plot in the tkinter window
    canvas.draw()  # draws the canvas window
    canvas.get_tk_widget().pack()  # packs it into the window

    x_selector = VariableSelector(data.columns)  # creates the objects of Variable Selector for both x and y axis
    y_selector = VariableSelector(data.columns)

    # function responsible for updating of the plot based on selected x and y values, and also the plot type
    # *_ acts as a placeholder, to make sure that parameters connected to event handler won't break the code
    def update_plot(*_):
        # clear the Axes
        ax.clear()

        sns.set(style="ticks")  # sets the default plot style
        if x_selector.selected is not None and y_selector.selected is not None:
            plot_type = plot_type_var.get()  # retrieves the variable from the plot type
            match plot_type:  # creates a plot of a given type
                case "Scatter":
                    sns.scatterplot(data=data, x=x_selector.selected, y=y_selector.selected, ax=ax)
                case "Line":
                    sns.lineplot(data=data, x=x_selector.selected, y=y_selector.selected, ax=ax)
                case "Bar":
                    sns.barplot(data=data, x=x_selector.selected, y=y_selector.selected, ax=ax)
        canvas.draw()

    # function made to update the x selector
    def on_select_x(*_):
        x_selector.select_variable(x_variable.get())  # changes the x variable of the plot
        update_plot()  # updates the plot

    # same function, but for y selector
    def on_select_y(*_):
        y_selector.select_variable(y_variable.get())
        update_plot()

    # setting the widgets for the window
    x_label = tk.Label(window, text="Select X Variable: ")
    x_label.pack(side=tk.LEFT, padx=10)
    x_variable = tk.StringVar()
    x_dropdown = tk.OptionMenu(window, x_variable, *data.columns)
    x_dropdown.pack(side=tk.LEFT, padx=10)
    x_variable.trace('w', on_select_x)

    y_label = tk.Label(window, text="Select Y Variable: ")
    y_label.pack(side=tk.LEFT, padx=10)
    y_variable = tk.StringVar()
    y_dropdown = tk.OptionMenu(window, y_variable, *data.columns)
    y_dropdown.pack(side=tk.LEFT, padx=10)
    y_variable.trace('w', on_select_y)

    plot_type_label = tk.Label(window, text="Select Plot Type: ")
    plot_type_label.pack(side=tk.LEFT, padx=10)
    plot_type_var = tk.StringVar()
    plot_type_var.set("Scatter")
    plot_type_dropdown = tk.OptionMenu(window, plot_type_var, "Scatter", "Line", "Bar")
    plot_type_dropdown.pack(side=tk.LEFT, padx=10)
    plot_type_var.trace('w', update_plot)

    tk.mainloop()
