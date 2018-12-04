Django Classic Leads
-------
Detailed documentation is in the "docs" directory.

Quick
-----------
`1. Add "DjangoClassicLeads" to your INSTALLED_APPS setting like this::`
```
    INSTALLED_APPS = [
        ...
        'django.contrib.admin',
	    'django.contrib.auth',
        'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'DjangoClassicLeads',
    ]
```

`5. Add url in your project.urls file::`
```
	urlpatterns = [
	    path('accounts/', include('DjangoClassicLeads.urls')),
		...
	]
```

8. Run `python manage.py migrate` to manage lead.

`9. Start the development server and visit http://127.0.0.1:8000/admin/` to manage user profile (you'll need the Admin app enabled).
