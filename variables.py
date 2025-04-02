import tkinter as tk
from tkinter import messagebox

class PetFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TailTrail - Pet Finder")
        self.root.geometry("500x400")
        

        self.pets = []
        
       
        self.create_widgets()
    
    def create_widgets(self):
      
        tk.Label(self.root, text="Lost Pet Finder", font=('Arial', 20)).pack(pady=10)
        
       
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)
        
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Button(search_frame, text="Search", command=self.search_pets).pack(side=tk.LEFT)
        
        # Results Display
        self.results_text = tk.Text(self.root, height=10, width=50)
        self.results_text.pack(pady=10)
        
        # Report Frame
        report_frame = tk.Frame(self.root)
        report_frame.pack(pady=10)
        
        tk.Button(report_frame, text="Report Lost Pet", command=self.show_report_form).pack()
    
    def search_pets(self):
        search_term = self.search_entry.get().lower()
        self.results_text.delete(1.0, tk.END)
        
        if not search_term:
            self.results_text.insert(tk.END, "Please enter a search term")
            return
            
        found_pets = [pet for pet in self.pets 
                     if search_term in pet["name"].lower() 
                     or search_term in pet["breed"].lower()]
        
        if not found_pets:
            self.results_text.insert(tk.END, "No matching pets found")
        else:
            for pet in found_pets:
                self.results_text.insert(tk.END, 
                                       f"Name: {pet['name']}\n"
                                       f"Breed: {pet['breed']}\n"
                                       f"Color: {pet['color']}\n"
                                       f"Location: {pet['location']}\n\n")
    
    def show_report_form(self):
        
        form_window = tk.Toplevel(self.root)
        form_window.title("Report Lost Pet")
        
       
        tk.Label(form_window, text="Pet Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(form_window, width=30)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_window, text="Breed:").grid(row=1, column=0, padx=5, pady=5)
        breed_entry = tk.Entry(form_window, width=30)
        breed_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(form_window, text="Color:").grid(row=2, column=0, padx=5, pady=5)
        color_entry = tk.Entry(form_window, width=30)
        color_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(form_window, text="Last Seen Location:").grid(row=3, column=0, padx=5, pady=5)
        location_entry = tk.Entry(form_window, width=30)
        location_entry.grid(row=3, column=1, padx=5, pady=5)
        
        def submit_form():
           
            new_pet = {
                "name": name_entry.get(),
                "breed": breed_entry.get(),
                "color": color_entry.get(),
                "location": location_entry.get()
            }
            
           
            if not all(new_pet.values()):
                messagebox.showerror("Error", "Please fill all fields")
                return
                
            self.pets.append(new_pet)
            messagebox.showinfo("Success", f"{new_pet['name']} has been reported!")
            form_window.destroy()
        
        tk.Button(form_window, text="Submit", command=submit_form).grid(row=4, columnspan=2, pady=10)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PetFinderApp(root)
    root.mainloop()
