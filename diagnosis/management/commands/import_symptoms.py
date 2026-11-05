from django.core.management.base import BaseCommand
from diagnosis.models import Symptom

class Command(BaseCommand):
    help = 'Import symptoms into the database'

    def handle(self, *args, **kwargs):
        symptoms = [
            "Abdominal pain", "Abdominal swelling", "Acidity", "Aching muscles",
            "Back pain", "Bloating", "Blurred vision", "Bone pain", "Chest pain",
            "Chills", "Chronic cough", "Constipation", "Cough", "Dehydration",
            "Delirium", "Diarrhea", "Difficulty breathing", "Difficulty swallowing",
            "Dizziness", "Dry mouth", "Earache", "Excessive sweating", "Fatigue",
            "Fever", "Flatulence", "Frequent urination", "Headache", "Heartburn",
            "Heart palpitations", "Hoarseness", "Insomnia", "Irritability", "Joint pain",
            "Lack of appetite", "Lethargy", "Loss of balance", "Loss of consciousness",
            "Memory loss", "Mood swings", "Muscle cramps", "Nausea", "Night sweats",
            "Nosebleeds", "Pain during urination", "Painful periods", "Pale skin",
            "Rapid heartbeat", "Rash", "Red eyes", "Runny nose", "Shortness of breath",
            "Skin itchiness", "Sleepiness", "Sneezing", "Sore throat", "Stiff neck",
            "Stomach cramps", "Sweating", "Swelling", "Tiredness", "Tremors",
            "Unexplained weight loss", "Unusual bruising", "Unusual bleeding",
            "Vision changes", "Vomiting", "Waking up at night", "Weakness", "Wheezing",
            "Abnormal heart rate", "Anxiety", "Blisters", "Change in bowel habits",
            "Confusion", "Dry skin", "Excessive thirst", "Hair loss", "Increased sensitivity to temperature",
            "Increased thirst", "Itchy eyes", "Lumps", "Menstrual irregularities", "Muscle weakness",
            "Numbness or tingling", "Painful joints", "Skin discoloration", "Speech difficulties",
            "Swollen lymph nodes", "Tinnitus (ringing in the ears)", "Urinary incontinence",
            "Vision loss", "Weight gain", "Abnormal movements", "Allergic reactions",
            "Blood in stool", "Frequent headaches", "Seizures", "Swollen abdomen", "Tenderness"
        ]

        for symptom in symptoms:
            Symptom.objects.get_or_create(name=symptom)
            self.stdout.write(self.style.SUCCESS(f'Successfully added symptom: {symptom}'))

