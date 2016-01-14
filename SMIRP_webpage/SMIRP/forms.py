from django import forms
from SMIRP.choices import *

class PredictionForm(forms.Form):
	sequence = forms.CharField(label='Sequence', max_length=30, required = False)
	model = forms.ChoiceField(choices = MODEL_CHOICES, label = 'Model', widget = forms.Select(), required = False)
	def is_valid(self):
		# Run the parent validation so django won't complain about not checking
		valid = super(PredictionForm, self).is_valid()
		return True