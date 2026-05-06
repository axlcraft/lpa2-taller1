import pytest
from src.models.concretos.silla import Silla


class TestSilla:

    @pytest.fixture
    def silla_basica(self):
        return Silla(
            nombre="Silla Básica",
            material="Madera",
            color="Marrón",
            precio_base=50.0,
        )

    @pytest.fixture
    def silla_oficina(self):
        return Silla(
            nombre="Silla Oficina",
            material="Metal",
            color="Negro",
            precio_base=100.0,
            altura_regulable=True,
            tiene_ruedas=True,
            material_tapizado="Tela"
        )

    @pytest.fixture
    def silla_comedor(self):
        return Silla(
            nombre="Silla Comedor",
            material="Madera",
            color="Blanco",
            precio_base=80.0,
            tiene_respaldo=True,
            material_tapizado="Cuero"
        )

    # Pruebas de instanciación
    def test_instanciacion_correcta(self, silla_basica):
        assert silla_basica.nombre == "Silla Básica"
        assert silla_basica.material == "Madera"
        assert silla_basica.color == "Marrón"
        assert silla_basica.precio_base == 50.0

    def test_instanciacion_con_opciones(self, silla_oficina):
        assert silla_oficina.altura_regulable is True
        assert silla_oficina.tiene_ruedas is True

    # Pruebas de propiedades
    def test_propiedad_altura_regulable_getter(self, silla_basica):
        assert silla_basica.altura_regulable is False

    def test_propiedad_altura_regulable_setter(self, silla_basica):
        silla_basica.altura_regulable = True
        assert silla_basica.altura_regulable is True

    def test_propiedad_tiene_ruedas_getter(self, silla_basica):
        assert silla_basica.tiene_ruedas is False

    def test_propiedad_tiene_ruedas_setter(self, silla_basica):
        silla_basica.tiene_ruedas = True
        assert silla_basica.tiene_ruedas is True

    # Pruebas de cálculo de precio
    def test_calcular_precio(self, silla_basica):
        precio = silla_basica.calcular_precio()
        assert precio >= 50.0
        assert isinstance(precio, (int, float))

    def test_calcular_precio_con_altura_regulable(self, silla_oficina):
        # Precio base 100 * factor de comodidad + 30 (altura) + 20 (ruedas)
        precio = silla_oficina.calcular_precio()
        assert precio > 100.0

    def test_calcular_precio_sin_extras(self, silla_basica):
        # Sin altura regulable ni ruedas, solo precio base con factor
        precio = silla_basica.calcular_precio()
        assert isinstance(precio, float)

    # Pruebas de descripción
    def test_obtener_descripcion(self, silla_basica):
        descripcion = silla_basica.obtener_descripcion()
        assert "Silla Básica" in descripcion
        assert "Madera" in descripcion
        assert "Marrón" in descripcion

    def test_obtener_descripcion_contiene_altura_regulable(self, silla_basica, silla_oficina):
        desc_basica = silla_basica.obtener_descripcion()
        assert "Altura regulable: No" in desc_basica

        desc_oficina = silla_oficina.obtener_descripcion()
        assert "Altura regulable: Sí" in desc_oficina

    def test_obtener_descripcion_contiene_ruedas(self, silla_basica, silla_oficina):
        desc_basica = silla_basica.obtener_descripcion()
        assert "Ruedas: No" in desc_basica

        desc_oficina = silla_oficina.obtener_descripcion()
        assert "Ruedas: Sí" in desc_oficina

    # Pruebas de regular altura
    def test_regular_altura_no_regulable(self, silla_basica):
        resultado = silla_basica.regular_altura(80)
        assert "no tiene altura regulable" in resultado

    def test_regular_altura_valida(self, silla_oficina):
        resultado = silla_oficina.regular_altura(70)
        assert "Altura ajustada a 70 cm" in resultado

    def test_regular_altura_muy_baja(self, silla_oficina):
        resultado = silla_oficina.regular_altura(30)
        assert "debe estar entre 40 y 100 cm" in resultado

    def test_regular_altura_muy_alta(self, silla_oficina):
        resultado = silla_oficina.regular_altura(110)
        assert "debe estar entre 40 y 100 cm" in resultado

    def test_regular_altura_minima_valida(self, silla_oficina):
        resultado = silla_oficina.regular_altura(40)
        assert "Altura ajustada a 40 cm" in resultado

    def test_regular_altura_maxima_valida(self, silla_oficina):
        resultado = silla_oficina.regular_altura(100)
        assert "Altura ajustada a 100 cm" in resultado

    # Pruebas de es_silla_oficina
    def test_es_silla_oficina_verdadero(self, silla_oficina):
        assert silla_oficina.es_silla_oficina() is True

    def test_es_silla_oficina_sin_ruedas(self):
        silla = Silla(
            nombre="Silla Altura Ajustable",
            material="Metal",
            color="Gris",
            precio_base=90.0,
            altura_regulable=True,
            tiene_ruedas=False
        )
        assert silla.es_silla_oficina() is False

    def test_es_silla_oficina_sin_altura_regulable(self):
        silla = Silla(
            nombre="Silla con Ruedas",
            material="Metal",
            color="Azul",
            precio_base=80.0,
            altura_regulable=False,
            tiene_ruedas=True
        )
        assert silla.es_silla_oficina() is False

    def test_es_silla_oficina_basica(self, silla_basica):
        assert silla_basica.es_silla_oficina() is False