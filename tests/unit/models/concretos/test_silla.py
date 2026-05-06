import pytest
from src.models.concretos.silla import Silla


class TestSilla:

    @pytest.fixture
    def silla_basica(self):
        return Silla(
            nombre="Silla Básica",
            material="Madera",
            color="Marrón",
            precio_base=50.0,
        )

    def test_instanciacion_correcta(self, silla_basica):
        assert silla_basica.nombre == "Silla Básica"
        assert silla_basica.material == "Madera"
        assert silla_basica.color == "Marrón"
        assert silla_basica.precio_base == 50.0

    def test_calcular_precio(self, silla_basica):
        precio = silla_basica.calcular_precio()
        assert precio >= 50.0
        assert isinstance(precio, (int, float))

    def test_obtener_descripcion(self, silla_basica):
        descripcion = silla_basica.obtener_descripcion()
        assert "Silla Básica" in descripcion
        assert "Madera" in descripcion
        assert "Marrón" in descripcion