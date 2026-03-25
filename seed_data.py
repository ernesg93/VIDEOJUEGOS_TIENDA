"""Script para cargar datos de ejemplo en la base de datos."""
import os
import sys

# Agregar el directorio del proyecto al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tienda_videojuegos'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda_videojuegos.settings')

import django
django.setup()

from catalogo.models import Genero, Producto


def cargar_datos():
    """Carga datos de ejemplo en la base de datos."""
    
    # Crear géneros
    generos_data = [
        {'nombre': 'Acción', 'descripcion': 'Juegos de acción y aventura'},
        {'nombre': 'RPG', 'descripcion': 'Role Playing Games'},
        {'nombre': 'Deportes', 'descripcion': 'Simuladores deportivos'},
        {'nombre': 'Estrategia', 'descripcion': 'Juegos de estrategia y táctica'},
        {'nombre': 'Carreras', 'descripcion': 'Juegos de carreras y conducción'},
    ]

    for g in generos_data:
        Genero.objects.get_or_create(nombre=g['nombre'], defaults={'descripcion': g['descripcion']})

    print(f'Géneros creados: {Genero.objects.count()}')

    # Obtener géneros
    genero_accion = Genero.objects.get(nombre='Acción')
    genero_rpg = Genero.objects.get(nombre='RPG')
    genero_deportes = Genero.objects.get(nombre='Deportes')

    # Crear productos de ejemplo
    productos_data = [
        {
            'titulo': 'The Legend of Zelda: Breath of the Wild',
            'precio': 59.99,
            'stock': 15,
            'plataforma': 'SWITCH',
            'descripcion_corta': 'Una aventura épica en un mundo abierto',
            'descripcion_larga': 'Embárcate en una aventura épica en un mundo vasto y detallado donde puedes explorar libremente. Resuelve puzzles, domina el combate y descubre los secretos del reino de Hyrule.',
            'fecha_lanzamiento': '2017-03-03',
            'edad_minima': 12,
            'genero': genero_accion,
        },
        {
            'titulo': 'Cyberpunk 2077',
            'precio': 59.99,
            'stock': 8,
            'plataforma': 'PC',
            'descripcion_corta': 'RPG futurista de mundo abierto',
            'descripcion_larga': 'Explora Night City, una megalópolis futurista donde la tecnología y la humanidad chocan. Crea tu propio personaje y forja tu destino en esta historia épica.',
            'fecha_lanzamiento': '2020-12-10',
            'edad_minima': 18,
            'genero': genero_rpg,
        },
        {
            'titulo': 'FIFA 24',
            'precio': 69.99,
            'stock': 20,
            'plataforma': 'PS5',
            'descripcion_corta': 'El simulador de fútbol más realista',
            'descripcion_larga': 'Experimenta el fútbol como nunca antes con gráficos de última generación y físicas realistas. Juega con tus equipos favoritos y compite online.',
            'fecha_lanzamiento': '2023-09-29',
            'edad_minima': 3,
            'genero': genero_deportes,
        },
    ]

    for p in productos_data:
        titulo = p.pop('titulo')
        genero = p.pop('genero')
        Producto.objects.get_or_create(
            titulo=titulo,
            defaults={
                **p,
                'genero': genero,
                'activo': True
            }
        )

    print(f'Productos creados: {Producto.objects.count()}')
    print('¡Datos de ejemplo cargados correctamente!')


if __name__ == '__main__':
    cargar_datos()