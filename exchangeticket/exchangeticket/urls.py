"""exchangeticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from enroll import views
from django.conf.urls.static import static
from django.conf import settings

    # url(r'^accounts/', include('accounts.urls')),
urlpatterns = [
    path('accounts/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', views.home_page , name="homepage"),
    path('contact/<int:id>/', views.contact , name="contact"),
    path('search', views.search , name="search"),
    path('myticket/', views.add_show, name="addandshow"),
    path('delete/<int:id>/',views.delete_data, name="deletedata"),
    path('<int:id>/',views.update_data, name="updatedata"),
    path('ticket/<int:id>/',views.ticket_detail,name='ticket_detail'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('ticket/save-review/<int:pid>',views.save_review,name='save-review'),

]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)