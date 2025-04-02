from django import from .forms import 
class FormContatto(forms.Form):
    nome = form.CharField()
    cognome = forms.CharFiled()
    email = forms.CharFiled()
    contenuto = forms.CharFiled(widget=forms.Textarea(attrs={"placeholder": "Area Testuale! Scrivi pure!"}))
    