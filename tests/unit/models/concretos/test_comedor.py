import pytest
from src.models.concretos.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


class TestComedor:

    @pytest.fixture
    def mesa_basica(self):
        return Mesa("Mesa Familiar", "Madera", "Roble", 500.0,
                    forma="rectangular", capacidad_personas=6)

    @pytest.fixture
    def silla_basica(self):
        return Silla("Silla", "Madera", "Roble", 120.0, tiene_respaldo=True)

    @pytest.fixture
    def comedor_basico(self, mesa_basica, silla_basica):
        sillas = [silla_basica for _ in range(4)]
        return Comedor(mesa=mesa_basica, sillas=sillas)

    @pytest.fixture
    def comedor_vacio(self, mesa_basica):
        return Comedor(mesa=mesa_basica)

    def test_inicializacion_con_sillas(self, comedor_basico):
        assert comedor_basico.mesa is not None
        assert len(comedor_basico.sillas) == 4

    def test_inicializacion_sin_sillas(self, comedor_vacio):
        assert comedor_vacio.mesa is not None
        assert len(comedor_vacio.sillas) == 0

    def test_calcular_precio_total(self, comedor_basico):
        precio_total = comedor_basico.calcular_precio_total()
        assert isinstance(precio_total, float)
        assert precio_total > 0

    def test_agregar_silla(self, comedor_vacio, silla_basica):
        comedor_vacio.agregar_silla(silla_basica)
        assert len(comedor_vacio.sillas) == 1

    def test_quitar_silla_existente(self, comedor_basico, silla_basica):
        comedor_basico.quitar_silla(silla_basica)
        assert len(comedor_basico.sillas) == 3

    def test_quitar_silla_no_existente(self, comedor_basico, mesa_basica):
        # Una mesa no es una silla, así que no debería hacerse nada
        initial_count = len(comedor_basico.sillas)
        comedor_basico.quitar_silla(mesa_basica)
        assert len(comedor_basico.sillas) == initial_count

    def test_cantidad_sillas(self, comedor_basico):
        assert comedor_basico.cantidad_sillas() == 4

    def test_cantidad_sillas_vacio(self, comedor_vacio):
        assert comedor_vacio.cantidad_sillas() == 0

    def test_descripcion(self, comedor_basico):
        descripcion = comedor_basico.descripcion()
        assert isinstance(descripcion, str)
        assert "Comedor con mesa:" in descripcion
        assert "sillas:" in descripcion
        assert len(comedor_basico.sillas) == 4