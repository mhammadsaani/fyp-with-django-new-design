from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView
from legalysis.forms import FileForm
from legalysis.models import Document, User


# class UploadDocument(View):
    
#     def get(self, request):
#         form = FileForm()
#         return render(request, 'legalysis/index.html', {'form': form})
    
    
#     def post(self, request):
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             doc = form.cleaned_data['document']
#             document = Document(user=User.objects.get(username='admin'), document=doc)
#             document.save()
#             return render(request, 'legalysis
# /index.html', {'form': form})
            
#         else:
#             return render(request, 'legalysis/index.html', {'form': form})
        
        
class UploadDocument(FormView):
    template_name = 'legalysis/index.html'
    form_class = FileForm
    success_url = "/chat/"
    model = Document
    
    def form_valid(self, form):
        doc = form.cleaned_data['document']
        document = Document(user=User.objects.get(username='admin'), document=doc)
        document.save()
        return super().form_valid(form)
    

class Chat(View):
    def get(self, request):
        return render(request, 'legalysis/chat.html')
    
    def post(self, request):
        prompt = request.POST['prompt']
        return render(request, 'legalysis/chat.html')
        