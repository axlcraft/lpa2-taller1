import pytest
from src.models.concretos.mesa import Mesa
from src.models.concretos.escritorio import Escritorio


class TestSuperficies:
    """Tests para la categoría Superficies (testeando muebles concretos)"""

    @pytest.fixture
    def mesa_basica(self):
        return Mesa(
            nombre="Mesa Comedor",
            material="Madera",
            color="Roble",
            precio_base=400,
            forma="rectangular",
            capacidad_personas=6
        )

    @pytest.fixture
    def escritorio_basico(self):
        return Escritorio(
            nombre="Escritorio Oficina",
            material="MDF",
            color="Blanco",
            precio_base=300,
            forma="rectangular",
            tiene_cajones=True,
            num_cajones=3,
            tiene_iluminacion=True
        )

    # Pruebas de instanciación
    def test_instanciacion_mesa(self, mesa_basica):
        assert mesa_basica.nombre == "Mesa Comedor"
        assert mesa_basica.material == "Madera"
        assert mesa_basica.color == "Roble"
        assert mesa_basica.precio_base == 400
        assert mesa_basica.forma == "rectangular"
        assert mesa_basica.capacidad_personas == 6

    def test_instanciacion_escritorio(self, escritorio_basico):
        assert escritorio_basico.nombre == "Escritorio Oficina"
        assert escritorio_basico.material == "MDF"
        assert escritorio_basico.color == "Blanco"
        assert escritorio_basico.precio_base == 300
        assert escritorio_basico.tiene_cajones is True
        assert escritorio_basico.num_cajones == 3

    # Pruebas de cálculo de precio
    def test_calcular_precio_mesa(self, mesa_basica):
        precio = mesa_basica.calcular_precio()
        assert isinstance(precio, (int, float))
        assert precio > 0

    def test_calcular_precio_escritorio(self, escritorio_basico):
        precio = escritorio_basico.calcular_precio()
        assert isinstance(precio, (int, float))
        assert precio > 0

    # Pruebas de descripción
    def test_obtener_descripcion_mesa(self, mesa_basica):
        descripcion = mesa_basica.obtener_descripcion()
        assert "Mesa" in descripcion
        assert "Comedor" in descripcion

    def test_obtener_descripcion_escritorio(self, escritorio_basico):
        descripcion = escritorio_basico.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0

    # Pruebas de mesas con diferentes formas
    def test_mesa_forma_redonda(self):
        mesa = Mesa(
            nombre="Mesa Redonda",
            material="Vidrio",
            color="Transparente",
            precio_base=500,
            forma="redonda",
            capacidad_personas=4
        )
        assert mesa.forma == "redonda"

    def test_mesa_forma_cuadrada(self):
        mesa = Mesa(
            nombre="Mesa Pequeña",
            material="Madera",
            color="Natural",
            precio_base=200,
            forma="cuadrada",
            capacidad_personas=4
        )
        assert mesa.forma == "cuadrada"
        assert mesa.capacidad_personas == 4

    # Pruebas de escritorios con distintas características
    def test_escritorio_con_iluminacion(self):
        escritorio = Escritorio(
            nombre="Escritorio Moderno",
            material="Acero",
            color="Gris",
            precio_base=450,
            tiene_iluminacion=True
        )
        assert escritorio.tiene_iluminacion is True

    def test_escritorio_sin_iluminacion(self):
        escritorio = Escritorio(
            nombre="Escritorio Simple",
            material="Madera",
            color="Nogal",
            precio_base=250,
            tiene_iluminacion=False
        )
        assert escritorio.tiene_iluminacion is False

    def test_escritorio_sin_cajones(self):
        escritorio = Escritorio(
            nombre="Escritorio Abierto",
            material="MDF",
            color="Blanco",
            precio_base=200,
            tiene_cajones=False,
            num_cajones=0
        )
        assert escritorio.tiene_cajones is False
