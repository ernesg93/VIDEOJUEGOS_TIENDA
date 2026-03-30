from django.core.management.base import BaseCommand

from catalogo.models import Producto


PRODUCTOS = [
    {
        "titulo": "The Legend of Zelda: Breath of the Wild",
        "precio": 59.99,
        "plataforma": "SWITCH",
        "stock": 15,
        "activo": True,
    },
    {
        "titulo": "Cyberpunk 2077",
        "precio": 49.99,
        "plataforma": "PC",
        "stock": 20,
        "activo": True,
    },
    {
        "titulo": "God of War Ragnarok",
        "precio": 54.99,
        "plataforma": "PS5",
        "stock": 12,
        "activo": True,
    },
    {
        "titulo": "Halo Infinite",
        "precio": 39.99,
        "plataforma": "XBOX",
        "stock": 18,
        "activo": True,
    },
    {
        "titulo": "Elden Ring",
        "precio": 59.99,
        "plataforma": "PC",
        "stock": 25,
        "activo": True,
    },
    {
        "titulo": "Spider-Man 2",
        "precio": 69.99,
        "plataforma": "PS5",
        "stock": 10,
        "activo": True,
    },
    {
        "titulo": "Mario Kart 8 Deluxe",
        "precio": 59.99,
        "plataforma": "SWITCH",
        "stock": 22,
        "activo": True,
    },
    {
        "titulo": "Forza Horizon 5",
        "precio": 39.99,
        "plataforma": "XBOX",
        "stock": 16,
        "activo": True,
    },
    {
        "titulo": "Red Dead Redemption 2",
        "precio": 44.99,
        "plataforma": "PC",
        "stock": 14,
        "activo": True,
    },
    {
        "titulo": "Hogwarts Legacy",
        "precio": 49.99,
        "plataforma": "PS5",
        "stock": 11,
        "activo": True,
    },
    {
        "titulo": "Resident Evil 4",
        "precio": 39.99,
        "plataforma": "PS5",
        "stock": 13,
        "activo": True,
    },
    {
        "titulo": "Starfield",
        "precio": 59.99,
        "plataforma": "XBOX",
        "stock": 9,
        "activo": True,
    },
    {
        "titulo": "Street Fighter 6",
        "precio": 34.99,
        "plataforma": "PC",
        "stock": 17,
        "activo": True,
    },
    {
        "titulo": "Baldur's Gate 3",
        "precio": 59.99,
        "plataforma": "PC",
        "stock": 12,
        "activo": True,
    },
    {
        "titulo": "Metroid Prime Remastered",
        "precio": 39.99,
        "plataforma": "SWITCH",
        "stock": 10,
        "activo": True,
    },
    {
        "titulo": "Final Fantasy VII Rebirth",
        "precio": 69.99,
        "plataforma": "PS5",
        "stock": 8,
        "activo": True,
    },
    {
        "titulo": "Sea of Thieves",
        "precio": 29.99,
        "plataforma": "XBOX",
        "stock": 19,
        "activo": True,
    },
    {
        "titulo": "Assassin's Creed Mirage",
        "precio": 44.99,
        "plataforma": "PC",
        "stock": 11,
        "activo": True,
    },
    {
        "titulo": "Diablo IV",
        "precio": 49.99,
        "plataforma": "PS5",
        "stock": 15,
        "activo": True,
    },
    {
        "titulo": "Splatoon 3",
        "precio": 54.99,
        "plataforma": "SWITCH",
        "stock": 14,
        "activo": True,
    },
]


class Command(BaseCommand):
    help = 'Populate database with sample video game products'

    def handle(self, *args, **kwargs):
        """Create sample products if they don't exist."""
        created_count = 0
        for producto_data in PRODUCTOS:
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
