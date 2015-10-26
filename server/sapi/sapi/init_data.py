from django.contrib.auth.models import User



from accounts.models import Profile, Org
from menu.models import Menu

ORGS = [
    {
        'name':'Green Buds',
        'slug':'green-buds',
        'attrs': {
            'mmjmenu':{
                'token':'IJoqwaFEPNnsbrDjSXfKtSxxC'
            }
        }
    },
    {
        'name':'NBHH',
        'slug':'nbhh',
        'attrs': {}
    }
]


USERS = [
    {   'username':'wilblack',
        'password':'wilblack1',
        'first_name':'Wil',
        'last_name':'Black',
        'is_staff':True,
        'is_superuser':True,
        'email':'wil.black@solalla.com',
        'attrs': {},
        'orgs': ['green-buds']
    },
    {   'username':'admin',
        'password':'admin1',
        'first_name':'Admin',
        'last_name':'User',
        'is_staff':True,
        'is_superuser':True,
        'email':'',
        'attrs':{},
        'orgs': ['green-buds']
    }
]


MENUS = [
    {
        'name': 'Store 1 Menu',
        'org': 'green-buds',
        'source': 'mmjmenu'
    }
]

def load(overwrite=False):
    print "~"*10+" ORGS "+"~"*10
    for obj in ORGS:
        print "  Adding: "+obj['name']
        org, created = Org.objects.get_or_create(slug=obj['slug'])

        if overwrite or created:
            org.name = obj['name']
            org.attrs = obj['attrs']
            org.save()


    print "~"*10+" USERS "+"~"*10
    for obj in USERS:
        print "  Adding: "+obj['username']
        user, created = User.objects.get_or_create(username=obj['username'])

        if overwrite or created:
            user.is_superuser = obj['is_superuser']
            user.is_staff = obj['is_staff']
            user.first_name = obj['first_name']
            user.last_name = obj['last_name']
            user.email = obj['email']
            user.set_password(obj['password'])
            
            user.save()
            user.profile.attrs = obj['attrs']
            
            # update orgs
            user.profile.orgs.clear()
            for slug in obj.get('orgs', []):
                org = Org.objects.get(slug=slug)
                user.profile.orgs.add(org)


            user.profile.save()


    print "~"*10+" MENUS "+"~"*10
    for obj in MENUS:
        org = Org.objects.get(slug=obj['org'])
        menu, created = Menu.objects.get_or_create(name=obj['name'], org=org)
        if overwrite or created:
            menu.source = obj['source']
            menu.save()





