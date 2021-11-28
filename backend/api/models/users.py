from django.db.models import CharField, Model, EmailField


class Users(Model):
    username = CharField(verbose_name='Name', default='', max_length=100, blank=False)
    email = EmailField(verbose_name='email', default='', max_length=100, blank=False)
    password = CharField(verbose_name='password', default='', max_length=100, blank=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

