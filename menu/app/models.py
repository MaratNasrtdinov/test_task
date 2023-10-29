from django.db import models


class Elements(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=200, blank=True, null=True, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Elements'

    def subelems(self):
        return self.elements_set.all()

    def get_last_items(self):
        if self.parent:
            return self.parent.get_last_items() + [self.parent.id]
        else:
            return []

    def __str__(self):
        return self.name
