from django.db import models


# Create your models here.
class About(models.Model):
    image = models.ImageField(upload_to='about')
    video = models.FileField(upload_to='about_video')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=+True)

    def __str__(self):
        return self.image


class Team(models.Model):
    name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='team_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=+True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Users(models.Model):
    First_name = models.CharField(max_length=212)
    Last_name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='users')
    phone = models.CharField(max_length=212)
    email = models.CharField(max_length=212)
    password = models.CharField(max_length=212)
    region = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=+True)

    def __str__(self):
        return self.First_name


class Client(models.Model):
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    video_id = models.OneToOneField(About, on_delete=models.CASCADE)
    is_pay = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id


class Payment(models.Model):
    price = models.IntegerField()
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=+True)

    def __str__(self):
        return self.price


class Websites(models.Model):
    name = models.CharField(max_length=212)
    link = models.CharField(max_length=212)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=+True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Web_Images(models.Model):
    website_id = models.ForeignKey(Websites, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='web_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=+True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.website_id.name


class Video_lessons(models.Model):
    name = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='video_lessons')
    video = models.FileField(upload_to='video_lessons')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=+True)
    deleted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

