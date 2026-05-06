from typing import List
from models.mueble import Mueble


class Catalogo:
    """
    Clase encargada de gestionar el inventario de muebles y realizar 
    operaciones de búsqueda y filtrado.
    """

    def __init__(self, inventario: List[Mueble] = None):
        self._inventario: List[Mueble] = inventario if inventario is not None else []

    def agregar(self, mueble: Mueble):
        """Agrega un mueble al catálogo."""
        self._inventario.append(mueble)

    def obtener_todos(self) -> List[Mueble]:
        """Devuelve la lista completa de muebles."""
        return self._inventario

    def buscar_por_nombre(self, nombre: str) -> List[Mueble]:
        """Busca muebles cuyo nombre contenga la cadena buscada (case-insensitive)."""
        if not nombre:
            return []

        busqueda = nombre.lower()
        return [
            m for m in self._inventario
            if busqueda in m.nombre.lower()
        ]

    def filtrar_por_material(self, material: str) -> List[Mueble]:
        """Filtra muebles por coincidencia exacta de material."""
        if not material:
            return []

        material_buscado = material.lower()
        return [
            m for m in self._inventario
            if m.material.lower() == material_buscado
        ]

    def filtrar_por_precio(self, min_precio: float, max_precio: float) -> List[Mueble]:
        """
        Filtra muebles dentro de un rango de precio inclusivo.
        Incluye manejo de errores para asegurar que la comparación sea numérica.
        """
        try:
            min_p = float(min_precio)
            max_p = float(max_precio)
        except (ValueError, TypeError):
            return []

        resultado = []
        for m in self._inventario:
            try:
                precio_actual = float(m.calcular_precio())
                if min_p <= precio_actual <= max_p:
                    resultado.append(m)
            except (ValueError, TypeError):
                continue

        return resultado