from django.db import models

# Create your models here.
class Article(models.Model):
	class Meta():
		db_table='Article'

	article_title=models.CharField(max_length=200)
	article_text=models.TextField()
	article_date=models.DateTimeField('Дата публикации')
	article_likes=models.IntegerField(default=0)

class Comment(models.Model):
	class Meta():
		db_table='Comment'

	comments_text=models.TextField()
	comments_article=models.ForeignKey(Article)
