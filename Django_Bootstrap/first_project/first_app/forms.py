from django import forms

# Very Basic Example of a Django Form

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

#Form for sign up - connected with model
class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'

'''
Important things to follow:

form.py--form_view(Create form render,etc.)--form.html(Show the form)--urls.py(urlpattern to call form_view 
																			that shows the template) 

forms.py - Used to actually create the form (what data to accept in the form)

Add a View in views.py - 
	Used to display the form: urls.py - has form_view
	Used to accept the data:
	Used to View data/connect to the model: for get/post method from the form.html 
	Used to connect to the model

Add a template form.html -
	This is the form that is rendered
	get the data from the user
	display the fomr using {{key name from form_view}}	
	Submit button - post - check in forms_view

Add to urls.py -
	Call the form_view and display form template when form urlpattern matched
'''
