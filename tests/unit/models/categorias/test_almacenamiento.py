import pytest
from src.models.concretos.armario import Armario
from src.models.concretos.cajonera import Cajonera


class TestAlmacenamiento:
    """Tests para la categoría Almacenamiento (testeando muebles concretos)"""

    @pytest.fixture
    def armario_basico(self):
        return Armario(
            nombre="Armario Clásico",
            material="Madera",
            color="Castaño",
            precio_base=600,
            num_puertas=3,
            num_cajones=2,
            tiene_espejos=False
        )

    @pytest.fixture
    def cajonera_basica(self):
        return Cajonera(
            nombre="Cajonera 5 Cajones",
            material="MDF",
            color="Blanco",
            precio_base=300,
            num_cajones=5,
            tiene_ruedas=False
        )

    # Pruebas de instanciación
    def test_instanciacion_armario(self, armario_basico):
        assert armario_basico.nombre == "Armario Clásico"
        assert armario_basico.material == "Madera"
        assert armario_basico.color == "Castaño"
        assert armario_basico.precio_base == 600
        assert armario_basico.num_puertas == 3
        assert armario_basico.num_cajones == 2
        assert armario_basico.tiene_espejos is False

    def test_instanciacion_cajonera(self, cajonera_basica):
        assert cajonera_basica.nombre == "Cajonera 5 Cajones"
        assert cajonera_basica.material == "MDF"
        assert cajonera_basica.color == "Blanco"
        assert cajonera_basica.precio_base == 300

    # Pruebas de cálculo de precio
    def test_calcular_precio_armario(self, armario_basico):
        precio = armario_basico.calcular_precio()
        assert isinstance(precio, (int, float))
        assert precio > 0

    def test_calcular_precio_cajonera(self, cajonera_basica):
        precio = cajonera_basica.calcular_precio()
        assert isinstance(precio, (int, float))
        assert precio > 0

    # Pruebas de descripción
    def test_obtener_descripcion_armario(self, armario_basico):
        descripcion = armario_basico.obtener_descripcion()
        assert "Armario" in descripcion
        assert "Clásico" in descripcion

    def test_obtener_descripcion_cajonera(self, cajonera_basica):
        descripcion = cajonera_basica.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0

    # Pruebas de propiedades
    def test_armario_con_espejos(self):
        armario = Armario(
            nombre="Armario con Espejo",
            material="Madera",
            color="Blanco",
            precio_base=700,
            tiene_espejos=True
        )
        assert armario.tiene_espejos is True

    def test_armario_sin_cajones(self):
        armario = Armario(
            nombre="Armario Sin Cajones",
            material="MDF",
            color="Natural",
            precio_base=400,
            num_cajones=0
        )
        assert armario.num_cajones == 0

    def test_cajonera_con_ruedas(self):
        cajonera = Cajonera(
            nombre="Cajonera Móvil",
            material="Acero",
            color="Gris",
            precio_base=500,
            tiene_ruedas=True
        )
        assert cajonera.tiene_ruedas is True

    def test_cajonera_sin_ruedas(self):
        cajonera = Cajonera(
            nombre="Cajonera Fija",
            material="Madera",
            color="Nogal",
            precio_base=300,
            tiene_ruedas=False
        )
        assert cajonera.tiene_ruedas is False
