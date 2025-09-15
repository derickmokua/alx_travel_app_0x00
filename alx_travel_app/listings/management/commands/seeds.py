from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {"title": "Beach House", "description": "Beautiful house by the beach.", "price_per_night": 120.00, "location": "Miami"},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains.", "price_per_night": 90.00, "location": "Colorado"},
            {"title": "City Apartment", "description": "Modern apartment in downtown.", "price_per_night": 150.00, "location": "New York"},
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))

