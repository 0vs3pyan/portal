from django import forms
from django_summernote.fields import SummernoteTextField, SummernoteTextFormField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from news.models import Comments


class CommentForm(forms.ModelForm):
    text = SummernoteTextFormField()

    class Meta:
        model = Comments
        fields = (
            'text',
        )
        widgets = {
            'text': SummernoteInplaceWidget()
        }
