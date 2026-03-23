from django import forms

from .models import Club


class ClubCreate(forms.ModelForm):
	class Meta:
		model = Club
		fields = [
			'name',
			'description',
			'price',
			'location'
		]
