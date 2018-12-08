# Django Classic User Accounts

[![GitHub forks](https://img.shields.io/github/forks/sumankumar72/django-classic-user-account.svg)](https://github.com/sumankumar72/django-classic-user-account/network) [![GitHub issues](https://img.shields.io/github/issues/sumankumar72/django-classic-user-account.svg)](https://github.com/sumankumar72/django-classic-user-account/issues) [![GitHub stars](https://img.shields.io/github/stars/sumankumar72/django-classic-user-account.svg)](https://github.com/sumankumar72/django-classic-user-account/stargazers) [![GitHub license](https://img.shields.io/github/license/sumankumar72/django-classic-user-account.svg)](https://github.com/sumankumar72/django-classic-user-account)


#### Features
  - Type some Markdown on the left
  - Sing up
  - Email confirmation
  - Extended user model
  - Profile picture
  - Password reset
  - Account management (update account settings and change password)
  - Custom `User` model support

### Requirements
  - Django 2.0 +
  - Python 3.5, or 3.6

### Quick installation


`1. Add "ClassicUserAccounts" to your INSTALLED_APPS setting like this::`
```
    INSTALLED_APPS = [
        'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'ClassicUserAccounts',
	    'sorl.thumbnail',
	    'django.contrib.admin',
	    'django.contrib.auth',
	    ...
    ]
```
`2. Add "AUTH_USER_MODEL" in your settings file like this::`
```
	AUTH_USER_MODEL = 'ClassicUserAccounts.User'
```

`3. Add "Middleware" to youe MIDDLEWARE settings like this::`
```
	MIDDLEWARE = [
	   ...
	   'ClassicUserAccounts.middleware.ClassicUserAccountsMiddleWare',
	]
```

`4. Add "SITE_NAME" in your settings file like this::`
```
    SITE_NAME = 'Your site name'
```

`5. Add url in your project.urls file::`
```
	urlpatterns = [
	    path('accounts/', include('ClassicUserAccounts.urls')),
		...
	]
```
`6. Change Skin ::`
```
    Avaliable Skins:: [
        'skin-blue',
        'skin-black',
        'skin-red',
        'skin-yellow',
        'skin-purple',
        'skin-green',
        'skin-blue-light',
        'skin-black-light',
        'skin-red-light',
        'skin-yellow-light',
        'skin-purple-light',
        'skin-green-light'
    ]

    You have to add "ROLE_BASED_SKIN" in your settings.py file like this::

    ROLE_BASED_SKIN = [
        {'role': 'Admin', 'skin_name': 'skin-red'},
        {'role': 'Subscriber', 'skin_name': 'skin-purple'}
    ]
```
`7. Multi theme feature added::`
```
    Add THEME_NAME in your settings file to change theme
    THEME_NAME = 'default-theme'  Required
    USER_BASED_THEME = False # Default False
    Available themes : default-theme, theme-1, theme-2, theme-3
```

8. Run `python manage.py migrate` to extend django user model.

`9. Start the development server and visit http://127.0.0.1:8000/admin/` to manage user profile.
