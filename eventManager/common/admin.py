from django.contrib import admin
from unfold.admin import ModelAdmin

from eventManager.accounts.models import AppUser
from eventManager.common.models import Venue, Organizer
from eventManager.events.models import Event, Registration


@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ('title', 'date', 'venue', 'organizer', 'created_at')

    search_fields = ('title', 'description', 'location', 'organizer__name', 'venue__name')

    list_filter = ('organizer', 'venue', 'date',)

    ordering = ('date',)

    actions = ['mark_as_cancelled']

    def mark_as_cancelled(self, request, queryset):
        queryset.update(description="Cancelled")
        self.message_user(request, f"{queryset.count()} events were marked as cancelled.")

    mark_as_cancelled.short_description = "Mark selected events as Cancelled"


@admin.register(Venue)
class VenueAdmin(ModelAdmin):
    list_display = ('name', 'location', 'capacity')
    search_fields = ('name', 'location')
    list_filter = ('location',)


@admin.register(Organizer)
class OrganizerAdmin(ModelAdmin):
    list_display = ('name', 'contact_info')
    search_fields = ('name', 'contact_info')
    list_filter = ('name',)


@admin.register(Registration)
class RegistrationAdmin(ModelAdmin):
    list_display = ('user', 'event', 'registration_date')

    list_filter = ('registration_date', 'event')

    search_fields = ('user__username', 'event__title')

    ordering = ('registration_date',)

    actions = ['delete_registrations']



@admin.register(AppUser)
class AppUserAdmin(ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')

    list_filter = ('is_staff', 'is_active', 'date_joined')

    search_fields = ('username', 'email')

    ordering = ('date_joined',)

    actions = ['activate_users', 'deactivate_users']

    def activate_users(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(request, f"{count} users were activated.")

    activate_users.short_description = "Activate selected users"

    def deactivate_users(self, request, queryset):
        count = queryset.update(is_active=False)
        self.message_user(request, f"{count} users were deactivated.")

    deactivate_users.short_description = "Deactivate selected users"
