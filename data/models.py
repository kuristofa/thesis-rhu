from django.db import models
from django.utils import timezone
from django.db.models.deletion import CASCADE

SEX_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

BARANGAY_CHOICES = (
    ("Santo Rosario", "Santo Rosario"),
    ("San Carlos", "San Carlos"),
    ("Parian", "Parian"),
    ("Balas", "Balas"),
    ("Divisoria", "Divisoria"),
    ("San Vicente", "San Vicente"),
    ("Santo Cristo", "Santo Cristo"),
    ("Lagundi", "Lagundi"),
    ("San Jose Matulid", "San Jose Matulid"),
    ("San Miguel", "San Miguel"),
    ("Sabanilla", "Sabanilla"),
)

SHIFT_CHOICES = (
    ("Day", "Day"),
    ("Afternoon", "Afternoon"),
)

STAFF_CHOICES = (
    ("Nurse", "Nurse"),
    ("Clinical Officer", "Clinical Officer"),
    ("Public Health Officer", "Public Health Officer"),
    ("Cleaner", "Cleaner"),
    ("Security", "Security"),
    ("Driver", "Driver"),
    ("Counselor", "Counselor"),
    ("Nutritionist", "Nutritionist"),
)

class HealthHistory(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    history_checkup = models.TextField()
    diagnosis = models.TextField(null=True)

    def __str__(self):
        return self.patient.name

class PatientVisit(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    visit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name

class Patient(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)
    phone = models.CharField(max_length=200)
    address = models.CharField(choices=BARANGAY_CHOICES, max_length=100)
    dental_report = models.CharField(max_length=200, default='No dental report available')
    laboratory_report = models.CharField(max_length=200, default='No laboratory report available')
    health_history = models.CharField(max_length=200, default='No history yet')
    diagnosis = models.CharField(max_length=200, default='No diagnosis yet')
    registered_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Nurse(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)
    phone = models.CharField(max_length=200)
    address = models.CharField(choices=BARANGAY_CHOICES, max_length=200)
    employment_date = models.DateTimeField()
    def __str__(self):
        return self.user.name

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(choices=BARANGAY_CHOICES, max_length=200)

    def __str__(self):
        return self.user.name

class HealthWorker(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(choices=BARANGAY_CHOICES, max_length=200)
    employment_date = models.DateTimeField()
    def __str__(self):
        return self.user.name

class MedicineSupply(models.Model):
    drug_code = models.CharField(max_length=200)
    drug_name = models.CharField(max_length=500)
    supply_unit = models.CharField(max_length=300)
    quantity = models.FloatField()
    date_recorded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.drug_name

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescribed_on = models.DateTimeField(default=timezone.now)
    prescribed_medicine = models.ForeignKey(MedicineSupply, on_delete=models.CASCADE, null=True, blank=True)
    prescription_notes = models.TextField()
    prescribed_by = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.patient.name} - {str(self.prescribed_drug)}"

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=SEX_CHOICES)
    phone = models.CharField(max_length=200)
    description = models.TextField(null=True)
    date_requested = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class PatientFeedback(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    comment = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name
