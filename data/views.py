from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            messages.error(request, 'Unrecognized user role or invalid credentials.')

        else:
            # Handle invalid login credentials
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')

@login_required
def dashboard(request):
    # Get data for the dashboard
    staff_count = Staff.objects.all().count()
    patient_count = Patient.objects.all().count()
    visit_count = PatientVisit.objects.all().count()
    drug_count = Drug.objects.all().count()
    appointment_count = Appointment.objects.all().count()
    prescription_count = Prescription.objects.all().count()
    history_count = HealthHistory.objects.all().count()
    feedback_count = PatientFeedback.objects.all().count()

    context = {
        'staff_count': staff_count,
        'patient_count': patient_count,
        'visit_count': visit_count,
        'drug_count': drug_count,
        'appointment_count': appointment_count,
        'prescription_count': prescription_count,
        'history_count': history_count,
        'feedback_count': feedback_count,
    }

    return render(request, 'dashboard.html', context)

@permission_required("data.view_staff")
def staffs(request):
    staffs = Staff.objects.all()
    return render(request, "data/staff.html", {"staffs": staffs})

@permission_required("data.view_staff")
def staff_details(request, id):
    staff = Staff.objects.get(pk=id)
    context = {
        "staff": staff
    }
    return render(request, "data/staff_details.html", context)

@permission_required("data.add_staff")
def add_staff(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StaffForm()
        else:
            staff = Staff.objects.get(pk=id)
            form = StaffForm(instance=staff)
        return render(request, "data/add_staff.html", {"form": form})
    else:
        if id == 0:
            form = StaffForm(request.POST)
        else:
            staff = Staff.objects.get(pk=id)
            form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
        return redirect('staff')

@permission_required("data.view_patient")
def patients(request):
    patients = Patient.objects.all()
    context = {
        "patients": patients
    }
    return render(request, "data/patients.html", context)

@permission_required("data.view_patients")
def patient_details(request, id):
    patient = Patient.objects.get(pk=id)
    context = {
        "patient": patient
    }
    return render(request, "data/patient_details.html", context)

@permission_required("data.add_patient")
def add_patient(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PatientForm()
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(instance=patient)
        return render(request, "data/add_patient.html", {"form": form})
    else:
        if id == 0:
            form = PatientForm(request.POST)
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
        return redirect('patients')

@permission_required("data.view_patientvisit")
def visits(request):
    visits = PatientVisit.objects.all()
    visits_count = PatientVisit.objects.all().count()
    context = {
        "visits": visits,
        "visits_count": visits_count
    }
    return render(request, "data/visits.html", context)

@permission_required("data.add_patientvisit")
def add_visit(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = VisitForm()
        else:
            visit = PatientVisit.objects.get(pk=id)
            form = VisitForm(instance=visit)
        return render(request, "data/add_visit.html", {"form": form})
    else:
        if id == 0:
            form = VisitForm(request.POST)
        else:
            visit = PatientVisit.objects.get(pk=id)
            form = VisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
        return redirect('visits')

@permission_required("data.view_drug")
def drugs(request):
    drugs = Drug.objects.all()
    return render(request, "data/drugs.html", {"drugs": drugs})

@permission_required("data.view_drug")
def drug_details(request, id):
    drug = Drug.objects.get(pk=id)
    context = {
        "drug": drug
    }
    return render(request, "data/drug_details.html", context)

@permission_required("data.add_drug")
def add_drug(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DrugForm()
        else:
            drug = Drug.objects.get(pk=id)
            form = DrugForm(instance=drug)
        return render(request, "data/add_drug.html", {"form": form})
    else:
        if id == 0:
            form = DrugForm(request.POST)
        else:
            drug = Drug.objects.get(pk=id)
            form = DrugForm(request.POST, instance=drug)
        if form.is_valid():
            form.save()
        return redirect('drugs')

@permission_required("data.view_appointment")
def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, "data/appointments.html", {"appointments": appointments})

@permission_required("data.view_appointment")
def appointment_details(request, id):
    appointment = Appointment.objects.get(pk=id)
    context = {
        "appointment": appointment
    }
    return render(request, "data/appointment_details.html", context)

@permission_required("data.add_appointment")
def add_appointment(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AppointmentForm()
        else:
            appointment = Appointment.objects.get(pk=id)
            form = AppointmentForm(instance=appointment)
        return render(request, "data/add_appointment.html", {"form": form})
    else:
        if id == 0:
            form = AppointmentForm(request.POST)
        else:
            appointment = Appointment.objects.get(pk=id)
            form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
        return redirect('appointments')


def prescriptions(request):
    prescriptions = Prescription.objects.all()
    return render(request, "data/prescriptions.html", {"prescriptions": prescriptions})

def add_prescription(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PrescriptionForm()
        else:
            prescription = Prescription.objects.get(pk=id)
            form = PrescriptionForm(instance=prescription)
        return render(request, "data/add_prescription.html", {"form": form})
    else:
        if id == 0:
            form = PrescriptionForm(request.POST)
        else:
            prescription = Prescription.objects.get(pk=id)
            form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
        return redirect('prescriptions')

def prescription_details(request, id):
    prescription = Prescription.objects.get(pk=id)
    context = {
        "prescription": prescription
    }
    return render(request, "data/prescription_details.html", context)

def health_histories(request):
    health_histories = HealthHistory.objects.all()
    return render(request, "data/histories.html", {"health_histories": health_histories})


def add_health_history(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = HistoryForm()
        else:
            history = HealthHistory.objects.get(pk=id)
            form = HistoryForm(instance=history)
        return render(request, "data/add_history.html", {"form": form})
    else:
        if id == 0:
            form = HistoryForm(request.POST)
        else:
            history = HealthHistory.objects.get(pk=id)
            form = HistoryForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
        return redirect('health_histories')

def feedback(request):
    feedbacks = PatientFeedback.objects.all()
    return render(request, "data/feedbacks.html", {"feedbacks": feedbacks})

def add_feedback(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FeedbackForm()
        else:
            feedback = PatientFeedback.objects.get(pk=id)
            form = FeedbackForm(instance=feedback)
        return render(request, "data/add_feedback.html", {"form": form})
    else:
        if id == 0:
            form = FeedbackForm(request.POST)
        else:
            feedback = PatientFeedback.objects.get(pk=id)
            form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
        return redirect('feedbacks')

def feedback_details(request, id):
    feedback = PatientFeedback.objects.get(pk=id)
    context = {
        "feedback": feedback
    }
    return render(request, "data/feedback_details.html", context)

def logout(request):
    auth.logout(request)
    return redirect("homepage")