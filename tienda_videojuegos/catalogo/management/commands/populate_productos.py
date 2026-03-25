from django.core.management.base import BaseCommand
from catalogo.models import Producto


class Command(BaseCommand):
    help = 'Populate database with sample video game products'

    def handle(self, *args, **kwargs):
        """Create sample products if they don't exist."""
        productos = [
            {
                "titulo": "The Legend of Zelda: Breath of the Wild",
                "precio": 59.99,
                "plataforma": "SWITCH",
                "stock": 15,
                "activo": True
            },
            {
                "titulo": "Cyberpunk 2077",
                "precio": 49.99,
                "plataforma": "PC",
                "stock": 20,
                "activo": True
            },
            {
                "titulo": "God of War Ragnarök",
                "precio": 54.99,
                "plataforma": "PS5",
                "stock": 12,
                "activo": True
            },
            {
                "titulo": "Halo Infinite",
                "precio": 39.99,
                "plataforma": "XBOX",
                "stock": 18,
                "activo": True
            },
            {
                "titulo": "Elden Ring",
                "precio": 59.99,
                "plataforma": "PC",
                "stock": 25,
                "activo": True
            },
            {
                "titulo": "Spider-Man 2",
                "precio": 69.99,
                "plataforma": "PS5",
                "stock": 10,
                "activo": True
            },
            {
                "titulo": "Mario Kart 8 Deluxe",
                "precio": 59.99,
                "plataforma": "SWITCH",
                "stock": 22,
                "activo": True
            },
            {
                "titulo": "Forza Horizon 5",
                "precio": 39.99,
                "plataforma": "XBOX",
                "stock": 16,
                "activo": True
            },
        ]

        created_count = 0
        for producto_data in productos:
            producto, created = Producto.objects.get_or_create(
                titulo=producto_data["titulo"],
                defaults=producto_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created: {producto.titulo}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Already exists: {producto.titulo}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\nCompleted! Created {created_count} new products.'
            )
        )
