from django.db import models
from django.contrib.auth.models import User

# user create လိုက်တာနဲ့ တန်းပြီး profile ဆောက်ပေးတယ်
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """User Profile model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.webp", upload_to="img/profiles", null=True, blank=True)
    position = models.CharField(max_length=255, blank=True, null=True, help_text="I am Backend Developer")
    description = models.CharField(max_length=500, blank=True, null=True)
    cv_file = models.FileField(upload_to="cv-files/", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profiles..."

    # user create လိုက်တာနဲ့ တန်းပြီး profile ဆောက်ပေးတယ်
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)