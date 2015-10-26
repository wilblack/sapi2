import json
import requests
from jsonfield import JSONField


from django.db import models

from accounts.models import Org



MENU_SOURCES = [
    ('local', 'User Defined'),
    ('mmjmenu', 'MMJ Menu'),
    ('biotrack', 'Bio Tracker')
]



class Menu(models.Model):
    org = models.ForeignKey(Org)
    name = models.CharField(max_length=200)
    source = models.CharField(choices=MENU_SOURCES, default='local', max_length=25)
    
    def __unicode__(self):
        return "%s - %s" %(self.org, self.name)

    def fetch_menu(self):
        url = 'https://mmjmenu.com/api/v1/menu_items'
        pwd = 'x'
        
        if self.source == 'mmjmenu':
            mmjmenu = self.org.attrs.get('mmjmenu', None)
            if not mmjmenu:
                raise Exception('mmjmenu keyword not found on Org.attrs')
            token = mmjmenu['token']
            res = requests.get(url, auth=(token, pwd))
            
            data = json.loads(res.text)
            menu_items = data['menu_items']
            for item in menu_items:
                category = item.pop('category')
                if category == 'Cannabis':
                    obj, created = MenuItem.objects.get_or_create(menu=self, sid=item['id'])
                    obj.name = item.pop('name')
                    obj.about = item.pop('body_html'),
                    obj.attrs = item
                    
                    obj.save()

        elif self.source == 'local':
            pass
        elif self.source == 'biotrack':
            pass


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='menuitems')
    name = models.CharField(max_length=200)
    about = models.TextField()
    sid = models.CharField(max_length=100, blank=True, null=True)

    attrs = JSONField(default={}, help_text="")

    def __str__(self):
        return self.name



