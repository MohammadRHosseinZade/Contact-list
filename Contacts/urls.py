from django.urls import path
from .views import GeneratePhoneContactView, UserContactlistView, ContactInfoUpdateView


urlpatterns = [
    path('generate/', GeneratePhoneContactView.as_view(), name='Generating Contact'),
    path('retrieve_list/', UserContactlistView.as_view(), name='retrieve list Contact'),
    path('update_contact_detail/<int:detail_id>/', ContactInfoUpdateView.as_view(), name='update contact detail'),
]

 