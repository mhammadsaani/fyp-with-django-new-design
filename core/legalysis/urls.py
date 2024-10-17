from django.urls import path
from django.views.generic import TemplateView
from legalysis import views


app_name = 'legalysis'
urlpatterns = [
    path('', views.UploadDocument.as_view(), name='homepage'),
    path('chat/', views.Chat.as_view(), name='chat'),
    path('uploaded-documents/',TemplateView.as_view(template_name="legalysis/test.html"), name="uploaded_documents")
]
