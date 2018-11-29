from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].label = "Subject:"
        self.fields['from_email'].label = "Your email:"
        self.fields['message'].label = "What do you want to say?"
