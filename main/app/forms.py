from django import forms

class feedback(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.EmailField(label='Your email', max_length=100)
    your_mesg = forms.CharField(label='Message',widget=forms.Textarea)

