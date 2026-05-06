import pytest
from src.models.categorias.asientos import Asiento


# Clase dummy para probar la abstracta
class AsientoDummy(Asiento):
    def calcular_precio(self) -> float:
        return self.precio_base * self.calcular_factor_comodidad()

    def obtener_descripcion(self) -> str:
        return f"Dummy: {self.obtener_info_asiento()}"


class TestAsiento:

    def test_instanciacion(self):
        asiento = AsientoDummy(
            "Silla", "Madera", "Negro", 100.0, 2, True, "tela"
        )

        assert asiento.nombre == "Silla"
        assert asiento.capacidad_personas == 2
        assert asiento.tiene_respaldo is True
        assert asiento.material_tapizado == "tela"

    def test_factor_comodidad(self):
        asiento = AsientoDummy(
            "Silla", "Madera", "Negro", 100.0, 3, True, "cuero"
        )

        factor = asiento.calcular_factor_comodidad()

        assert factor > 1.0

    def test_factor_comodidad_sin_tapizado(self):
        asiento = AsientoDummy(
            "Silla", "Madera", "Negro", 100.0, 1, False, None
        )

        factor = asiento.calcular_factor_comodidad()

        assert factor == 1.0  # caso base

    def test_setters_validacion(self):
        asiento = AsientoDummy(
            "Silla", "Madera", "Negro", 100.0, 2, True
        )

        with pytest.raises(ValueError):
            asiento.capacidad_personas = 0

    def test_info_asiento(self):
        asiento = AsientoDummy(
            "Silla", "Madera", "Negro", 100.0, 2, True, "tela"
        )

        info = asiento.obtener_info_asiento()

        assert "Capacidad" in info
        assert "Respaldo" in info
        assert "tela" in info

    def test_calcular_precio(self):
        asiento = AsientoDummy(
            "Silla", "Madera", "Negro", 100.0, 2, True, "cuero"
        )

        precio = asiento.calcular_precio()

        assert precio > 100

    def test_descripcion(self):
        asiento = AsientoDummy(
            "Silla", "Madera", "Negro", 100.0, 2, True
        )

        desc = asiento.obtener_descripcion()

        assert "Dummy" in desc