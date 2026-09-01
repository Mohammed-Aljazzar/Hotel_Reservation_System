from django.db import models
from django.urls import reverse
from  django.utils import timezone
from django.contrib.auth.models import User 
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name=_("title"))
    tag = TaggableManager()
    image = models.ImageField(_("image"),upload_to='posts/')
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author',verbose_name=_("author"))
    description = models.TextField(_("description"),max_length=15000)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_("category"),related_name='post_category')
    slug = models.SlugField(_("url"),null=True, blank=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    slug = models.SlugField(max_length=80, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(str(self.name), allow_unicode=True) or "category"
            slug = base_slug
            index = 2
            while type(self)._base_manager.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{index}"
                index += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
    
