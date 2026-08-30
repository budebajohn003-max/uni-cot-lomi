from django.contrib import admin

try:
    from .models import CRTenant, Domain, TenantSubscription
except ImportError:
    # Handle case where models can't be imported during migrations/build
    CRTenant = None
    Domain = None
    TenantSubscription = None


if CRTenant is not None:
    @admin.register(CRTenant)
    class CRTenantAdmin(admin.ModelAdmin):
        list_display = ['name', 'schema_name', 'subdomain', 'is_active', 'is_trial', 'paid_until', 'created_on']
        list_filter = ['is_active', 'is_trial']
        search_fields = ['name', 'schema_name', 'subdomain']
        readonly_fields = ['schema_name', 'created_on']
        ordering = ['-created_on']


if Domain is not None:
    @admin.register(Domain)
    class DomainAdmin(admin.ModelAdmin):
        list_display = ['domain', 'tenant', 'is_primary']
        list_filter = ['is_primary']
        search_fields = ['domain']


if TenantSubscription is not None:
    @admin.register(TenantSubscription)
    class TenantSubscriptionAdmin(admin.ModelAdmin):
        list_display = ['tenant', 'plan', 'status', 'start_date', 'end_date', 'is_active', 'created_at']
        list_filter = ['plan', 'status', 'is_active']
        search_fields = ['tenant__name', 'tenant__schema_name', 'tenant__subdomain']
        ordering = ['-created_at']

