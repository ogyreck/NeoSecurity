from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class Grade(models.Model):
    name = models.CharField(max_length=250, verbose_name='Должность')
    priority = models.PositiveSmallIntegerField()


class Group(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название отдела')


class Document(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название документа')
    groups = models.ManyToManyField(Group)
    min_grade = models.ForeignKey(Grade, related_name='grade', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Worker(AbstractUser):
    email = models.EmailField('email', max_length=254)
    first_name = models.CharField('first_name', max_length=150)
    last_name = models.CharField('last_name', max_length=150)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
    groups = models.ManyToManyField(Group, through='WorkerGroup',
                                    through_fields=('worker', 'group'),
                                    )


class WorkerGroup(models.Model):
    group = models.ForeignKey(Group, related_name='groups_in_workers', on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, related_name='workers_in_group', on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, related_name='grades', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['worker', 'group'],
                name='group_worker_unique'
            )
        ]
