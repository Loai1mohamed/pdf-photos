import tkinter as tk
from tkinter import filedialog
from PIL import Image


class ImageToPDFConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Image to PDF Converter")
        self.image_path = None

        # Create widgets
        self.image_label = tk.Label(self.master, text="No image selected")
        self.image_label.pack()

        self.select_button = tk.Button(self.master, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=10)

        self.convert_button = tk.Button(self.master, text="Convert to PDF", command=self.convert_image_to_pdf)
        self.convert_button.pack()

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if self.image_path:
            self.image_label.configure(text=self.image_path)

    def convert_image_to_pdf(self):
        if not self.image_path:
            return

        image = Image.open(self.image_path)
        pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if pdf_path:
            image.save(pdf_path, "PDF", resolution=100.0)
            tk.messagebox.showinfo("Success", "Image converted to PDF")


if __name__ == "__main__":
    root = tk.Tk()
    converter = ImageToPDFConverter(root)
    root.mainloop()