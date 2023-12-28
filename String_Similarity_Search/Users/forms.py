from django import forms

from Users.models import UserRegister_Model, UserUpload_Model


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegister_Model
        fields = ('firstName','lastName','userName', 'password', 'mobilenum', 'emailId', 'location', 'dob',)

class UserUploadForm(forms.ModelForm):
    class Meta:
        model = UserUpload_Model
        fields = ('title', 'document', 'original_cluster')

