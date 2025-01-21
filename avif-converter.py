import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def get_unique_filename(output_folder, base_name, extension):
    """
    Generates a unique filename by appending (copy #) if the file already exists.
    """
    counter = 1
    unique_name = base_name + extension
    while os.path.exists(os.path.join(output_folder, unique_name)):
        unique_name = f"{base_name} (copy {counter}){extension}"
        counter += 1
    return unique_name

def convert_images_to_avif(input_folder, output_folder, quality, progress_bar, status_label):
    """
    Converts all images in the input folder to AVIF format using ImageMagick.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Supported image extensions
    supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp')

    # Get list of images to convert
    images = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_extensions)]
    total_images = len(images)

    if total_images == 0:
        messagebox.showwarning("No Images", "No supported images found in the input folder.")
        return

    # Initialize progress bar
    progress_bar["maximum"] = total_images
    progress_bar["value"] = 0

    # Iterate over all files in the input folder
    for i, filename in enumerate(images):
        # Update status label
        status_label.config(text=f"Converting {filename} ({i + 1}/{total_images})")
        root.update_idletasks()  # Refresh the GUI

        # Construct base name and extension
        base_name, extension = os.path.splitext(filename)
        output_extension = ".avif"

        # Generate a unique output filename
        unique_output_name = get_unique_filename(output_folder, base_name, output_extension)
        output_path = os.path.join(output_folder, unique_output_name)

        # Construct input path
        input_path = os.path.join(input_folder, filename)

        # Use ImageMagick to convert the image
        try:
            subprocess.run(
                [
                    "magick",
                    input_path,
                    "-quality",
                    str(quality),
                    output_path,
                ],
                check=True,
            )
            print(f"Converted {filename} to {unique_output_name}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to convert {filename}: {e}")

        # Update progress bar
        progress_bar["value"] = i + 1
        root.update_idletasks()  # Refresh the GUI

    # Show completion message
    status_label.config(text="Conversion complete!")
    messagebox.showinfo("Conversion Complete", "All images have been converted to AVIF!")

def select_input_folder():
    folder = filedialog.askdirectory()
    input_folder_var.set(folder)

def select_output_folder():
    folder = filedialog.askdirectory()
    output_folder_var.set(folder)

def start_conversion():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    quality = quality_var.get()

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders.")
        return

    # Reset progress bar and status label
    progress_bar["value"] = 0
    status_label.config(text="Starting conversion...")
    root.update_idletasks()  # Refresh the GUI

    # Start conversion
    convert_images_to_avif(input_folder, output_folder, quality, progress_bar, status_label)

# Create the main window
root = tk.Tk()
root.title("AVIF Converter")

# Variables to store folder paths and quality
input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()
quality_var = tk.IntVar(value=60)

# GUI Layout
tk.Label(root, text="Input Folder:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_folder_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_input_folder).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Output Folder:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_folder_var, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="Quality (0-100):").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=quality_var, width=10).grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.grid(row=3, column=0, columnspan=3, pady=10)

# Status label
status_label = tk.Label(root, text="Ready", fg="blue")
status_label.grid(row=4, column=0, columnspan=3, pady=10)

# Convert button
tk.Button(root, text="Convert to AVIF", command=start_conversion).grid(row=5, column=1, pady=20)

# Run the application
root.mainloop()