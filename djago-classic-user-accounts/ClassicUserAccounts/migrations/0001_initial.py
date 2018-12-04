# Generated by Django 2.1.1 on 2018-09-23 08:35

import ClassicUserAccounts.managers
from django.db import migrations, models
import django.db.models.deletion
from ClassicUserAccounts.initial_migrations import insert_timezone

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ClassicUserAccounts', '0010_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offset', models.CharField(max_length=50)),
                ('abbr', models.CharField(blank=True, max_length=50, null=True)),
                ('zone_text', models.CharField(db_index=True, max_length=200, unique=True)),
                ('value', models.CharField(max_length=200, unique=True)),
                ('utc', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Timezone',
                'verbose_name_plural': 'Timezones',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('title', models.CharField(blank=True, choices=[('1st\xa0Lt', 'First Lieutenant'), ('Adm', 'Admiral'), ('Atty', 'Attorney'), ('Capt', 'Captain\xa0'), ('Chief', 'Chief'), ('Cmdr', 'Commander'), ('Col', 'Colonel'), ('Dean', 'Dean'), ('Dr', 'Doctor'), ('Gen', 'General'), ('Gov', 'Governor'), ('Hon', 'Honorable'), ('Lt Col', 'Lieutenant Colonel'), ('Maj', 'Major'), ('MSgt', 'Major/Master Sergeant'), ('Mr', 'Mister'), ('Mrs', 'Married Woman'), ('Ms', 'Single or Married Woman'), ('Prince', 'Prince'), ('Prof', 'Professor (includes Assistant and Associate')], max_length=100, null=True, verbose_name='title')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='last name')),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('fax', models.CharField(max_length=20, null=True)),
                ('website', models.URLField(max_length=300, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True)),
                ('skype_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Skype ID')),
                ('facebook_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Facebook ID')),
                ('twitter_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='LinkedIn ID')),
                ('linkedin_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Twitter ID')),
                ('business_email', models.EmailField(blank=True, help_text='<b>Note:</b>This email will used for all communication purpose.', max_length=250, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('timezone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ClassicUserAccounts.TimeZone')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', ClassicUserAccounts.managers.UserManager()),
            ],
        ),
        migrations.RunPython(insert_timezone)
    ]
