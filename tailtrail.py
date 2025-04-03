import tkinter as tk
from tkinter import messagebox

class PetFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Finder")
        self.root.geometry("500x500")
        
        # Store pets (simplified for now)
        self.lost_pets = []  
        self.found_pets = []
        
        # Basic form setup
        self.setup_upload_form()
    
    def setup_upload_form(self):
        """Your primary focus - the upload form"""
        # Form frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=20)
        
        # Type selection (Lost/Found)
        tk.Label(self.form_frame, text="Report Type:").grid(row=0, column=0, sticky="e")
        self.report_type = tk.StringVar(value="lost")
        tk.Radiobutton(self.form_frame, text="Lost Pet", variable=self.report_type, value="lost").grid(row=0, column=1)
        tk.Radiobutton(self.form_frame, text="Found Pet", variable=self.report_type, value="found").grid(row=0, column=2)
        
        # Basic fields
        fields = [
            ("Name:", "name"),
            ("Species:", "species"),
            ("Breed:", "breed"),
            ("Color:", "color"),
            ("Location:", "location"),
            ("Your Phone:", "phone")
        ]
        
        self.entries = {}  # Stores all entry widgets
        
        for i, (label, field) in enumerate(fields, start=1):
            tk.Label(self.form_frame, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(self.form_frame, width=30)
            entry.grid(row=i, column=1, columnspan=2, padx=5, pady=5)
            self.entries[field] = entry
        
        # Submit button
        tk.Button(self.form_frame, text="Submit", 
                 command=self.submit_form,
                 bg="#4CAF50", fg="white").grid(row=len(fields)+1, columnspan=3, pady=10)
    
    def submit_form(self):
        """Handle form submission (basic validation)"""
        # Get all entered data
        pet_data = {
            "type": self.report_type.get(),
            "name": self.entries["name"].get(),
            "species": self.entries["species"].get(),
            "breed": self.entries["breed"].get(),
            "color": self.entries["color"].get(),
            "location": self.entries["location"].get(),
            "contact": self.entries["phone"].get()
        }
        
        # Simple validation
        if not pet_data["name"] or not pet_data["location"]:
            messagebox.showerror("Error", "Name and Location are required!")
            return
        
        # Store in the appropriate list
        if pet_data["type"] == "lost":
            self.lost_pets.append(pet_data)
        else:
            self.found_pets.append(pet_data)
        
        messagebox.showinfo("Success", f"{pet_data['name']} reported as {pet_data['type']}!")
        self.clear_form()
    
    def clear_form(self):
        """Reset all fields"""
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.report_type.set("lost")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PetFinderApp(root)
    root.mainloop()