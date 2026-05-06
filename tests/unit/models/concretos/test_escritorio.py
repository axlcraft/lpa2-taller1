from src.models.concretos.escritorio import Escritorio


class TestEscritorio:

    def test_instanciacion_correcta(self):
        escritorio = Escritorio(
            "Escritorio 1", "Madera", "Negro", 300,
            "L", True, 2, 1.8, True
        )

        assert escritorio.nombre == "Escritorio 1"
        assert escritorio.material == "Madera"
        assert escritorio.color == "Negro"
        assert escritorio.precio_base == 300
        assert escritorio.forma == "L"
        assert escritorio.tiene_cajones is True
        assert escritorio.num_cajones == 2
        assert escritorio.largo == 1.8
        assert escritorio.tiene_iluminacion is True

    def test_calcular_precio_basico(self):
        escritorio = Escritorio(
            "Escritorio 2", "Madera", "Blanco", 200
        )

        precio = escritorio.calcular_precio()

        # Sin extras
        assert precio == 200

    def test_calcular_precio_con_cajones(self):
        escritorio = Escritorio(
            "Escritorio 3", "Madera", "Blanco", 200,
            tiene_cajones=True, num_cajones=3
        )

        precio = escritorio.calcular_precio()

        # 200 + (3 * 25) = 275
        assert precio == 275

    def test_calcular_precio_completo(self):
        escritorio = Escritorio(
            "Escritorio 4", "Metal", "Gris", 200,
            forma="L",
            tiene_cajones=True,
            num_cajones=2,
            largo=2.0,
            tiene_iluminacion=True
        )

        precio = escritorio.calcular_precio()

        # 200 + (2*25) + 50 + 40 + 30 = 200 + 50 + 50 + 40 + 30 = 370
        assert precio == 370

    def test_obtener_descripcion(self):
        escritorio = Escritorio(
            "Escritorio 5", "Madera", "Blanco", 250,
            forma="L",
            tiene_cajones=True,
            num_cajones=2,
            largo=1.6,
            tiene_iluminacion=True
        )

        desc = escritorio.obtener_descripcion()

        assert "Escritorio 5" in desc
        assert "Madera" in desc
        assert "Blanco" in desc
        assert "Forma=L" in desc
        assert "Cajones=2" in desc
        assert "Iluminación=Sí" in desc