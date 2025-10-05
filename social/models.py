from django.db import models
from django.contrib.auth.models import User

# Post model
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Optional media field
    media_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:20]}"


# Follow model
class Follow(models.Model):
    follower = models.ForeignKey(
        User, 
        related_name="following",  # users this user is following
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User, 
        related_name="followers",  # users who follow this user
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
