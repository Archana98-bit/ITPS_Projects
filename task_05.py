import json
import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['phone'], data['email'])


class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        return self.contacts

    def update_contact(self, name, new_contact):
        for contact in self.contacts:
            if contact.name == name:
                contact.name = new_contact.name
                contact.phone = new_contact.phone
                contact.email = new_contact.email
                self.save_contacts()
                return True
        return False

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        self.save_contacts()

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                contacts_data = json.load(file)
                return [Contact.from_dict(data) for data in contacts_data]
        except FileNotFoundError:
            return []


class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contact_book = ContactBook()

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, height=15, width=50)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical")
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=10)

        self.view_button = tk.Button(self.button_frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=0, column=1, padx=10)

        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=0, column=2, padx=10)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=0, column=3, padx=10)

        self.view_contacts()

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter name:")
        phone = simpledialog.askstring("Input", "Enter phone:")
        email = simpledialog.askstring("Input", "Enter email:")
        if name and phone and email:
            contact = Contact(name, phone, email)
            self.contact_book.add_contact(contact)
            self.view_contacts()

    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        contacts = self.contact_book.view_contacts()
        for contact in contacts:
            self.listbox.insert(tk.END, f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def update_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a contact to update")
            return
        name = self.listbox.get(selected).split(", ")[0].split(": ")[1]
        new_name = simpledialog.askstring("Input", "Enter new name:")
        new_phone = simpledialog.askstring("Input", "Enter new phone:")
        new_email = simpledialog.askstring("Input", "Enter new email:")
        if new_name and new_phone and new_email:
            new_contact = Contact(new_name, new_phone, new_email)
            if self.contact_book.update_contact(name, new_contact):
                self.view_contacts()
            else:
                messagebox.showerror("Error", "Contact not found")

    def delete_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a contact to delete")
            return
        name = self.listbox.get(selected).split(", ")[0].split(": ")[1]
        self.contact_book.delete_contact(name)
        self.view_contacts()


root = tk.Tk()
app = ContactBookApp(root)
root.mainloop()
