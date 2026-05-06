import pytest
from src.models.categorias.superficies import Superficie


# Clase dummy para probar la abstracta
class SuperficieDummy(Superficie):
    def calcular_precio(self) -> float:
        return self.precio_base * self.calcular_factor_tamaño()

    def obtener_descripcion(self) -> str:
        return f"Dummy: {self.obtener_info_superficie()}"


class TestSuperficie:

    def test_instanciacion(self):
        obj = SuperficieDummy(
            "Mesa", "Madera", "Negro", 100.0, 100, 50, 75
        )

        assert obj.nombre == "Mesa"
        assert obj.largo == 100
        assert obj.ancho == 50
        assert obj.altura == 75

    def test_calcular_area(self):
        obj = SuperficieDummy(
            "Mesa", "Madera", "Negro", 100.0, 100, 50, 75
        )

        area = obj.calcular_area()

        assert area == 5000

    def test_factor_tamano(self):
        obj = SuperficieDummy(
            "Mesa", "Madera", "Negro", 100.0, 100, 100, 75
        )

        factor = obj.calcular_factor_tamaño()

        assert factor > 1.0

    def test_setters_validacion(self):
        obj = SuperficieDummy(
            "Mesa", "Madera", "Negro", 100.0, 100, 50, 75
        )

        with pytest.raises(ValueError):
            obj.largo = 0

        with pytest.raises(ValueError):
            obj.ancho = -10

        with pytest.raises(ValueError):
            obj.altura = 0

    def test_info_superficie(self):
        obj = SuperficieDummy(
            "Mesa", "Madera", "Negro", 100.0, 120, 60, 75
        )

        info = obj.obtener_info_superficie()

        assert "Dimensiones" in info
        assert "120x60x75" in info

    def test_calcular_precio(self):
        obj = SuperficieDummy(
            "Mesa", "Madera", "Negro", 100.0, 100, 100, 75
        )

        precio = obj.calcular_precio()

        assert precio > 100

    def test_descripcion(self):
        obj = SuperficieDummy(
            "Mesa", "Madera", "Negro", 100.0, 100, 50, 75
        )

        desc = obj.obtener_descripcion()

        assert "Dummy" in desc