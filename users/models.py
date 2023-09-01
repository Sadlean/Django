from django.db import models
from django.contrib.auth.models import User
from PIL import Image


CHOICES = (('male', 'Мужской пол'), ('female', 'Женский пол'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    # OneToOneField - ссылка на конкретную запись из другой таблички
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')
    gender = models.CharField(choices=CHOICES, max_length=20, default='male')
    mails = models.BooleanField('Соглашение на отправку уведомлений на почту', default=False)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'

