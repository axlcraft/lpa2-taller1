import pytest
from src.models.concretos.cama import Cama


class TestCama:

    def test_instanciacion_correcta(self):
        cama = Cama("Cama 1", "Madera", "Blanco", 500, "queen", True, True)

        assert cama.nombre == "Cama 1"
        assert cama.material == "Madera"
        assert cama.color == "Blanco"
        assert cama.precio_base == 500
        assert cama.tamaño == "queen"
        assert cama.incluye_colchon is True
        assert cama.tiene_cabecera is True

    def test_setter_tamaño_valido(self):
        cama = Cama("Cama 2", "Metal", "Negro", 300)

        cama.tamaño = "king"

        assert cama.tamaño == "king"

    def test_setter_tamaño_invalido(self):
        cama = Cama("Cama 3", "Madera", "Gris", 400)

        with pytest.raises(ValueError):
            cama.tamaño = "gigante"  # no permitido

    def test_calcular_precio_basico(self):
        cama = Cama("Cama 4", "Madera", "Blanco", 200, "individual", False, False)

        precio = cama.calcular_precio()

        assert precio == 200

    def test_calcular_precio_con_tamaño(self):
        cama = Cama("Cama 5", "Madera", "Blanco", 200, "queen", False, False)

        precio = cama.calcular_precio()

        # 200 + 400
        assert precio == 600

    def test_calcular_precio_completo(self):
        cama = Cama("Cama 6", "Madera", "Blanco", 200, "king", True, True)

        precio = cama.calcular_precio()

        # 200 + 600 + 300 + 100 = 1200
        assert precio == 1200

    def test_obtener_descripcion(self):
        cama = Cama("Cama 7", "Madera", "Blanco", 300, "matrimonial", True, False)

        desc = cama.obtener_descripcion()

        assert "Cama 7" in desc
        assert "Madera" in desc
        assert "Blanco" in desc
        assert "matrimonial" in desc
        assert "Incluye colchón: Sí" in desc