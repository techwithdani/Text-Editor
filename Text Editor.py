import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Function to open a file and display its content in the text editor
def open_file(window, text_edit):
    # Prompt user to select a text file
    path = askopenfilename(filetypes=[("Text Files", "*.txt")])

    # Check if a file was selected
    if not path:
        return
    
    # Clear the text editor
    text_edit.delete(1.0, tk.END)
    
    # Open the selected file and read its content
    with open(path, "r") as f:
        content = f.read()
         # Insert the content into the text editor
        text_edit.insert(tk.END, content)
        
    window.title(f"Open file: {path}")
    
# Function to save the content of the text editor to a file
def save_file(window, text_edit):
    # Prompt user to select a location to save the file
    path = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

     # Check if a location was selected
    if not path:
        return
    
    # Write the content to the selected file
    with open(path, "w") as f:
         # Get the content of the text editor
        content = text_edit.get(1.0, tk.END)
        f.write(content)
        
    window.title(f"Open file: {path}")
    
# Main function to set up the GUI application
def main():
    # Create the main window
    WINDOW = tk.Tk()
    WINDOW.title("Text Editor")

    # Configure layout: row 0 has a minimum size of 500, column 1 has a minimum size of 600
    WINDOW.rowconfigure(0, minsize=500)
    WINDOW.columnconfigure(1, minsize=600)

    # Create a text widget for editing text
    text = tk.Text(WINDOW, font="Helvetica 24")
    text.grid(row=0, column=1)

    # Create a frame for holding buttons
    frame = tk.Frame(WINDOW, relief=tk.RAISED, bd=5)
    # Create a Save button and associate it with the save_file function
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(WINDOW, text))
    # Create an Open button and associate it with the open_file function
    open_buttton = tk.Button(frame, text="Open", command=lambda: open_file(WINDOW, text))

    # Place Save and open button in the frame
    save_button.grid(row=0, column=0, padx=8, pady=8, sticky="ew")
    open_buttton.grid(row=1, column=0, padx=8, pady=8, sticky="ew")
    frame.grid(row=0, column=2, sticky="ns")

    # Bind keyboard shortcuts to respective functions
    WINDOW.bind("<Control-s>", lambda s: save_file(WINDOW, text))
    WINDOW.bind("<Control-o>", lambda o: open_file(WINDOW, text))

    WINDOW.mainloop()

if __name__ == "__main__":
    main()