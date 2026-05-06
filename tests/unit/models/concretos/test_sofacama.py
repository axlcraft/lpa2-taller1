from src.models.concretos.sofacama import SofaCama


class TestSofaCama:

    def test_herencia_multiple(self):
        sofa_cama = SofaCama(
            nombre="Sofá Cama Moderno",
            material="Tela",
            color="Gris",
            precio_base=500.0,
            capacidad_personas=3,
            tamaño_cama="queen",
        )
        assert sofa_cama.capacidad_personas == 3
        assert sofa_cama.nombre == "Sofá Cama Moderno"

    def test_resolucion_metodos(self):
        sofa_cama = SofaCama(
            nombre="Sofá Cama",
            material="Cuero",
            color="Negro",
            precio_base=600.0,
            capacidad_personas=2,
            tamaño_cama="full",
        )
        precio = sofa_cama.calcular_precio()
        assert isinstance(precio, (int, float))
        assert precio > 0