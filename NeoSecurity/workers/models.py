from django.db import models
from django.db.models import UniqueConstraint


class Priority(models.Model):
    name = models.CharField(...)
    code_priority = models.CharField(...)


class Group(models.Model):
    name = models.CharField(...)
    priority = models.ManyToManyField(Priority, through='GroupPriority')


class GroupPriority(models.Model):
    group = models.ForeignKey(Group, related_name='groups', on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, related_name='priority', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['priority', 'group'],
                name='group_worker_unique'
            )
        ]


class Worker(models.Model):
    name = models.CharField(...)
    last_name = models.CharField(...)
    surname = models.CharField(...)
    groups = models.ManyToManyField(Group, through='WorkerGroup', blank=True)


class WorkerGroup(models.Model):
    group = models.ForeignKey(Group, related_name='groups', on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, related_name='workers', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['worker', 'group'],
                name='group_worker_unique'
            )
        ]


class Document(models.Model):
    name = models.CharField(...)
    file = ...
    priorities = models.ManyToManyField(Priority, through='PriorityDocument')


class PriorityDocument(models.Model):
    priority = models.ForeignKey(Priority, related_name='priorities', on_delete=models.CASCADE)
    document = models.ForeignKey(Document, related_name='documents', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['priority', 'document'],
                name='priority_document_unique'
            )
        ]
