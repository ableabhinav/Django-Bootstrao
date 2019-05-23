from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'first_app/index.html',date_dict)

def form_name_view(request):
    form = forms.FormName()

    # Check to see if we get a POST back.
    if request.method == 'POST':
        # In which case we pass in that request.
        form = forms.FormName(request.POST)

        # Check to see form is valid
        if form.is_valid():
            # Do something.
            print("Form Validation Success. Prints in console.")
            print("Name"+form.cleaned_data['name'])
            print("Email"+form.cleaned_data['email'])
            print('Text'+form.cleaned_data['text'])
    return render(request,'basicapp/form_page.html',{'form':form})