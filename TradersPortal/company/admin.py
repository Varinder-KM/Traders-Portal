from django.contrib import admin
from company.models import company_model, watchlist_model

admin.site.register(company_model)
admin.site.register(watchlist_model)
