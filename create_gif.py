import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import imageio.v3 as iio
import os

class GifApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Team GIF Generator")
        self.root.geometry("700x500")
        self.root.configure(bg="#f9fafb")
        
        self.images = []
        self.file_paths = []

        # Title
        self.title_label = tk.Label(root, text="🌀 Team GIF Generator", font=("Segoe UI", 18, "bold"), bg="#f9fafb", fg="#4F46E5")
        self.title_label.pack(pady=10)

        # Select button
        self.select_button = tk.Button(root, text="📂 Select Images", font=("Segoe UI", 12), command=self.select_images, bg="#6366F1", fg="white")
        self.select_button.pack(pady=10)

        # Image preview
        self.preview_frame = tk.Frame(root, bg="#f9fafb")
        self.preview_frame.pack(pady=10)

        # Generate button
        self.generate_button = tk.Button(root, text="🎬 Generate GIF", font=("Segoe UI", 12), command=self.generate_gif, bg="#22C55E", fg="white")
        self.generate_button.pack(pady=20)

    def select_images(self):
        self.file_paths = filedialog.askopenfilenames(
            title="Select PNG images",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.webp")]
        )

        self.images.clear()

        for widget in self.preview_frame.winfo_children():
            widget.destroy()

        for file in self.file_paths:
            try:
                img = Image.open(file)
                img.thumbnail((120, 120))
                photo = ImageTk.PhotoImage(img)
                label = tk.Label(self.preview_frame, image=photo, bg="#f9fafb")
                label.image = photo  # keep a reference
                label.pack(side=tk.LEFT, padx=5)
                self.images.append(iio.imread(file))
            except Exception as e:
                print(f"Error loading image: {file} - {e}")

    def generate_gif(self):
        if not self.images:
            messagebox.showwarning("No Images", "Please select images first.")
            return

        try:
            iio.imwrite("team.gif", self.images, duration=600, loop=0)
            messagebox.showinfo("GIF Created", "🎉 team.gif has been successfully created!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create GIF: {e}")

# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = GifApp(root)
    root.mainloop()
