from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Post


@receiver(pre_save, sender=Post)
def set_published_date(sender, instance, **kwargs):
    """Set published_at when post status changes to published"""
    if instance.pk:
        try:
            old_instance = Post.objects.get(pk=instance.pk)
            if old_instance.status == 'draft' and instance.status == 'published':
                if not instance.published_at:
                    instance.published_at = timezone.now()
        except Post.DoesNotExist:
            pass
    else:
        if instance.status == 'published' and not instance.published_at:
            instance.published_at = timezone.now()


@receiver(post_save, sender=Post)
def notify_post_published(sender, instance, created, **kwargs):
    """Send notification when a post is published"""
    if instance.status == 'published':
        # In a real application, you would send emails, push notifications, etc.
        # For demonstration, we'll just print a message
        if created:
            print(f"New post published: {instance.title} by {instance.author.username}")
        else:
            print(f"Post updated and published: {instance.title}")
