from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import DweetForm, CommentForm, ReplyForm, ProfileImageForm, DweetImageForm, CommentImageForm, ReplyImageForm, CustomUserCreationForm, DweetEditForm, CommentEditForm, ReplyEditForm
from .models import Dweet, Comment, Reply, Profile, ProfileImage, DweetImage, CommentImage, ReplyImage

# Create your views here.

def index(request):
    return render(request, "astro/index.html")

def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("astro:dweet", dweet.id)
        
    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    return render(
        request,
        "astro/dashboard.html",
        {"form": form, "dweets": followed_dweets},
    )
    
def profile_image_upload(request):
    '''Process profile images uploaded by users'''
    if request.method == 'POST':
        form = ProfileImageForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            profileImage = form.save(commit=False)
            profileImage.user = request.user
            profileImage.save()
            img_obj = form.instance
            current_user_profile = request.user.profile
            current_user_profile.profileImage = img_obj.image
            current_user_profile.save()
            return render(
                request,
                "astro/profile_image_upload.html",
                {"form": form, "img_obj": img_obj}
            )
    else:
        form = ProfileImageForm()
        return render(
            request,
            "astro/profile_image_upload.html",
            {"form": form}
        )
        
def dweet_image_upload(request, pk):
    '''Process dweet images uploaded by users'''
    dweet = Dweet.objects.get(pk=pk)
    if request.method == "POST":
        form = DweetImageForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            dweetImage = form.save(commit=False)
            dweetImage.user = request.user
            dweetImage.save()
            img_obj = form.instance
            dweet.dweetImage = img_obj.image
            dweet.save()
            return render(
                request,
                "astro/dweet_image_upload.html",
                {"form": form, "img_obj": img_obj, "dweet": dweet}
            )
    else:
        form = DweetImageForm()
        return render(
            request,
            "astro/dweet_image_upload.html",
            {"form": form, "dweet": dweet}
        )
        
def comment_image_upload(request, pk):
    '''Process comment images uploaded by users'''
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentImageForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            commentImage = form.save(commit=False)
            commentImage.user = request.user
            commentImage.save()
            img_obj = form.instance
            comment.commentImage = img_obj.image
            comment.save()
            return render(
                request,
                "astro/comment_image_upload.html",
                {"form": form, "img_obj": img_obj, "comment": comment}
            )
    else:
        form = CommentImageForm()
        return render(
            request,
            "astro/comment_image_upload.html",
            {"form": form, "comment": comment}
        )
        
def reply_image_upload(request, pk):
    '''Process reply images uploaded by users'''
    reply = Reply.objects.get(pk=pk)
    if request.method == "POST":
        form = ReplyImageForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            replyImage = form.save(commit=False)
            replyImage.user = request.user
            replyImage.save()
            img_obj = form.instance
            reply.replyImage = img_obj.image
            reply.save()
            return render(
                request,
                "astro/reply_image_upload.html",
                {"form": form, "img_obj": img_obj, "reply": reply}
            )
    else:
        form = ReplyImageForm()
        return render(
            request,
            "astro/reply_image_upload.html",
            {"form": form, "reply": reply}
        )
                
def dweet(request, pk):
    dweet = Dweet.objects.get(pk=pk)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            dweet.comments.add(comment.id)
            dweet.save()
            return redirect("astro:comment", comment.id)
    
    return render(
        request,
        "astro/dweet.html",
        {"form": form, "dweet": dweet}
    )
    
def dweet_edit(request, pk):
    '''Edit Dweets for Users'''
    context = {}
    dweet = Dweet.objects.get(pk=pk)
    initial_dweet = {
        "body": dweet.body
    }
    form = DweetEditForm(request.POST or None, initial=initial_dweet)
    context['form'] = form
    context['dweet'] = dweet
    if request.method == "POST":
        if form.is_valid():
            updated_dweet = form.save(commit=False)
            dweet.body = updated_dweet.body
            dweet.save()
            return redirect("astro:dweet", dweet.id)
    return render(
        request,
        "astro/dweet_edit.html",
        context
    )
    
def comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    dweet = Dweet.objects.get(comments__id=comment.id)
    form = ReplyForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.save()
            comment.replies.add(reply.id)
            comment.save()
            return redirect("astro:comment", comment.id)
            
    return render(
        request,
        "astro/comment.html",
        {"form": form, "comment": comment, "dweet": dweet}
    )
    
def comment_edit(request, pk):
    '''Edit Comments for Users'''
    context = {}
    comment = Comment.objects.get(pk=pk)
    initial_comment = {
        'body': comment.body
    }
    form = CommentEditForm(request.POST or None, initial=initial_comment)
    context['form'] = form
    context['comment'] = comment
    if request.method == "POST":
        if form.is_valid():
            updated_comment = form.save(commit=False)
            comment.body = updated_comment.body
            comment.save()
            return redirect("astro:comment", comment.id)
    return render(
        request,
        "astro/comment_edit.html",
        context
    )
    
def reply(request, pk):
    reply = Reply.objects.get(pk=pk)
    comment = Comment.objects.get(replies__id=reply.id)
    return render(
        request,
        "astro/reply.html",
        {"reply": reply, "comment": comment}
    )
    
def reply_edit(request, pk):
    '''Edit Replies for Users'''
    context = {}
    reply = Reply.objects.get(pk=pk)
    initial_reply = {
        'body': reply.body
    }
    form = ReplyEditForm(request.POST or None, initial=initial_reply)
    context['form'] = form
    context['reply'] = reply
    if request.method == "POST":
        if form.is_valid():
            updated_reply = form.save(commit=False)
            reply.body = updated_reply.body
            reply.save()
            return redirect("astro:reply", reply.id)
    return render(
        request,
        "astro/reply_edit.html",
        context
    )

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "astro/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "astro/profile.html", {"profile": profile})

def register(request):
    if request.method == "GET":
        return render(
            request, "astro/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('astro:dashboard'))