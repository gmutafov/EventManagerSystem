from django import forms

from eventManager.common.models import Venue, Organizer


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'location', 'capacity', 'available_from']
        widgets = {
            'available_from': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name', 'contact_info', 'bio']


class OrganizerDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Are you sure you want to delete this Organizer?")

    def clean_confirm(self):
        confirm = self.cleaned_data.get('confirm')
        if not confirm:
            raise forms.ValidationError("You must confirm before deleting this Organizer.")
        return confirm
