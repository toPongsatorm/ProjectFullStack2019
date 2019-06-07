from django.contrib import admin
from .models import Book,Borrow,Publisher,Binding,Transaction
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Book._meta.fields]
admin.site.register(Book,BookAdmin)
class BorrowAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Borrow._meta.fields]
admin.site.register(Borrow,BorrowAdmin)
class PublisherAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Publisher._meta.fields]
admin.site.register(Publisher,PublisherAdmin)
class BindingAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Binding._meta.fields]
admin.site.register(Binding,BindingAdmin)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Transaction._meta.fields]
admin.site.register(Transaction,TransactionAdmin)
