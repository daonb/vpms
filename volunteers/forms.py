from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from volunteers.models import EKnight, Expertise, Volunteer

class Add_volunteer(ModelForm):
	class Meta:
		model = Volunteer
		exclude = ['old_num_of_arrivals']
		widgets = {
			'first_name': forms.TextInput(attrs={
				'autofocus': 'true',
				'required': 'required'
			}),
			'last_name': forms.TextInput(attrs={
				'required': 'required',
			}),
			'email': forms.TextInput(attrs={
				'type': 'email',
				'required': 'required',
			}),
			'phone': forms.TextInput(attrs={
				'type': 'phone',
				'required': 'required',
			}),
#			'skill': forms.TextInput(attrs={
#				'max_length': 999,
#				'autocomplete': 'on',
#				'list': 'skills',
#			}),
		}

class Add_project(ModelForm):
	class Meta:
		model = EKnight
		widgets = {
			'name': forms.TextInput(attrs={
				'type': 'text',
				'autofocus': 'true',
			})
	}
