from django import forms
from .models import AdmissionInquiry

class AdmissionInquiryForm(forms.ModelForm):

    class Meta:

        model = AdmissionInquiry

        fields = '__all__'

        widgets = {

            'student_name':
                forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Student Name'
                    }
                ),

            'parent_name':
                forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Parent Name'
                    }
                ),

            'age':
                forms.NumberInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Age'
                    }
                ),

            'mobile':
                forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Mobile Number'
                    }
                ),

            'email':
                forms.EmailInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Email Address'
                    }
                ),

            'course':
                forms.TextInput(
                    attrs={
                        'class':'form-control',
                        'placeholder':'Course Interested'
                    }
                ),

            'message':
                forms.Textarea(
                    attrs={
                        'class':'form-control',
                        'rows':4,
                        'placeholder':'Message'
                    }
                ),
        }