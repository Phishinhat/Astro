from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Dweet, Comment, Reply, ProfileImage, DweetImage, CommentImage, ReplyImage

class ProfileImageForm(forms.ModelForm):
    '''Form for the ProfileImage Model'''
    class Meta:
        model = ProfileImage
        fields = ('image',)
        
class DweetImageForm(forms.ModelForm):
    '''Form for the DweetImage Model'''
    class Meta:
        model = DweetImage
        fields = ('image',)
        
class CommentImageForm(forms.ModelForm):
    '''Form for the CommentImage Model'''
    class Meta:
        model = CommentImage
        fields = ('image',)
        
class ReplyImageForm(forms.ModelForm):
    '''Form for the ReplyImage Model'''
    class Meta:
        model = ReplyImage
        fields = ('image',)

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Dweet
        exclude = ("user", "comments", "reactions", "dweetImage")
        
class CommentForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Comment something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )
    
    class Meta:
        model = Comment
        exclude = ("user", "replies", "reactions", "commentImage")
        
class ReplyForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Reply something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label = "",
    )
    
    class Meta:
        model = Reply
        exclude = ("user", "reactions", "replyImage")
        
class DweetEditForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "class": "textarea is-success is-medium",
            }
        ),
        label = "",
    )
    
    class Meta:
        model = Dweet
        exclude = ("user", "comments", "reactions", "dweetImage")
        
class CommentEditForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "class": "textarea is-success is-medium",
            }
        ),
        label = "",
    )
    
    class Meta:
        model = Comment
        exclude = ("user", "replies", "reactions", "commentImage")
        
class ReplyEditForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "class": "textarea is-success is-medium",
            }
        ),
        label = "",
    )
    
    class Meta:
        model = Reply
        exclude = ("user", "reactions", "replyImage")
        
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name',)