from src.models.concretos.armario import Armario


class TestArmario:

    def test_instanciacion_correcta(self):
        armario = Armario("Armario 1", "Madera", "Blanco", 500, 3, 2, True)

        assert armario.nombre == "Armario 1"
        assert armario.material == "Madera"
        assert armario.color == "Blanco"
        assert armario.precio_base == 500
        assert armario.num_puertas == 3
        assert armario.num_cajones == 2
        assert armario.tiene_espejos is True

    def test_calcular_precio_sin_extras(self):
        armario = Armario("Armario 2", "Madera", "Negro", 200, 2, 0, False)

        precio = armario.calcular_precio()

        # 200 + (2*50) = 300
        assert precio == 300

    def test_calcular_precio_con_cajones_y_espejos(self):
        armario = Armario("Armario 3", "Metal", "Gris", 300, 2, 3, True)

        precio = armario.calcular_precio()

        # 300 + (2*50) + (3*30) + 100 = 300 + 100 + 90 + 100 = 590
        assert precio == 590

    def test_obtener_descripcion(self):
        armario = Armario("Armario 4", "Madera", "Blanco", 400, 4, 1, True)

        descripcion = armario.obtener_descripcion()

        assert "Armario 4" in descripcion
        assert "Madera" in descripcion
        assert "Blanco" in descripcion
        assert "Puertas=4" in descripcion
        assert "Cajones=1" in descripcion
        assert "Espejos=Sí" in descripcion