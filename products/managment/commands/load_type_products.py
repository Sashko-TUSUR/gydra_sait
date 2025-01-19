import json
from django.core.management.base import BaseCommand
from gydra_market.products.models import TypeProduct

class Command(BaseCommand):
    help = 'Loads type products from a JSON file into the database'

    def handle(self, *args, **kwargs):
        with open('path/to/type_products.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                TypeProduct.objects.create(
                    name=item['name'],
                    description=item.get('description', '')
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded type products'))