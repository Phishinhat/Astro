from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profileImage = models.ImageField(
        default= 'default.png',
        blank=True
    )
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
    
    def __str__(self):
        return self.user.username
        
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()
        
class ProfileImage(models.Model):
    user = models.ForeignKey(
        User,
        related_name="profile_images",
        on_delete=models.DO_NOTHING
    )
    image = models.ImageField(
        upload_to='images/Users/Profiles',
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def get_absolute_url(self):
        return reverse('profileImage-detail', args=[str(self.id)])
        
    def __str__(self):
        return (
            f"{self.user.username} "
            f"({self.created_at:%Y-%m-%d %H:%M})"
        )
        
class DweetImage(models.Model):
    user = models.ForeignKey(
        User,
        related_name="dweet_images",
        on_delete=models.DO_NOTHING
    )
    image = models.ImageField(
        upload_to='images/Users/Dweets',
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def get_absolute_url(self):
        return reverse('dweetImage-detail', args=[str(self.id)])
        
    def __str__(self):
        return (
            f"{self.user.username} "
            f"({self.created_at:%Y-%m-%d %H:%M})"
        )
        
class CommentImage(models.Model):
    user = models.ForeignKey(
        User,
        related_name="comment_images",
        on_delete=models.DO_NOTHING
    )
    image = models.ImageField(
        upload_to='images/Users/Comments',
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def get_absolute_url(self):
        return reverse('commentImage-detail', args=[str(self.id)])
        
    def __str__(self):
        return (
            f"{self.user.username} "
            f"({self.created_at:%Y-%m-%d %H:%M})"
        )
        
class ReplyImage(models.Model):
    user = models.ForeignKey(
        User,
        related_name="reply_images",
        on_delete=models.DO_NOTHING
    )
    image = models.ImageField(
        upload_to='images/Users/Replies',
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def get_absolute_url(self):
        return reverse('replyImage-detail', args=[str(self.id)])
        
    def __str__(self):
        return (
            f"{self.user.username} "
            f"({self.created_at:%Y-%m-%d %H:%M})"
        )

class Dweet(models.Model):
    user = models.ForeignKey(User,
                             related_name="dweets",
                             on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=250)
    dweetImage = models.ImageField(
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(
        'Comment',
        related_name="dweeted_by",
        symmetrical=False,
        blank=True
    )
    
    class Meta:
        ordering = ['-created_at']
    
    def get_absolute_url(self):
        return reverse('dweet-detail', args=[str(self.id)])

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )
        
class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=250)
    replies = models.ManyToManyField(
        'Reply',
        related_name="commented_by",
        symmetrical=False,
        blank=True
    )
    commentImage = models.ImageField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    class Meta:
        ordering = ['-created_at']
    
    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])
    
    def __str__(self):
        return (
            f'{self.user} '
            f'({self.created_at:%Y-%m-%d %H:%M}): '
            f'{self.body[:30]}...'
        )
        
class Reply(models.Model):
    user = models.ForeignKey(
        User,
        related_name="replies",
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(
        max_length=250
    )
    replyImage = models.ImageField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    class Meta:
        ordering = ['-created_at']
        
    def get_absolute_url(self):
        return reverse('reply-detail', args=[str(self.id)])
        
    def __str__(self):
        return (
            f"{self.user.username} "
            f"({self.created_at:%Y-%m-%d %H:%M})"
        )