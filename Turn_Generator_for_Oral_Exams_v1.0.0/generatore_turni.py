# """
# ******************************************************************************
# *                                                                            *
# *                         Turn Generator for Oral Exams                      *
# *                                                                            *
# * DESCRIPTION:                                                               *
# * This program generates randomized turn sequences for oral exams. It allows *
# * the user to either create individual turn sequences or divide students into*
# * groups. The program features a graphical user interface (GUI) built with   *
# * Tkinter. The user can choose between generating individual turns or groups *
# * and generate the turn order with a click of a button.                      *
# *                                                                            *
# * Copyright (c) 2024, Nico Fontani                                           *
# * Creation Date: 25 Nov 2024                                                 *
# *                                                                            *
# * Original Author: Nico Fontani                                              *
# * Last Modified: 25 Nov 2024                                                 *
# *                                                                            *
# * Supported by Python, Tkinter, and random                                   *
# *                                                                            *
# ******************************************************************************
# """

import tkinter as tk
from tkinter import messagebox
import random

# List of students (alphabetically by last name) put here all names of students
students = [
    "ANDERSON JACKSON",
    "BROWN DAVID",
    "DAVIS EMMA",
    "HARRIS NATHANIEL",
    "JONES BENJAMIN",
    "KING PATRICK",
    "MARTIN KAREN",
    "MILLER FREDERICK",
    "MOORE HARRY",
    "SMITH ALICE",
    "TAYLOR ISLA",
    "THOMAS LUCAS",
    "WHITE MEGAN",
    "WILLIAMS CHLOE",
    "WILSON GABRIELA",
    "YOUNG OLIVIA"
]


# Function to generate individual turns
def generate_individual_turns(students):
    random.shuffle(students)  # Shuffle the students randomly
    turns = "\n".join([f"Turn {i+1}: {student}" for i, student in enumerate(students)])
    return turns

# Function to generate groups
def generate_groups(students, group_size):
    random.shuffle(students)  # Shuffle the students randomly
    divided_groups = [students[i:i + group_size] for i in range(0, len(students), group_size)]
    
    groups_text = ""
    for i, group in enumerate(divided_groups, 1):
        groups_text += f"Group {i}: {', '.join(group)}\n"
    return groups_text

# Function called by the "Generate Turns" button
def generate_turns():
    # Use the predefined list of students
    students_copy = students.copy()

    # Check the user's choice
    if var_choice.get() == "individual":
        turns = generate_individual_turns(students_copy)
        text_output.delete(1.0, tk.END)  # Clear the text area
        text_output.insert(tk.END, turns)  # Show the turns
    elif var_choice.get() == "groups":
        try:
            num_groups = int(entry_groups.get())
            if num_groups < 1 or num_groups > len(students_copy):
                raise ValueError("Invalid number of students per group.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of students per group.")
            return
        groups = generate_groups(students_copy, num_groups)
        text_output.delete(1.0, tk.END)  # Clear the text area
        text_output.insert(tk.END, groups)  # Show the groups
    else:
        messagebox.showerror("Error", "Please select a turn generation mode.")

# Creating the main window
root = tk.Tk()
root.title("Turn Generator for Oral Exams")

# Set the window size
root.geometry("500x400")

# Label for the selection
label = tk.Label(root, text="Choose turn generation mode:")
label.pack(pady=10)

# Variable for the choice (individual turns or groups)
var_choice = tk.StringVar()
var_choice.set("individual")  # Set the default value to "individual"

# Radio button for individual turns
radio_individual = tk.Radiobutton(root, text="Individual Turns", variable=var_choice, value="individual")
radio_individual.pack()

# Radio button for groups
radio_groups = tk.Radiobutton(root, text="Groups", variable=var_choice, value="groups")
radio_groups.pack()

# Label and input field for the number of students per group
label_groups = tk.Label(root, text="Number of students per group:")
label_groups.pack(pady=5)

entry_groups = tk.Entry(root)
entry_groups.pack(pady=5)

# Button to generate the turns
button_generate = tk.Button(root, text="Generate Turns", command=generate_turns)
button_generate.pack(pady=20)

# Text area to display the generated turns or groups
text_output = tk.Text(root, width=50, height=10)
text_output.pack(pady=10)

# Run the window
root.mainloop()
