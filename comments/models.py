# from django.db import models
# from django.contrib.auth.models import User
# from main import models as main_model
#
# class Comment(models.Model):
#     post = models.ForeignKey(main_model.Movie )
#     name = models.ForeignKey(User)
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ('created',)
#
#     def __str__(self):
#         return 'Comment by {} on {}'.format(self.name, self.post)