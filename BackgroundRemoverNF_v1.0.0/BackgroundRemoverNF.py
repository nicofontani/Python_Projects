# """
# ******************************************************************************/ 
# *                                                                            *
# *                           Background Remover Tool                          *
# *                                                                            *
# * DESCRIPTION:                                                               *
# * This program allows the user to remove the background from images using    *
# * the Rembg library. It features a graphical user interface (GUI) built with *
# * Tkinter. The user can select an input image file, specify the output path, *
# * and remove the background with a click of a button.                        *
# *                                                                            *
# * Copyright (c) 2024, Nico Fontani                                           *
# * Creation Date: 10 Nov 2024                                                 *
# *                                                                            *
# * Original Author: Nico Fontani                                              *
# * Last Modified: 13 Nov 2024                                                 *
# *                                                                            *
# * Supported by Python, Tkinter, Rembg, and Pillow                            *
# *                                                                            *
# ******************************************************************************/
# """

import tkinter as tk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image
import os

def select_input_file():
    """Open file dialog to select the input image."""
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Images", "*.png;*.jpg;*.jpeg")]
    )
    input_path_entry.delete(0, tk.END)
    input_path_entry.insert(0, file_path)

def select_output_file():
    """Open file dialog to select where to save the output image."""
    file_path = filedialog.asksaveasfilename(
        title="Select where to save the image with no background",
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")]
    )
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, file_path)

def remove_background():
    """Remove the background from the selected image."""
    input_path = input_path_entry.get()
    output_path = output_path_entry.get()

    if not input_path or not output_path:
        messagebox.showerror("Error", "Please specify both input and output paths.")
        return

    try:
        # Read the input image and remove the background
        with open(input_path, "rb") as input_file:
            input_image = input_file.read()
            output_image = remove(input_image)

        # Write the output image to the specified file
        with open(output_path, "wb") as output_file:
            output_file.write(output_image)

        messagebox.showinfo("Success", "Background removed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the GUI window
app = tk.Tk()
app.title("Background Remover NF")
app.geometry("800x700")
app.resizable(True, True)

# Label and Entry for input image path
tk.Label(app, text="Input Image Path:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
input_path_entry = tk.Entry(app, width=40)
input_path_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_input_file).grid(row=0, column=2, padx=5)

# Label and Entry for output image path
tk.Label(app, text="Output Image Path:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
output_path_entry = tk.Entry(app, width=40)
output_path_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_output_file).grid(row=1, column=2, padx=5)

# Button to remove the background
download_button = tk.Button(app, text="Download", command=remove_background)
download_button.grid(row=2, column=1, pady=20)

# Start the application
app.protocol("WM_DELETE_WINDOW", app.destroy)  # Allow closing the window with the 'X' button
app.mainloop()
