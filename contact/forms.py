from django import forms


class ContactForm(forms.Form):
	name = forms.CharField(label='', max_length=100)
	email = forms.EmailField(label='', max_length=100)
	reason = forms.Select(choices=[])
	message = forms.Textarea()