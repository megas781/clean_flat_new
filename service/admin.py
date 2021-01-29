from django.contrib import admin
from .models import Service, Order, Review, Discount, Faq, Report
# Register your models here.
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Discount)
admin.site.register(Faq)
admin.site.register(Report)