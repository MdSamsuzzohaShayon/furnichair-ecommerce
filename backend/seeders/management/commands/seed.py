import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from accounts.models import User, Address
from contacts.models import Contact
from products.models import Category, Product, DeliveryPlace
from orders.models import Order
from wishlist.models import Wishlist

fake = Faker()

BD_CITIES = [
    "Dhaka", "Chattogram", "Khulna", "Rajshahi", "Sylhet",
    "Barishal", "Rangpur", "Mymensingh", "Comilla", "Narayanganj",
]

CLOUDINARY_IMAGES = [
    "ecom/fz4fcirraaur7ewmfqkk.jpg",
    "ecom/gu3pdiwuemudkfoh3sqq.jpg",
    "ecom/c8w4z7vg7dmdrlvwvq49.jpg",
    "ecom/eermrzp5z4tyvugmpzkb.jpg",
    "ecom/nowosbb4m7wblft1bxfq.jpg",
    "ecom/oy7ewtbs85jfa8p3ftcf.jpg",
    "ecom/liaxg0jx7vwlx70aqny7.jpg",
    "ecom/hquk9zhu0jeextkmaj5y.jpg",
    "ecom/my7hadpufbrjxq2wiwwl.jpg",
    "ecom/pel1d9fj60i4d7rcuffp.jpg",
    "ecom/mrv7mwzs7wdq6iisbsgb.jpg",
    "ecom/gakgs6qyuvp0drmvcdzy.png",
    "ecom/vipmrpvjoymvd1qhgkpu.png",
    "ecom/p6tcjt6nhgzuvjkrme5s.png",
]

CLOUDINARY_IMAGES = list(set(CLOUDINARY_IMAGES))

class Command(BaseCommand):
    help = "Seed the database with random data for all apps"

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete existing seeded data before seeding",
        )

    def handle(self, *args, **options):
        if options["flush"]:
            self.flush_data()

        with transaction.atomic():
            categories = self.seed_categories()
            products = self.seed_products(categories)
            delivery_places = self.seed_delivery_places()
            users = self.seed_users()
            addresses = self.seed_addresses(users)
            self.seed_orders(users, products, addresses, delivery_places)
            self.seed_contacts()
            self.seed_wishlist()

        self.stdout.write(self.style.SUCCESS("✅ Database seeded successfully!"))

    # ---------------- Cleanup ----------------
    def flush_data(self):
        self.stdout.write("Flushing existing data...")
        Order.objects.all().delete()
        Wishlist.objects.all().delete()
        Contact.objects.all().delete()
        Address.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        DeliveryPlace.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

    # ---------------- Category ----------------
    def seed_categories(self):
        self.stdout.write("Seeding categories...")

        category_names = [
            "Sofas", "Chairs", "Tables", "Beds",
            "Wardrobes", "Bookshelves", "Office Furniture", "Outdoor Furniture",
        ]

        # safer than sample (avoids crash if images < categories)
        images = CLOUDINARY_IMAGES.copy()
        random.shuffle(images)

        def get_image(index: int):
            """Cycle images safely if not enough"""
            return images[index % len(images)]

        parents = []

        # ---------------- PARENT CATEGORIES ----------------
        for i, name in enumerate(category_names):
            category, _ = Category.objects.get_or_create(
                name=name,
                defaults={
                    "image": get_image(i),
                    "shipping_charge": random.randint(50, 200),
                },
            )
            parents.append(category)

        # ---------------- CHILD CATEGORIES ----------------
        children = []

        for parent in parents:
            for _ in range(2):
                child_name = f"{parent.name} - {fake.word().capitalize()}"

                category, _ = Category.objects.get_or_create(
                    name=child_name,
                    defaults={
                        "parent": parent,
                        "image": get_image(random.randint(0, len(images) - 1)),
                        "shipping_charge": random.randint(50, 200),
                    },
                )

                children.append(category)

        return parents + children
    # ---------------- Product ----------------
    def seed_products(self, categories):
        self.stdout.write("Seeding products...")
        products = []
        for _ in range(30):
            price = random.randint(2000, 50000)
            discount = price - random.randint(0, int(price * 0.3))
            title = f"{fake.word().capitalize()} {fake.word().capitalize()} {random.randint(100, 999)}"

            images = random.sample(CLOUDINARY_IMAGES, 4)

            product, _ = Product.objects.get_or_create(
                title=title,
                defaults={
                    "price": Decimal(price),
                    "discount_price": Decimal(discount),
                    "total_stock": Decimal(random.randint(0, 200)),
                    "description": fake.paragraph(nb_sentences=5),
                    "category": random.choice(categories),
                    # Cloudinary images (IMPORTANT)
                    "image1": images[0],
                    "image2": images[1],
                    "image3": images[2],
                    "image4": images[3],
                },
            )
            products.append(product)
        return products

    # ---------------- DeliveryPlace ----------------
    def seed_delivery_places(self):
        self.stdout.write("Seeding delivery places...")
        places = []
        for city in BD_CITIES:
            place, _ = DeliveryPlace.objects.get_or_create(
                place=city,
                defaults={"price": random.randint(50, 500)},
            )
            places.append(place)
        return places

    # ---------------- User ----------------
    def seed_users(self):
        self.stdout.write("Seeding users...")
        users = []
        for _ in range(10):
            email = fake.unique.email()
            user = User.objects.create_user(
                email=email,
                password="password123",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                is_validated=True,
            )
            users.append(user)
        return users

    # ---------------- Address ----------------
    def seed_addresses(self, users):
        self.stdout.write("Seeding addresses...")
        addresses = []
        for user in users:
            address = Address.objects.create(
                user=user,
                city=random.choice(BD_CITIES),
                country="Bangladesh",
                phone=random.randint(1000000000, 1999999999),
                area=fake.street_address(),
            )
            addresses.append(address)
        return addresses

    # ---------------- Order ----------------
    def seed_orders(self, users, products, addresses, delivery_places):
        self.stdout.write("Seeding orders...")
        status_keys = [choice[0] for choice in Order.STATUS_CHOICES]

        for _ in range(20):
            buyer = random.choice(users)
            product = random.choice(products)
            address = random.choice(addresses)
            city = random.choice(delivery_places)
            quantity = random.randint(1, 5)

            shipping = (city.price + (product.category.shipping_charge if product.category else 0))
            total = int(product.discount_price) * quantity + shipping * quantity

            Order.objects.create(
                status=random.choice(status_keys),
                is_paid=random.choice([True, False]),
                buyer=buyer,
                product=product,
                address=address,
                city=city,
                quantity=quantity,
                total=total,
            )

    # ---------------- Contact ----------------
    def seed_contacts(self):
        self.stdout.write("Seeding contacts...")
        for _ in range(10):
            Contact.objects.create(
                name=fake.name(),
                email=fake.email(),
                message=fake.paragraph(nb_sentences=3),
                preview=random.choice([True, False]),
            )

    # ---------------- Wishlist ----------------
    def seed_wishlist(self):
        self.stdout.write("Seeding wishlist...")
        for _ in range(10):
            Wishlist.objects.create(
                email=fake.unique.email(),
                preview=random.choice([True, False]),
            )