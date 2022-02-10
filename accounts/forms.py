from django import forms

class SignUpForm(forms.Form):
	username = forms.CharField(max_length=30)

	def signup(self, request, user):
		user.username = self.cleaned_data['username']
		user.save()