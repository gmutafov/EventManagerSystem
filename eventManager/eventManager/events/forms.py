from django import forms
from eventManager.events.models import Event


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location','venue', 'organizer', 'image']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Event name should be at least 3 characters.")
        return title

class EventCreateForm(EventBaseForm):
        pass


class EventEditForm(EventBaseForm):
        pass


class EventDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Are you sure you want to delete this event?")

    def clean_confirm(self):
        confirm = self.cleaned_data.get('confirm')
        if not confirm:
            raise forms.ValidationError("You must confirm before deleting the event.")
        return confirm


class EventDetailsForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'image']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'disabled': True}),
        }
        readonly_fields = ['title', 'description', 'date', 'location', 'image']


