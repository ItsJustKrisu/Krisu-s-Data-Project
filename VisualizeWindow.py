import math
import tkinter as tk
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class VariableSelector:
    def __init__(self, options):
        self.options = options
        self.selected = None

    def select_variable(self, variable):
        self.selected = variable


def visualize_data(data_path, width_input, height_input):
    data = pd.read_csv(data_path)

    window_width = width_input
    window_height = height_input

    window = tk.Tk()
    window.title("Data Visualization")
    window.resizable(False, False)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = math.floor((screen_width - window_width) / 2)
    y = math.floor((screen_height - window_height) / 2)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    fig, ax = plt.subplots()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    x_selector = VariableSelector(data.columns)
    y_selector = VariableSelector(data.columns)

    def update_plot(*_):
        # clear the Axes
        ax.clear()

        sns.set(style="ticks")
        if x_selector.selected is not None and y_selector.selected is not None:
            plot_type = plot_type_var.get()
            if plot_type == "Scatter":
                sns.scatterplot(data=data, x=x_selector.selected, y=y_selector.selected, ax=ax)
            elif plot_type == "Line":
                sns.lineplot(data=data, x=x_selector.selected, y=y_selector.selected, ax=ax)
            elif plot_type == "Bar":
                sns.barplot(data=data, x=x_selector.selected, y=y_selector.selected, ax=ax)

        canvas.draw()

    def on_select_x(*_):
        x_selector.select_variable(x_variable.get())
        update_plot()

    def on_select_y(*_):
        y_selector.select_variable(y_variable.get())
        update_plot()

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
