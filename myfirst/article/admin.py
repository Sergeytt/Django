from django.contrib import admin
from article.models import Article, Comment


# Register your models here.
class CommentInline(admin.StackedInline):
	model = Comment
	extra = 2

class ArticleAdmin(admin.ModelAdmin):
	fields = ['article_title','article_text','article_date']
	inlines = [CommentInline]
	list_display = ['article_title', 'article_date']
	list_filter = ['article_date']
	
admin.site.register(Article, ArticleAdmin)
