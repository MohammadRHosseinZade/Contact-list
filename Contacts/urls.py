from django.urls import path
from .views import GeneratePhoneContactView, UserContactlistView


urlpatterns = [
    path('generate/', GeneratePhoneContactView.as_view(), name='Generating Contact'),
    path('retrieve_list/', UserContactlistView.as_view(), name='Generating Contact'),
]
