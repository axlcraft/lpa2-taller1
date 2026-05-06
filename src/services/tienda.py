"""
Servicio de la tienda que maneja la lógica de negocio.
Esta clase implementa el patrón de servicio para separar la lógica de negocio de la UI.
"""

from typing import List, Dict

from models.mueble import Mueble
from models.composicion.comedor import Comedor


class TiendaMuebles:

    def __init__(self, nombre_tienda: str = "Mueblería OOP"):
        self._nombre = nombre_tienda
        self._inventario: List[Mueble] = []
        self._comedores: List[Comedor] = []
        self._ventas_realizadas: List[Dict] = []
        self._descuentos_activos: Dict[str, float] = {}
        self._total_muebles_vendidos: int = 0
        self._valor_total_ventas: float = 0.0

    # ------------------------------------------------------------------
    # Propiedades
    # ------------------------------------------------------------------

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def inventario(self):
        return self._inventario

    @property
    def descuentos_activos(self):
        return self._descuentos_activos

    # ------------------------------------------------------------------
    # Compatibilidad con test_tienda.py (agregar_producto / vender_producto)
    # ------------------------------------------------------------------

    def agregar_producto(self, producto: Mueble) -> bool:
        self._inventario.append(producto)
        print(f"Agregado: {getattr(producto, 'nombre', 'producto')}")
        return True

    def vender_producto(self, nombre: str) -> bool:
        for m in self._inventario:
            if getattr(m, "nombre", None) == nombre:
                self._inventario.remove(m)
                self._ventas_realizadas.append(m)
                print(f"Vendido: {nombre}")
                return True
        return False

    # ------------------------------------------------------------------
    # Inventario
    # ------------------------------------------------------------------

    def agregar_mueble(self, mueble: "Mueble") -> str:
        if mueble is None:
            return "Error: El mueble no puede ser None"
        try:
            precio = mueble.calcular_precio()
            if precio <= 0:
                return "Error: El mueble debe tener un precio válido mayor a 0"
        except Exception as e:
            return f"Error al calcular precio del mueble: {str(e)}"
        self._inventario.append(mueble)
        return f"Mueble {getattr(mueble, 'nombre', str(mueble))} agregado exitosamente al inventario"

    def agregar_comedor(self, comedor: "Comedor") -> str:
        if comedor is None:
            return "Error: El comedor no puede ser None"
        self._comedores.append(comedor)
        return f"Comedor {getattr(comedor, 'nombre', str(comedor))} agregado exitosamente"

    # ------------------------------------------------------------------
    # Búsqueda y filtros
    # ------------------------------------------------------------------

    def buscar_muebles_por_nombre(self, nombre: str) -> List["Mueble"]:
        if not nombre or not nombre.strip():
            return []
        nombre_lower = nombre.lower().strip()
        return [m for m in self._inventario if nombre_lower in m.nombre.lower()]

    def filtrar_por_precio(
        self, precio_min: float = 0, precio_max: float = float("inf")
    ) -> List["Mueble"]:
        if precio_min < 0:
            precio_min = 0
        resultados = []
        for mueble in self._inventario:
            try:
                precio = mueble.calcular_precio()
                if precio_min <= precio <= precio_max:
                    resultados.append(mueble)
            except Exception:
                continue
        return resultados

    def filtrar_por_material(self, material: str) -> List["Mueble"]:
        if not material or not material.strip():
            return []
        material_lower = material.lower().strip()
        resultados = []
        for mueble in self._inventario:
            try:
                if (
                    hasattr(mueble, "material")
                    and mueble.material
                    and mueble.material.lower().strip() == material_lower
                ):
                    resultados.append(mueble)
            except Exception:
                continue
        return resultados

    # ------------------------------------------------------------------
    # Descuentos
    # ------------------------------------------------------------------

    def aplicar_descuento(self, categoria: str, porcentaje: float) -> str:
        if not 0 < porcentaje <= 100:
            return "Error: El porcentaje debe estar entre 1 y 100"
        categoria_lower = categoria.lower().strip()
        if categoria_lower.endswith("s"):
            categoria_lower = categoria_lower[:-1]
        categoria_clase = categoria_lower.capitalize()
        self._descuentos_activos[categoria_clase] = porcentaje / 100
        return f"Descuento del {porcentaje}% aplicado a la categoría '{categoria_clase}'"

    # ------------------------------------------------------------------
    # Ventas
    # ------------------------------------------------------------------

    def realizar_venta(
        self, mueble: "Mueble", cliente: str = "Cliente Anónimo"
    ) -> Dict:
        if mueble not in self._inventario:
            return {"error": "El mueble no está disponible en inventario"}
        try:
            precio_original = mueble.calcular_precio()
            descuento_aplicado = 0
            tipo_mueble = type(mueble).__name__
            if self._descuentos_activos and tipo_mueble in self._descuentos_activos:
                descuento_aplicado = self._descuentos_activos[tipo_mueble]
            precio_final = precio_original * (1 - descuento_aplicado)
            from datetime import datetime
            nombre_mueble = getattr(mueble, "nombre", None) or tipo_mueble
            venta = {
                "mueble": nombre_mueble,
                "cliente": cliente,
                "precio_original": precio_original,
                "descuento": descuento_aplicado * 100,
                "precio_final": round(precio_final, 2),
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            self._ventas_realizadas.append(venta)
            self._inventario.remove(mueble)
            self._total_muebles_vendidos += 1
            self._valor_total_ventas += venta["precio_final"]
            return venta
        except Exception as e:
            return {"error": f"Error al procesar la venta: {str(e)}"}

    # ------------------------------------------------------------------
    # Estadísticas y reporte
    # ------------------------------------------------------------------

    def obtener_estadisticas(self) -> dict:
        try:
            total_muebles = len(self._inventario)
            total_comedores = len(self._comedores)
            valor_inventario = 0
            for mueble in self._inventario:
                try:
                    valor_inventario += mueble.calcular_precio()
                except Exception:
                    pass
            tipos_muebles = {}
            for mueble in self._inventario:
                tipo = type(mueble).__name__
                tipos_muebles[tipo] = tipos_muebles.get(tipo, 0) + 1
            ventas_realizadas = len(self._ventas_realizadas)
            return {
                "total_muebles": total_muebles,
                "total_comedores": total_comedores,
                "valor_inventario": valor_inventario,
                "tipos_muebles": tipos_muebles,
                "descuentos_activos": self._descuentos_activos.copy(),
                "ventas_realizadas": ventas_realizadas,
                "ventas": ventas_realizadas,
                "total_muebles_vendidos": self._total_muebles_vendidos,
                "valor_total_ventas": self._valor_total_ventas,
            }
        except Exception:
            return {
                "total_muebles": 0,
                "total_comedores": 0,
                "valor_inventario": 0.0,
                "tipos_muebles": {},
                "descuentos_activos": {},
                "ventas_realizadas": 0,
                "ventas": 0,
                "total_muebles_vendidos": 0,
                "valor_total_ventas": 0.0,
            }

    def generar_reporte_inventario(self) -> str:
        estadisticas = self.obtener_estadisticas() or {}
        nombre_tienda = getattr(self, "_nombre", "Tienda")
        reporte = f"=== REPORTE DE INVENTARIO - {nombre_tienda} ===\n\n"
        reporte += f"Total de muebles: {estadisticas.get('total_muebles', 0)}\n"
        reporte += f"Total de comedores: {estadisticas.get('total_comedores', 0)}\n"
        reporte += f"Valor total del inventario: ${estadisticas.get('valor_inventario', 0):.2f}\n\n"
        reporte += "DISTRIBUCIÓN POR TIPOS:\n"
        for tipo, cantidad in (estadisticas.get("tipos_muebles", {}) or {}).items():
            reporte += f"- {tipo}: {cantidad} unidades\n"
        descuentos = estadisticas.get("descuentos_activos", {}) or {}
        if descuentos:
            reporte += "\nDESCUENTOS ACTIVOS:\n"
            for categoria, descuento in descuentos.items():
                reporte += f"- {categoria}: {descuento * 100:.1f}%\n"
        return reporte


# Alias requerido por test_tienda.py
Tienda = TiendaMuebles