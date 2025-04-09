from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('question-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_posted']


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    likes = models.ManyToManyField(User, related_name='liked_answers', blank=True)
    
    def __str__(self):
        return f"Answer to {self.question.title} by {self.author.username}"
    
    def total_likes(self):
        return self.likes.count()
    
    class Meta:
        ordering = ['-date_posted']