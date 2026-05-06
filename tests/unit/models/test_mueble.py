import pytest
from src.models.concretos.silla import Silla


class TestMuebleBase:
    """
    Cubre la clase abstracta Mueble a través de Silla.
    Líneas faltantes: setters con validación (44-46, 56-58, 68-70, 80-82) y __str__ (111).
    """

    @pytest.fixture
    def silla(self):
        return Silla("Silla Test", "madera", "negro", 80.0)

    # setter nombre
    def test_setter_nombre_valido(self, silla):
        silla.nombre = "Nueva Silla"
        assert silla.nombre == "Nueva Silla"

    def test_setter_nombre_vacio_error(self, silla):
        with pytest.raises(ValueError):
            silla.nombre = ""

    def test_setter_nombre_espacios_error(self, silla):
        with pytest.raises(ValueError):
            silla.nombre = "   "

    # setter material
    def test_setter_material_valido(self, silla):
        silla.material = "metal"
        assert silla.material == "metal"

    def test_setter_material_vacio_error(self, silla):
        with pytest.raises(ValueError):
            silla.material = ""

    def test_setter_material_espacios_error(self, silla):
        with pytest.raises(ValueError):
            silla.material = "   "

    # setter color
    def test_setter_color_valido(self, silla):
        silla.color = "azul"
        assert silla.color == "azul"

    def test_setter_color_vacio_error(self, silla):
        with pytest.raises(ValueError):
            silla.color = ""

    def test_setter_color_espacios_error(self, silla):
        with pytest.raises(ValueError):
            silla.color = "   "

    # setter precio_base
    def test_setter_precio_valido(self, silla):
        silla.precio_base = 200.0
        assert silla.precio_base == 200.0

    def test_setter_precio_cero_valido(self, silla):
        silla.precio_base = 0
        assert silla.precio_base == 0

    def test_setter_precio_negativo_error(self, silla):
        with pytest.raises(ValueError):
            silla.precio_base = -1

    # __str__ (línea 111)
    def test_str(self, silla):
        resultado = str(silla)
        assert "madera" in resultado
        assert "negro" in resultado

    def test_repr(self, silla):
        resultado = repr(silla)
        assert "nombre=" in resultado or "Mueble(" in resultado