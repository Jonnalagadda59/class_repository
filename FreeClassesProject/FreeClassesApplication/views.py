from django.shortcuts import render
from .models import ClassData,FeedbackData,MessageData,DocumentData
from .forms import ClassForm,FeedbckForm,MessageForm,DocumentForm
from django.http.response import HttpResponse
import datetime
date1 = datetime.datetime.now()
# Create your views here.
def main_page(request):
    return render(request,'main_page.html')


def home_page(request):
    return render(request,'home_page.html')


def class_page(request):
    if request.method =="POST":
        cform = ClassForm(request.POST)
        if cform.is_valid():
            instname=request.POST.get('instname')
            course=request.POST.get('course')
            start_date = cform.cleaned_data.get('start_date')
            venue=request.POST.get('venue')

            data = ClassData(
                instname=instname,
                course=course,
                venue=venue,
                start_date=start_date,
            )
            data.save()
            cform = ClassForm()
            cdata = ClassData.objects.all()
            return render(request,'class_page.html',{'cform':cform,'cdata':cdata})
        else:
            return HttpResponse("Invalid Input")
    else:
        cdata = ClassData.objects.all()
        cform = ClassForm()
        return render(request, 'class_page.html', {'cform': cform, 'cdata': cdata})


def retrieve_page(request):
    cdata = ClassData.objects.all()
    return render(request,'retrieve_page.html',{'cdata': cdata})

def feedback_page(request):
    if request.method == "POST":
        fform = FeedbckForm(request.POST)
        if fform.is_valid():
            instname = request.POST.get('instname', '')
            faculty = request.POST.get('faculty','')
            rating = request.POST.get('rating', '')  # IntegrityError at /feedback/rating=ratimg
            feedback = request.POST.get('feedback', '')
            data = FeedbackData(
                instname=instname,
                faculty=faculty,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fdata = FeedbackData.objects.all()
            fform = FeedbckForm()
            return render(request, 'feedback_page.html', {'fform': fform, 'fdata': fdata})

        else:
            return HttpResponse("Invalid User Data")
    else:
        fdata = FeedbackData.objects.all()
        fform = FeedbckForm()
        return render(request, 'feedback_page.html', {'fform': fform, 'fdata': fdata})

def message_page(request):
    if request.method == "POST":
        mform = MessageForm(request.POST)
        if mform.is_valid():
            name = request.POST.get('name', '')

            # IntegrityError at /feedback/rating=ratimg
            message = request.POST.get('message', '')
            data = MessageData(
                name=name,
                message=message,
                date=date1
            )
            data.save()
            mdata = MessageData.objects.all()
            mform = MessageForm()
            return render(request, 'message_page.html', {'mform': mform, 'mdata': mdata})

        else:
            return HttpResponse("Invalid User Data")
    else:
        mdata = MessageData.objects.all()
        mform = MessageForm()
        return render(request, 'message_page.html', {'mform': mform, 'mdata': mdata})


def upload_file_page(request):
    if request.method == 'POST':
        dform = DocumentForm(request.POST)
        if dform.is_valid():
            subject = request.POST.get('subject')
            files = request.POST.get('files')
            data = DocumentData(
                subject=subject,
                files=files
            )
            data.save()
            ddata = DocumentData.objects.all()
            dform = DocumentForm()  # A empty, unbound form
            return render(request, 'upload_page.html', {'ddata': ddata, 'dform': dform})

        else:
            return HttpResponse('Invalid Data')


    else:
        ddata = DocumentData.objects.all()
        dform = DocumentForm()  # A empty, unbound form
        return render(request, 'upload_page.html', {'ddata': ddata, 'dform': dform})


def app_icon_page(request):
    return render(request,'app_icon_page.html')


