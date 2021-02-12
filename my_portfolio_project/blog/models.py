from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	# If a variable is defined in a Class, not even necessarily in the __init__(), you access it with self.var
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	# write a get_absolute_url function so that we can return the absolute url to this post's specific url 
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

"""SQL CODE FOR POST database
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;"""

"""Methods for database models
First run "python manage.py shell"

User.objects.all(), User.objects.first(), User.objects.last(), User.objects.filter(username='MEWINWIN').first(), 
User.objects.get(id=1), 
Use "." to access attributes like normal

post_1 = Post(title='Blog 1', content='First Post Content!', author=user), Post.objects.all(), post_1.save()
post_2 = Post(title='Blog 1', content='First Post Content!', author_id=user.id)
post_1.author.email

To access a specific user's posts, user_object.modelname_set
user.post_set.all(), user.post_set.first(), user.post_set.create(title='Blog 3', content='Third post content')
"""