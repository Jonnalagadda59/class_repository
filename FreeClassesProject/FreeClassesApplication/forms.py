from django import forms
from .models import ClassData,FeedbackData,MessageData,DocumentData


class ClassForm(forms.Form):
    instname = forms.CharField(
        label='Enter Institute Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Institute'
            }
        )

    )
    course = forms.CharField(
        label='Enter Course Name:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Course'
            }
        )

    )
    start_date = forms.DateField(
        widget=forms.SelectDateWidget()
    )

    venue = forms.CharField(
        label='Enter venue Name:',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter venue'
            }
        )

    )

class FeedbckForm(forms.Form):
    instname = forms.CharField(
        label='Enter Institution Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your Name'
            }
        )
    )
    faculty = forms.CharField(
        label='Enter Faculty Name:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'faculty Name'
            }
        )
    )
    rating = forms.IntegerField(
        label='Enter Your Rating:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label='Enter Your Feedback:',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )




class MessageForm(forms.Form):
    name = forms.CharField(
        label='Enter  Name:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your Name'
            }
        )
    )


    message = forms.CharField(
        label='Enter Your Message:',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )

class DocumentForm(forms.Form):
    subject  = forms.CharField(
        label="Enter your Subject:",
    )
    files = forms.FileField(max_length=10000)





