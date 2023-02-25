from courses.models import course
from django import forms

class CourseModelForm(forms.ModelForm):
    class Meta:
        model=course
        fields='__all__'
    #     field_args={
    #         "name": {
    #             "error_messages":{
    #                 "required":"Please let us know what to call you",
    #                 "max_length":"Too short!!!"
    #         }
    #     }
    # }
