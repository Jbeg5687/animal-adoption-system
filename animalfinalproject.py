import tkinter as tk
from tkinter import messagebox, simpledialog 

class Species:
    def __init__(self):
        self.species_options = ("Dog", "Cat", "Bird", "Reptile", "Other")
    def get_species(self):
        return self.species_options

class MedicalRecord:
    def __init__(self, animal_id):
        self.animal_id = animal_id
        self.medical_history = []
    def add_record(self, record):
        self.medical_history.append(record)
    def get_history(self):
        return self.medical_history

class AdoptionStatus:
    def __init__(self):
        self.status_map = {}
    def update_status(self, animal_id, status):
        self.status_map[animal_id] = status
    def get_status(self, animal_id):
        return self.status_map.get(animal_id, "Adoptable")  

class Animal:
    def __init__(self, animal_id, name, species, age):
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.age = age
        self.medical_record = MedicalRecord(animal_id)
        self.adoption_status = "Adoptable" 
    def update_medical_record(self, record):
        self.medical_record.add_record(record)
    def check_adoption_status(self):
        return self.adoption_status
    def display_info(self):
        return (f"Animal ID: {self.animal_id}\n"
                f"Name: {self.name}\n"
                f"Species: {self.species}\n"
                f"Age: {self.age}\n"
                f"Adoption Status: {self.adoption_status}\n"
                f"Medical Records: {self.medical_record.get_history()}\n")

class AnimalManagementApp:
    def __init__(self, root):
        self.animals = []
        self.species = Species()
        self.adoption_status = AdoptionStatus()
        self.animal_id_counter = 1
        self.selected_animal_index = None
        root.title("Animal Shelter")
        root.geometry("500x500")
        root.configure(bg="#E0BBE4")  
        font_style = ("Comic Sans MS", 12)
        button_font = ("Comic Sans MS", 10)
        input_frame = tk.Frame(root, bg="#E0BBE4")
        input_frame.pack(pady=10)
        self.label_name = tk.Label(input_frame, text="Animal Name:", bg="#E0BBE4", font=font_style)
        self.label_name.grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(input_frame, font=font_style)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)
        self.label_species = tk.Label(input_frame, text="Species:", bg="#E0BBE4", font=font_style)
        self.label_species.grid(row=1, column=0, padx=5, pady=5)
        self.species_var = tk.StringVar()
        self.species_var.set(self.species.get_species()[0])
        self.species_menu = tk.OptionMenu(input_frame, self.species_var, *self.species.get_species())
        self.species_menu.config(font=font_style)
        self.species_menu.grid(row=1, column=1, padx=5, pady=5)
        self.label_age = tk.Label(input_frame, text="Age:", bg="#E0BBE4", font=font_style)
        self.label_age.grid(row=2, column=0, padx=5, pady=5)
        self.entry_age = tk.Entry(input_frame, font=font_style)
        self.entry_age.grid(row=2, column=1, padx=5, pady=5)
        self.label_medical = tk.Label(input_frame, text="Medical Record:", bg="#E0BBE4", font=font_style)
        self.label_medical.grid(row=3, column=0, padx=5, pady=5)
        self.entry_medical = tk.Entry(input_frame, font=font_style)
        self.entry_medical.grid(row=3, column=1, padx=5, pady=5)
        self.label_adoption = tk.Label(input_frame, text="Adoption Status:", bg="#E0BBE4", font=font_style)
        self.label_adoption.grid(row=4, column=0, padx=5, pady=5)
        self.entry_adoption = tk.Entry(input_frame, font=font_style)
        self.entry_adoption.grid(row=4, column=1, padx=5, pady=5)
        button_frame = tk.Frame(root, bg="#E0BBE4")
        button_frame.pack(pady=10)
        self.button_add = tk.Button(button_frame, text="Add Animal", command=self.add_animal, bg="#957DAD", font=button_font)
        self.button_add.grid(row=0, column=0, padx=10, pady=10)
        self.button_update = tk.Button(button_frame, text="Update Animal", command=self.update_animal, bg="#957DAD", font=button_font)
        self.button_update.grid(row=0, column=1, padx=10, pady=10)
        self.button_delete = tk.Button(button_frame, text="Delete Animal", command=self.delete_animal, bg="#957DAD", font=button_font)
        self.button_delete.grid(row=0, column=2, padx=10, pady=10)
        self.button_view = tk.Button(button_frame, text="View All Animals", command=self.view_animals, bg="#957DAD", font=button_font)
        self.button_view.grid(row=0, column=3, padx=10, pady=10)
    def add_animal(self):
        name = self.entry_name.get()
        species = self.species_var.get()
        age = self.entry_age.get()
        medical = self.entry_medical.get()
        adoption = self.entry_adoption.get()
        if not name or not species or not age:
            messagebox.showerror("Input Error", "Please fill out all fields")
            return
        new_animal = Animal(self.animal_id_counter, name, species, int(age))
        if medical:
            new_animal.update_medical_record(medical)
        if adoption:
            new_animal.adoption_status = adoption
            self.adoption_status.update_status(self.animal_id_counter, adoption)
        self.animals.append(new_animal)
        self.animal_id_counter += 1
        self.clear_inputs()
        messagebox.showinfo("Success", "Animal added successfully!")
    def clear_inputs(self):
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_medical.delete(0, tk.END)
        self.entry_adoption.delete(0, tk.END)
    def view_animals(self):
        if not self.animals:
            messagebox.showinfo("No Animals", "No animals added yet.")
            return
        animal_info = "\n\n".join(f"ID {i+1}: {animal.display_info()}" for i, animal in enumerate(self.animals))
        top = tk.Toplevel()
        top.title("All Animals")
        top.configure(bg="#E0BBE4")
        label = tk.Label(top, text=animal_info, bg="#E0BBE4", font=("Comic Sans MS", 10))
        label.pack()
    def ask_integer_with_retry(self, prompt):
        while True:
            try:
                value = simpledialog.askstring("Input", prompt)
                if value == "":
                    return None  
                return int(value)  
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid integer.")
    def update_animal(self):
        name = simpledialog.askstring("Update Animal", "Enter Animal Name to update:")
        animal = self.get_animal_by_name(name)
        if not animal:
            messagebox.showerror("Error", "Animal not found!")
            return
        new_name = simpledialog.askstring("Update Animal", "Enter new name (leave blank for no change):")
        new_species = simpledialog.askstring("Update Animal", "Enter new species (leave blank for no change):")
        age = self.ask_integer_with_retry("Enter new age (leave blank for no change):")
        if age is None:
            age = animal.age  
        medical = simpledialog.askstring("Update Animal", "Enter new medical record (leave blank for no change):")
        adoption = simpledialog.askstring("Update Animal", "Enter new adoption status (leave blank for no change):")
        if new_name:
            animal.name = new_name
        if new_species:
            animal.species = new_species
        animal.age = age  
        if medical:
            animal.update_medical_record(medical)
        if adoption:
            animal.adoption_status = adoption
            self.adoption_status.update_status(animal.animal_id, adoption)

        messagebox.showinfo("Success", "Animal updated successfully!")

    def delete_animal(self):
        name = simpledialog.askstring("Delete Animal", "Enter Animal Name to delete:")
        animal = self.get_animal_by_name(name)
        if not animal:
            messagebox.showerror("Error", "Animal not found!")
            return

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {animal.name}?")
        if confirm:
            self.animals.remove(animal)
            messagebox.showinfo("Success", "Animal deleted successfully!")

    def get_animal_by_name(self, name):
        for animal in self.animals:
            if animal.name.lower() == name.lower():  
                return animal
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimalManagementApp(root)
    root.mainloop()
