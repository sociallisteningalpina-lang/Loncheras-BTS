#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""

import re
from typing import Callable

def create_topic_classifier() -> Callable[[str], str]:
    """
    Clasificador actualizado para la campaña Back to School Alpina.
    Incluye categoría específica para crisis reputacional en plantas.
    """
    
    def classify_topic(comment: str) -> str:
        comment_lower = str(comment).lower().strip()
        
        # 1. SITUACIÓN DE PLANTA Y LABORAL (Nueva Categoría Prioritaria)
        if re.search(
            r'instalaciones|esclavistas|ministerio|trabajo|clausura|'
            r'plantas|f[aá]brica|maldad|justicia|condena|sucio|'
            r'cancelen|saquen|colombia',
            comment_lower
        ):
            return 'Situación de Planta y Laboral'

        # 2. INGREDIENTES Y SALUD (Azúcar, químicos, nutrición)
        if re.search(
            r'az[uú]car|qu[ií]micos?|nutri|golosinas?|saludable|'
            r'daño|veneno|aditivos|colorantes|reproceso',
            comment_lower
        ):
            return 'Ingredientes y Salud'
            
        # 3. PREGUNTAS SOBRE EL PRODUCTO (Precio, puntos de venta)
        if re.search(
            r'precio|cu[aá]nto vale|d[oó]nde|comprar|tiendas|'
            r'disponible|valor|puntos|promoci[oó]n',
            comment_lower
        ):
            return 'Preguntas sobre el Producto'
            
        # 4. OPINIÓN GENERAL DEL PRODUCTO (Sabor y experiencia)
        if re.search(
            r'rico|bueno|excelente|gusta|delicioso|espectacular|'
            r'encanta|feo|horrible|mal[ií]simo|asco|sabe a',
            comment_lower
        ):
            return 'Opinión General del Producto'
            
        # 5. FUERA DE TEMA / NO RELEVANTE (Religión, emojis, spam)
        if (re.search(r'am[eé]n|dios|gloria|bendici[oó]n|tigre|presidente', comment_lower) 
            or len(comment_lower.split()) < 2):
            return 'Fuera de Tema / No Relevante'
        
        return 'Otros'
    
    return classify_topic

# Ejemplo rápido con tus comentarios:
classifier = create_topic_classifier()
print(classifier("Por esclavistas y no dejar entrar al ministerio")) # Situación de Planta y Laboral
print(classifier("Mejore esas instalaciones")) # Situación de Planta y Laboral
print(classifier("puro azúcar y quimicos")) # Ingredientes y Salud

# --- Ejemplo de uso con tus datos ---
classifier = create_topic_classifier()

test_comments = [
    "Nutritivas??? Solo azúcar",
    "Mejore esas instalaciones",
    "Con todo ese reproceso que le hecha a la leche saborizad",
    "AMÉN. Gloria a Dios.",
    "Platano"
]

for c in test_comments:
    print(f"Comentario: {c} -> Tema: {classifier(c)}")
# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
