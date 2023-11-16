from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "phone", "address", "dental_report", "laboratory_report", "health_history", "diagnosis", "registered_date")

@admin.register(MedicineSupply)
class DrugAdmin(admin.ModelAdmin):
    list_display = ("drug_code", "drug_name", "supply_unit", "date_recorded")

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("patient", "prescribed_on", "prescribed_medicine", "prescription_notes", "prescribed_by")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "description", "date_requested")

@admin.register(PatientVisit)
class PatientVisitAdmin(admin.ModelAdmin):
    list_display = ("patient", "visit_date")

@admin.register(PatientFeedback)
class PatientFeedbackAdmin(admin.ModelAdmin):
    list_display = ("patient", "comment", "date_commented")

@admin.register(HealthHistory)
class HealthHistoryAdmin(admin.ModelAdmin):
    list_display = ("patient", "history_checkup", "diagnosis")

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "address")

admin.site.site_title = "MEXICO RURAL HEALTH UNIT"
admin.site.site_header = "MEXICO RURAL HEALTH UNIT"
