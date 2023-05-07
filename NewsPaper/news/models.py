from django.db import models

# Create your models here.

class User(models.Model):
    pass

class Author(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_author = models.FloatField(default=0.0)


class Category(models.Model):
    name_category = models.CharField(max_length=255, unique=True)

class Post(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    article_title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField(default=0.0)

    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        return self.rating + 1.0

    def dislike(self):
        return self.rating - 1.0

    def preview(self):
        return self.text[:125] + "..."



class PostCategory(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    time_comment = time_in = models.DateTimeField(auto_now_add=True)
    rating_comment = models.FloatField(default=0.0)

    def like(self):
        return self.rating_comment + 1.0

    def dislike(self):
        return self.rating_comment - 1.0


