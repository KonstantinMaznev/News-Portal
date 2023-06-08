from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'authors'
            'article_title',
            'text',
            'category_type',
            'data_creation',
        ]

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 'NEWS'
        return super().form_valid(form)