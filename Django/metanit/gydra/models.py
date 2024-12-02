from django.db import models
import csv


class ExampleTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


if __name__ == '__main__':

    with open(r'"C:\Users\Sashok\Downloads\Microsoft_Access_Database.accdb"', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ExampleTable.objects.create(**row)
