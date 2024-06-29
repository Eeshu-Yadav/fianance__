from django.contrib import admin
from .models import Portfolio, LegSettings, LegExecutionDetails, RequestData

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'expiry', 'start', 'end', 'target', 'stop_loss')
    search_fields = ('name', 'expiry')

@admin.register(LegSettings)
class LegSettingsAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'state', 'right', 'txn', 'execution_time', 'sqoff_time', 'count_sl', 'count_tp', 'target_premium', 'stop_loss', 'take_profit','on_tp', 'on_sl', 'tgt_type', 'sl_type', 'tp_type')
    search_fields = ('portfolio__name', 'right', 'txn')

@admin.register(LegExecutionDetails)
class LegExecutionDetailsAdmin(admin.ModelAdmin):
    list_display = ('sqoff', 'execute', 'rexecute', 'rentry')
    search_fields = ('sqoff', 'execute', 'rexecute', 'rentry')

@admin.register(RequestData)
class RequestDataAdmin(admin.ModelAdmin):
    list_display = ('endpoint', 'timestamp')
    search_fields = ('endpoint', 'timestamp')
