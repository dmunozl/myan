from django.contrib.auth.models import AbstractUser


class MyanUser(AbstractUser):
    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.email

    class Meta:
        app_label = 'myan_core'
        ordering = ['first_name']
