from django.urls import path
from .views import GeneratePhoneContactView


urlpatterns = [
    path('generate/', GeneratePhoneContactView.as_view(), name='Generating Contact'),

]
