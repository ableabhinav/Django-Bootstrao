from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    # url(r'^formpage/',views.form_name_view,name='form_name')
    url(r'^laptops$', display_laptops, name="display_laptops"),
    url(r'^desktops$', display_desktops, name="display_desktops"),
    url(r'^mobiles$', display_mobiles, name="display_mobiles"),
]
