import datetime

from django.contrib import admin

from accounts.models import Profile, Org

from rest_framework.authtoken.models import Token



def reset_or_create_api_token(modeladmin, request, queryset):
    for profile in queryset:
        token, created = Token.objects.get_or_create(user=profile.user)
        if not created:
            # Delete old token and create a new one
            token.delete()
            token = Token.objects.create(user=profile.user)
        token.created = datetime.datetime.utcnow()
        token.save()


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'org_names',  'api_token', 'attrs']
    actions = [reset_or_create_api_token]

class OrgAdmin(admin.ModelAdmin):
    search_fields = ['name', 'slug']
    list_display = ['name', 'slug', 'id']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Org, OrgAdmin)