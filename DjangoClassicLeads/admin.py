from django.contrib import admin
from .models import LeadMaster, LeadFollowupHistory


class LeadFollowupHistoryInline(admin.StackedInline):
    model = LeadFollowupHistory
    extra = 0


class LeadMasterAdmin(admin.ModelAdmin):
    list_display = ('lead_title', 'first_name', 'last_name', 'official_email', 'official_phone', 'mobile_no', 'owner', 'product', 'value')
    search_fields = ('lead_title', 'first_name', 'last_name', 'official_email', 'official_phone', 'mobile_no', 'owner', 'product', 'value')
    inlines = [LeadFollowupHistoryInline, ]


admin.site.register(LeadMaster, LeadMasterAdmin)
