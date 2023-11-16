from django import forms
from . models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('__all__')


class VisitForm(forms.ModelForm):
    class Meta:
        model = PatientVisit
        fields = ('__all__')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = PatientFeedback
        fields = ('__all__')

class MedicineSupplyForm(forms.ModelForm):
    class Meta:
        model = MedicineSupply
        fields = ('__all__')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('__all__')

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('__all__')

class HistoryForm(forms.ModelForm):
    class Meta:
        model = HealthHistory
        fields = ('__all__')

