from django.contrib import admin
from accounts.models import Gender, Programme, TranscriptType, DeliveryOption, IdentificationType, GraduateType

admin.site.register(Gender)
admin.site.register(Programme)
admin.site.register(TranscriptType)
admin.site.register(DeliveryOption)
admin.site.register(IdentificationType)
admin.site.register(GraduateType)

