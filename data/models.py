from django.db import models
from django.utils import timezone

# Create your models here.
SEX_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
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



class BaseInfo(models.Model):
    id_number = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=SEX_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        abstract = True

class Staff(BaseInfo):
    position = models.CharField(max_length=100, choices=STAFF_CHOICES)
    employment_date = models.DateTimeField()
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)

    def __str__(self):
        return self.name

class Patient(BaseInfo):
    registered_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

CONTRACT_CHOICES = (
    ("Temporary", "Temporary"),
    ("Permanent", "Permanent"),
)

class Drug(models.Model):
    drug_code = models.CharField(max_length=200)
    drug_name = models.CharField(max_length=500)
    manufacturer = models.CharField(max_length=500)
    supplied_on = models.DateTimeField(default=timezone.now)
    supply_unit = models.CharField(max_length=300)
    quantity = models.FloatField()
    unit_price = models.FloatField()
    date_recorded = models.DateTimeField(default=timezone.now)

    def total_price(self):
        return self.quantity * self.unit_price    

    def __str__(self):
        return self.drug_name

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescribed_by = models.ForeignKey(Staff, on_delete=models.CASCADE)
    prescribed_drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    prescribed_on = models.DateTimeField(default=timezone.now)
    prescription_notes = models.TextField()

    def __str__(self):
        return self.patient.name + " " + str(self.prescribed_drug)

class Appointment(models.Model):
    id_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=SEX_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    description = models.TextField(null=True)
    date_requested = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class PatientVisit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name

class PatientFeedback(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    comment = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.patient.name
    
class HealthHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    history = models.TextField()
    diagnosis = models.TextField(null=True)

    def __str__(self):
        return self.patient.name