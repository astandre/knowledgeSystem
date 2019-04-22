from django.db import models


# Create your models here.
class Context(models.Model):
    url = models.CharField(max_length=300)
    prefix = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.url


class Key(models.Model):
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    property = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return "%s%s" % (self.context, self.property)


class Subject(models.Model):
    context = models.ForeignKey(Context, on_delete=models.CASCADE)
    value = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return "%s:%s" % (self.context, self.value)


class Predicate(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return "%s:%s" % (self.key, self.subject)


class Object(models.Model):
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
    predicate = models.ForeignKey(Predicate, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    label = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        if self.predicate is None:
            return "%s" % self.subject
        else:
            return "%s" % self.label


