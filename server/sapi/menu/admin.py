from django.contrib import admin

from menu.models import Menu, MenuItem



def refresh_menu(modeladmin, request, queryset):
    for menu in queryset:
        menu.fetch_menu()




class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'org', 'menu_items', 'source']
    actions = [refresh_menu]

    def menu_items(self, obj):
        return '<br/>'.join(item.__str__() for item in obj.menuitems.all())
    menu_items.allow_tags = True


class MenuItemAdmin(admin.ModelAdmin):
    search_fields = ['name', 'menu', 'about']
    list_display = ['name', 'menu', 'about', 'id']



admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)