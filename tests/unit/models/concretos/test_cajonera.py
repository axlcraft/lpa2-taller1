from src.models.concretos.cajonera import Cajonera


class TestCajonera:

    def test_instanciacion_correcta(self):
        cajonera = Cajonera("Cajonera 1", "Madera", "Blanco", 200, 4, True)

        assert cajonera.nombre == "Cajonera 1"
        assert cajonera.material == "Madera"
        assert cajonera.color == "Blanco"
        assert cajonera.precio_base == 200
        assert cajonera.num_cajones == 4
        assert cajonera.tiene_ruedas is True

    def test_calcular_precio_sin_ruedas(self):
        cajonera = Cajonera("Cajonera 2", "Madera", "Negro", 100, 3, False)

        precio = cajonera.calcular_precio()

        # 100 + (3 * 20) = 160
        assert precio == 160

    def test_calcular_precio_con_ruedas(self):
        cajonera = Cajonera("Cajonera 3", "Metal", "Gris", 100, 3, True)

        precio = cajonera.calcular_precio()

        # 100 + (3 * 20) + 30 = 190
        assert precio == 190

    def test_obtener_descripcion(self):
        cajonera = Cajonera("Cajonera 4", "Madera", "Blanco", 150, 2, True)

        descripcion = cajonera.obtener_descripcion()

        assert "Cajonera 4" in descripcion
        assert "Madera" in descripcion
        assert "Blanco" in descripcion
        assert "Cajones=2" in descripcion
        assert "Ruedas=Sí" in descripcion