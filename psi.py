import tkinter as tk
from tkinter import messagebox

class Disorder:
    def __init__(self, name, treatments, medications):
        self.name = name
        self.treatments = treatments
        self.medications = medications

class PsychologicalTreatment:
    def __init__(self):
        self.disorders = []

    def add_disorder(self, disorder):
        self.disorders.append(disorder)

    def get_treatment(self, disorder_name):
        for disorder in self.disorders:
            if disorder.name == disorder_name:
                return disorder.treatments
        return "No treatments found for this disorder"

    def get_medications(self, disorder_name):
        for disorder in self.disorders:
            if disorder.name == disorder_name:
                return disorder.medications
        return "No medications found for this disorder"

# GUI Application
class TreatmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Psychological Treatment App")
        
        self.treatment_app = PsychologicalTreatment()
        self.setup_disorders()
        
        self.disorder_label = tk.Label(root, text="Enter Disorder Name:")
        self.disorder_label.pack()
        self.disorder_entry = tk.Entry(root)
        self.disorder_entry.pack()
        
        self.treatment_button = tk.Button(root, text="Get Treatments", command=self.show_treatments)
        self.treatment_button.pack()
        
        self.medication_button = tk.Button(root, text="Get Medications", command=self.show_medications)
        self.medication_button.pack()
        
    def setup_disorders(self):
        depression = Disorder(
            "Depression",
            ["Cognitive Behavioral Therapy", "Interpersonal Therapy"],
            ["SSRIs", "SNRIs", "Tricyclic Antidepressants"]
        )
        anxiety = Disorder(
            "Anxiety",
            ["Cognitive Behavioral Therapy", "Exposure Therapy"],
            ["Benzodiazepines", "SSRIs"]
        )
        self.treatment_app.add_disorder(depression)
        self.treatment_app.add_disorder(anxiety)
        
    def show_treatments(self):
        disorder_name = self.disorder_entry.get()
        treatments = self.treatment_app.get_treatment(disorder_name)
        messagebox.showinfo("Treatments", f"Treatments for {disorder_name}: {treatments}")
        
    def show_medications(self):
        disorder_name = self.disorder_entry.get()
        medications = self.treatment_app.get_medications(disorder_name)
        messagebox.showinfo("Medications", f"Medications for {disorder_name}: {medications}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TreatmentApp(root)
    root.mainloop()
