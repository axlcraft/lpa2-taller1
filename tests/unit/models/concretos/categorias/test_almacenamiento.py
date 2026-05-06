import pytest
from src.models.categorias.almacenamiento import Almacenamiento


# Clase dummy para poder probar la abstracta
class AlmacenamientoDummy(Almacenamiento):
    def calcular_precio(self) -> float:
        return self.precio_base * self.calcular_factor_almacenamiento()

    def obtener_descripcion(self) -> str:
        return f"Dummy: {self.obtener_info_almacenamiento()}"


class TestAlmacenamiento:

    def test_instanciacion(self):
        obj = AlmacenamientoDummy(
            "Almacen", "Madera", "Blanco", 100.0, 3, 200
        )

        assert obj.nombre == "Almacen"
        assert obj.num_compartimentos == 3
        assert obj.capacidad_litros == 200

    def test_factor_almacenamiento(self):
        obj = AlmacenamientoDummy(
            "Almacen", "Madera", "Blanco", 100.0, 3, 200
        )

        factor = obj.calcular_factor_almacenamiento()

        assert factor > 1.0

    def test_setters_validacion(self):
        obj = AlmacenamientoDummy(
            "Almacen", "Madera", "Blanco", 100.0, 3, 200
        )

        with pytest.raises(ValueError):
            obj.num_compartimentos = 0

        with pytest.raises(ValueError):
            obj.capacidad_litros = -10

    def test_info_almacenamiento(self):
        obj = AlmacenamientoDummy(
            "Almacen", "Madera", "Blanco", 100.0, 2, 150
        )

        info = obj.obtener_info_almacenamiento()

        assert "Compartimentos" in info
        assert "150L" in info

    def test_calcular_precio(self):
        obj = AlmacenamientoDummy(
            "Almacen", "Madera", "Blanco", 100.0, 3, 200
        )

        precio = obj.calcular_precio()

        assert precio > 100

    def test_descripcion(self):
        obj = AlmacenamientoDummy(
            "Almacen", "Madera", "Blanco", 100.0, 3, 200
        )

        desc = obj.obtener_descripcion()

        assert "Dummy" in desc