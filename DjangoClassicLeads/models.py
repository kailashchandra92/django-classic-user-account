from django.db import models
import uuid
from django.conf import settings


class LeadMaster(models.Model):
    lead_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lead_title = models.CharField(max_length=500, null=True)
    lead_description = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    official_email = models.EmailField(null=True)
    official_phone = models.CharField(max_length=15, null=True, blank=True)
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(null=True)
    address_line1 = models.CharField(max_length=250, null=True, blank=True)
    address_line2 = models.CharField(max_length=250, null=True, blank=True)
    address_city = models.CharField(max_length=200, null=True, blank=True)
    address_state = models.CharField(max_length=50, null=True, blank=True)
    address_country = models.CharField(max_length=50, null=True, blank=True)
    address_zip = models.CharField(max_length=20, null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    twitter_handle = models.CharField(max_length=250, null=True, blank=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='lead_owner')
    source = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    privacy = models.CharField(max_length=250, null=True, blank=True)
    custom_fields = models.CharField(max_length=250, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='lead_created_by')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='lead_updated_by')
    deleted_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='lead_deleted_by')
    product = models.CharField(max_length=250, null=True, blank=True)
    value = models.DecimalField(max_digits=30, decimal_places=3, default=0, null=True)


class LeadFollowupHistory(models.Model):
    lead = models.ForeignKey(LeadMaster, on_delete=models.CASCADE, related_name='lead_master')
    activity = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True)
    next_activity_date = models.DateTimeField(null=True)
    followup_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    followup_date = models.DateTimeField(auto_created=True)