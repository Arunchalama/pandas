import pandas as pd
import tkinter as tk
from tkinter import ttk

# Function to display DataFrame in Tkinter window
def display_dataframe():
    # Example 1: Creating a DataFrame
    data = {'Name': ['Arunachalam', 'ashik', 'sujith'],
            'Age': [25, 30, 23],
            'City': ['kerala', 'chennai', 'coimbatore']}
    df = pd.DataFrame(data)#two dim data

    # Create a new Tkinter window
    window = tk.Toplevel(root)
    window.title("Pandas DataFrame in Tkinter")

    # Create a text widget to display the DataFrame
    text_widget = tk.Text(window, width=40, height=10)
    text_widget.pack(expand=True, fill='both')

    # Display the DataFrame in the text widget
    text_widget.insert(tk.END, str(df))

# Create the main Tkinter window
root = tk.Tk()
root.title("Pandas Tkinter Example")

# Create a button to trigger the display_dataframe function
display_button = ttk.Button(root, text="Display DataFrame", command=display_dataframe)
display_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()