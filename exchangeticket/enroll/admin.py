from django.contrib import admin
from .models import Category, Ticket, TicketReview

# Register your models here.
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','desc','category','thumnail','quality','price','time_pub', 'author')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class TicketReviewAdmin(admin.ModelAdmin):
    	list_display=('user','ticket','review_text','get_review_rating',)
admin.site.register(TicketReview,TicketReviewAdmin)
