from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your models here.



class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_rating = self.post_set.aggregate(postRating=Sum('rating'))
        p_rating = 0
        p_rating += post_rating.get('postRating')

        comment_rating = self.author_user.comment_set.aggregate(commentRating=Sum('rating'))
        c_rating = 0
        c_rating += comment_rating.get('commentRating')
        self.rating_author = p_rating * 3 + c_rating
        self.save()


class Category(models.Model):
    name_category = models.CharField(max_length=128, unique=True)

class Post(models.Model):
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    NEWS = "NW"
    ARTICLE = "AR"
    CATEGORY_CHOICES = (
        (NEWS, "Новость"),
        (ARTICLE, "Статья"),
    )
    category_type = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    data_creation = models.DateTimeField(auto_now_add=True)
    post_categories = models.ManyToManyField(Category, through='PostCategory')
    article_title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()


    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + "..."



class PostCategory(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    dataTime_creation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


