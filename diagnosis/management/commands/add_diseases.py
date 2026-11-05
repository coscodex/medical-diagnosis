from django.core.management.base import BaseCommand
from diagnosis.models import Symptom, Disease

class Command(BaseCommand):
    help = 'Add common diseases and their associated symptoms to the database'

    def handle(self, *args, **kwargs):
        # List of diseases and their associated symptoms
        diseases_data = [
            {
                "name": "Diabetes",
                "symptoms": ["Increased thirst", "Frequent urination", "Extreme hunger", "Fatigue", "Blurred vision"],
                "suggested_medicine": "Metformin",
                "description": "A chronic condition that occurs when the body cannot produce enough insulin."
            },
            {
                "name": "Hypertension",
                "symptoms": ["Headaches", "Shortness of breath", "Nosebleeds", "Flushing", "Dizziness"],
                "suggested_medicine": "Lisinopril",
                "description": "A condition in which the force of the blood against the artery walls is too high."
            },
            {
                "name": "Asthma",
                "symptoms": ["Wheezing", "Shortness of breath", "Chest tightness", "Coughing", "Difficulty sleeping"],
                "suggested_medicine": "Albuterol",
                "description": "A condition in which your airways narrow and swell and may produce extra mucus."
            },
            {
                "name": "Heart Disease",
                "symptoms": ["Chest pain", "Shortness of breath", "Fatigue", "Irregular heartbeat", "Swelling in legs/feet"],
                "suggested_medicine": "Aspirin",
                "description": "A range of conditions that affect your heart, including blood vessel diseases."
            },
            {
                "name": "Breast Cancer",
                "symptoms": ["Lumps in the breast", "Changes in breast shape", "Nipple discharge", "Skin changes", "Swelling"],
                "suggested_medicine": "Chemotherapy",
                "description": "A disease in which abnormal cells divide without control."
            },
            {
                "name": "Chronic Obstructive Pulmonary Disease (COPD)",
                "symptoms": ["Shortness of breath", "Chronic cough", "Wheezing", "Chest tightness", "Frequent respiratory infections"],
                "suggested_medicine": "Bronchodilators",
                "description": "A group of lung diseases that block airflow and make it difficult to breathe."
            },
            {
                "name": "Gastroesophageal Reflux Disease (GERD)",
                "symptoms": ["Heartburn", "Regurgitation", "Chest pain", "Difficulty swallowing", "Chronic cough"],
                "suggested_medicine": "Proton pump inhibitors",
                "description": "A chronic digestive condition where stomach acid or bile irritates the food pipe lining."
            },
            {
                "name": "Kidney Disease",
                "symptoms": ["Swelling in legs/ankles", "Fatigue", "Nausea", "Changes in urination", "High blood pressure"],
                "suggested_medicine": "Diuretics",
                "description": "A disease affecting kidney function, leading to waste buildup in the body."
            },
            {
                "name": "Influenza (Flu)",
                "symptoms": ["Fever", "Chills", "Cough", "Sore throat", "Body aches"],
                "suggested_medicine": "Antiviral medications",
                "description": "A contagious respiratory illness caused by influenza viruses."
            },
            {
                "name": "Allergies",
                "symptoms": ["Sneezing", "Itchy eyes", "Runny nose", "Skin rashes", "Swelling"],
                "suggested_medicine": "Antihistamines",
                "description": "An immune response to a foreign substance that's typically harmless."
            },
            {
                "name": "Osteoarthritis",
                "symptoms": ["Joint pain", "Stiffness", "Swelling", "Reduced range of motion", "Crepitus"],
                "suggested_medicine": "NSAIDs",
                "description": "A degenerative joint disease that occurs when the cartilage that cushions the joints breaks down."
            },
            {
                "name": "Rheumatoid Arthritis",
                "symptoms": ["Joint pain", "Swelling", "Morning stiffness", "Fatigue", "Fever"],
                "suggested_medicine": "DMARDs",
                "description": "An autoimmune disorder that primarily affects joints."
            },
            {
                "name": "Depression",
                "symptoms": ["Persistent sadness", "Loss of interest", "Fatigue", "Changes in sleep/appetite", "Difficulty concentrating"],
                "suggested_medicine": "Antidepressants",
                "description": "A mood disorder that causes a persistent feeling of sadness and loss of interest."
            },
            {
                "name": "Anxiety Disorders",
                "symptoms": ["Excessive worry", "Restlessness", "Fatigue", "Irritability", "Difficulty concentrating"],
                "suggested_medicine": "Antidepressants",
                "description": "A group of mental disorders characterized by significant feelings of anxiety and fear."
            },
            {
                "name": "Tuberculosis (TB)",
                "symptoms": ["Persistent cough", "Chest pain", "Coughing up blood", "Fatigue", "Weight loss"],
                "suggested_medicine": "Antitubercular medications",
                "description": "A potentially serious infectious disease that primarily affects the lungs."
            },
            {
                "name": "Chronic Sinusitis",
                "symptoms": ["Facial pain", "Nasal congestion", "Difficulty breathing through the nose", "Loss of smell", "Cough"],
                "suggested_medicine": "Nasal corticosteroids",
                "description": "Inflammation of the sinuses that lasts longer than 12 weeks."
            },
            {
                "name": "Skin Conditions (Eczema)",
                "symptoms": ["Dry skin", "Itching", "Red/irritated skin", "Thickened skin", "Skin lesions"],
                "suggested_medicine": "Topical corticosteroids",
                "description": "A condition that makes your skin red and itchy."
            },
            {
                "name": "Malaria",
                "symptoms": ["Fever", "Chills", "Sweating", "Fatigue", "Headaches"],
                "suggested_medicine": "Antimalarial medications",
                "description": "A disease caused by parasites transmitted through the bites of infected mosquitoes."
            },
            {
                "name": "Hepatitis",
                "symptoms": ["Fatigue", "Nausea", "Abdominal pain", "Loss of appetite", "Jaundice"],
                "suggested_medicine": "Antivirals",
                "description": "An inflammatory condition of the liver."
            },
            {
                "name": "Gout",
                "symptoms": ["Intense joint pain", "Lingering discomfort", "Inflammation and redness", "Limited range of motion", "Sudden attacks"],
                "suggested_medicine": "Colchicine",
                "description": "A form of arthritis characterized by severe pain, redness, and tenderness in joints."
            },
            {
                "name": "HIV/AIDS",
                "symptoms": ["Fever", "Fatigue", "Rash", "Night sweats", "Swollen lymph nodes"],
                "suggested_medicine": "Antiretroviral therapy",
                "description": "A chronic condition that damages the immune system."
            },
            {
                "name": "Diarrhea",
                "symptoms": ["Loose or watery stools", "Abdominal cramps", "Nausea", "Urgent need to use the bathroom", "Dehydration"],
                "suggested_medicine": "Loperamide",
                "description": "A condition characterized by frequent loose or liquid bowel movements."
            },
            {
                "name": "Dengue Fever",
                "symptoms": ["High fever", "Severe headache", "Pain behind the eyes", "Joint and muscle pain", "Rash"],
                "suggested_medicine": "Supportive care",
                "description": "A mosquito-borne viral infection causing severe flu-like symptoms."
            },
        ]

        for disease_data in diseases_data:
            # Create or get the symptoms
            symptoms = []
            for symptom_name in disease_data["symptoms"]:
                symptom, created = Symptom.objects.get_or_create(name=symptom_name)
                symptoms.append(symptom)

            # Create the disease
            disease, created = Disease.objects.get_or_create(
                name=disease_data["name"],
                suggested_medicine=disease_data["suggested_medicine"],
                description=disease_data["description"]
            )
            disease.symptoms.set(symptoms)  # Associate symptoms with the disease
            disease.save()

        self.stdout.write(self.style.SUCCESS('Successfully added diseases and their symptoms'))

