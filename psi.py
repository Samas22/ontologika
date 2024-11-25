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

# Example usage
if __name__ == "__main__":
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

    treatment_app = PsychologicalTreatment()
    treatment_app.add_disorder(depression)
    treatment_app.add_disorder(anxiety)

    disorder_name = "Depression"
    print(f"Treatments for {disorder_name}: {treatment_app.get_treatment(disorder_name)}")
    print(f"Medications for {disorder_name}: {treatment_app.get_medications(disorder_name)}")

    disorder_name = "Anxiety"
    print(f"Treatments for {disorder_name}: {treatment_app.get_treatment(disorder_name)}")
    print(f"Medications for {disorder_name}: {treatment_app.get_medications(disorder_name)}")
