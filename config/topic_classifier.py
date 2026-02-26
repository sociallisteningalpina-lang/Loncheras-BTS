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
    Retorna una función de clasificación de temas personalizada para la campaña 
    Back to School Alpina (Yogo Yogo, Alpinito).
    """
    
    def classify_topic(comment: str) -> str:
        comment_lower = str(comment).lower().strip()
        
        # 1. CRÍTICA CORPORATIVA Y LABORAL (Muy presente en tus datos)
        if re.search(
            r'instalaciones|empresa|esclavistas|ministerio|trabajo|'
            r'maldad|justicia|dinero sucio|cancelen|saquen volando',
            comment_lower
        ):
            return 'Crítica Corporativa / Laboral'
            
        # 2. INGREDIENTES Y SALUD (Azúcar y Nutrición)
        if re.search(
            r'az[uú]car|qu[ií]micos?|nutri|golosinas?|saludable|'
            r'daño|veneno|aditivos|colorantes',
            comment_lower
        ):
            return 'Ingredientes y Salud'
            
        # 3. CALIDAD Y PROCESOS DE PRODUCCIÓN
        if re.search(
            r'reproceso|leche saborizada|vencido|calidad|sabor a',
            comment_lower
        ):
            return 'Calidad y Procesos'
            
        # 4. PREGUNTAS SOBRE EL PRODUCTO
        if re.search(
            r'precio|cu[aá]nto vale|d[oó]nde|comprar|tiendas|'
            r'disponible|valor|puntos|promoci[oó]n',
            comment_lower
        ):
            return 'Preguntas sobre el Producto'
            
        # 5. OPINIÓN GENERAL (Positiva o Negativa sobre el sabor)
        if re.search(
            r'rico|bueno|excelente|gusta|delicioso|espectacular|'
            r'encanta|feo|horrible|mal[ií]simo|asco',
            comment_lower
        ):
            return 'Opinión General del Producto'
            
        # 6. FUERA DE TEMA / NO RELEVANTE (Religión, Política, Emojis o palabras sueltas)
        # Captura "Amén", "Dios", "Gloria", "Presidente" y comentarios de menos de 2 palabras
        if (re.search(r'am[eé]n|dios|gloria|bendici[oó]n|tigre|presidente', comment_lower) 
            or len(comment_lower.split()) < 2):
            return 'Fuera de Tema / No Relevante'
        
        # CATEGORÍA DEFAULT
        return 'Otros'
    
    return classify_topic

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
