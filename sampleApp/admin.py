from django.contrib import admin


from sampleApp.models import FeedBack, LoginTable, ManufactureTable,  ProductTable, UserTable

# Register your models here.
admin.site.register(UserTable)
admin.site.register(ManufactureTable)
admin.site.register(ProductTable)
admin.site.register(LoginTable)
admin.site.register(FeedBack)


