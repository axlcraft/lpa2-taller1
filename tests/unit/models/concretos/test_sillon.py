from src.models.concretos.sillon import Sillon


class TestSillon:

    def test_instanciacion_correcta(self):
        sillon = Sillon(
            "Sillón 1", "Cuero", "Negro", 500,
            3, True, "cuero", True, True, True
        )

        assert sillon.nombre == "Sillón 1"
        assert sillon.material == "Cuero"
        assert sillon.color == "Negro"
        assert sillon.precio_base == 500
        assert sillon.capacidad_personas == 3
        assert sillon.tiene_respaldo is True
        assert sillon.material_tapizado == "cuero"
        assert sillon.tiene_brazos is True
        assert sillon.es_reclinable is True
        assert sillon.tiene_reposapiés is True

    def test_calcular_precio_basico(self):
        sillon = Sillon("Sillón 2", "Madera", "Blanco", 200)

        precio = sillon.calcular_precio()

        # Solo precio base + brazos (True por defecto)
        # 200 + 100 = 300
        assert precio == 300

    def test_calcular_precio_con_tapizado(self):
        sillon = Sillon(
            "Sillón 3", "Madera", "Blanco", 200,
            material_tapizado="tela"
        )

        precio = sillon.calcular_precio()

        # 200 + 200 (tapizado) + 100 (brazos)
        assert precio == 500

    def test_calcular_precio_completo(self):
        sillon = Sillon(
            "Sillón 4", "Metal", "Gris", 200,
            material_tapizado="cuero",
            tiene_brazos=True,
            es_reclinable=True,
            tiene_reposapiés=True
        )

        precio = sillon.calcular_precio()

        # 200 + 200 + 100 + 250 + 80 = 830
        assert precio == 830

    def test_obtener_descripcion(self):
        sillon = Sillon(
            "Sillón 5", "Madera", "Negro", 300,
            2, True, "tela", True, False, True
        )

        desc = sillon.obtener_descripcion()

        assert "Sillón 5" in desc
        assert "Madera" in desc
        assert "Negro" in desc
        assert "Capacidad=2" in desc
        assert "Tapizado=tela" in desc
        assert "Brazos=Sí" in desc
        assert "Reposapiés=Sí" in desc