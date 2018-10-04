from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
      widget=forms.TextInput(
        attrs={
          "class": "form-control",
        }
      ),
      max_length=50, 
      required=True)
    from_email = forms.EmailField(
      widget=forms.EmailInput(
        attrs={
          "class": "form-control",
        }
      ),
      max_length=100, 
      required=True)
    message = forms.CharField(
      widget=forms.Textarea(
        attrs={
          "class": "form-control",
          "rows": 5,
        }
      ), 
      max_length=3000, 
      required=True)