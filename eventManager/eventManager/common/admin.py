from django.contrib import admin

from eventManager.accounts.models import AppUser
from eventManager.common.models import Venue, Organizer
from eventManager.events.models import Event, Registration


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # 1. List Display
    list_display = ('title', 'date', 'venue', 'organizer', 'created_at')

    # 2. Search Fields
    search_fields = ('title', 'description', 'location', 'organizer__name', 'venue__name')

    # 3. Filters
    list_filter = ('date', 'venue', 'organizer')

    # 4. Ordering
    ordering = ('date',)

    # 5. Custom Actions
    actions = ['mark_as_cancelled']

    def mark_as_cancelled(self, request, queryset):
        queryset.update(description="Cancelled")
        self.message_user(request, f"{queryset.count()} events were marked as cancelled.")

    mark_as_cancelled.short_description = "Mark selected events as Cancelled"


# Register other models with minimal customization
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity')
    search_fields = ('name', 'location')


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info')
    search_fields = ('name', 'contact_info')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    # 1. List Display
    list_display = ('user', 'event', 'registration_date')

    # 2. Filters
    list_filter = ('registration_date', 'event')

    # 3. Search Fields
    search_fields = ('user__username', 'event__title')

    # 4. Ordering
    ordering = ('registration_date',)

    # 5. Custom Actions
    actions = ['delete_registrations']

    def delete_registrations(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} registrations were successfully deleted.")

    delete_registrations.short_description = "Delete selected registrations"



@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    # 1. List Display
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')

    # 2. Filters
    list_filter = ('is_staff', 'is_active', 'date_joined')

    # 3. Search Fields
    search_fields = ('username', 'email')

    # 4. Ordering
    ordering = ('date_joined',)

    # 5. Custom Actions
    actions = ['activate_users', 'deactivate_users']

    def activate_users(self, request, queryset):
        count = queryset.update(is_active=True)
        self.message_user(request, f"{count} users were activated.")

    activate_users.short_description = "Activate selected users"

    def deactivate_users(self, request, queryset):
        count = queryset.update(is_active=False)
        self.message_user(request, f"{count} users were deactivated.")

    deactivate_users.short_description = "Deactivate selected users"
