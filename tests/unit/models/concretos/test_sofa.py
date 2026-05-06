import pytest
from src.models.concretos.sofa import Sofa


class TestSofa:

    def test_instanciacion(self):
        sofa = Sofa("Sofa Moderno", "Cuero", "Negro", 500.0, 3)

        assert sofa.nombre == "Sofa Moderno"
        assert sofa.material == "Cuero"
        assert sofa.color == "Negro"
        assert sofa.capacidad_personas == 3

    def test_calcular_precio(self):
        sofa = Sofa(
            "Sofa", "Tela", "Gris", 500.0,
            capacidad_personas=3,
            tiene_brazos=True,
            es_modular=True,
            incluye_cojines=True
        )

        precio = sofa.calcular_precio()

        assert isinstance(precio, float)
        assert precio > 500

    def test_propiedades(self):
        sofa = Sofa("Sofa", "Tela", "Azul", 400.0)

        assert sofa.tiene_brazos is True
        assert sofa.es_modular is False
        assert sofa.incluye_cojines is False

    def test_descripcion(self):
        sofa = Sofa("Sofa Test", "Tela", "Rojo", 300.0)

        desc = sofa.obtener_descripcion()

        assert "Sofá" in desc
        assert "Rojo" in desc