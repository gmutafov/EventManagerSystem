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

