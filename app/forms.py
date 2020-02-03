from django import forms
from django.urls import reverse_lazy
from .models import Post
from .widgets import SuggestWidget


class PostCreateForm(forms.ModelForm):
    relation_posts = forms.ModelChoiceField(
        label='関連記事', queryset=Post.objects, required=False,
        widget=SuggestWidget(attrs={'data-url': reverse_lazy('app:api_posts_get')})
    )

    class Meta:
        model = Post
        fields = '__all__'

