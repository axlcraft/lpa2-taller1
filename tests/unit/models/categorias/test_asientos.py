import pytest
from src.models.concretos.silla import Silla
from src.models.concretos.sofa import Sofa
from src.models.concretos.sillon import Sillon


class TestAsientos:
    """Tests para la categoría Asientos"""

    @pytest.fixture
    def silla_basica(self):
        return Silla(
            nombre="Silla Estándar",
            material="Madera",
            color="Natural",
            precio_base=100.0,
            tiene_respaldo=True,
            material_tapizado="tela"
        )

    @pytest.fixture
    def sofa_basico(self):
        return Sofa(
            nombre="Sofá Cómodo",
            material="Tela",
            color="Gris",
            precio_base=600.0,
            capacidad_personas=3,
            tiene_respaldo=True,
            material_tapizado="tela"
        )

    @pytest.fixture
    def sillon_basico(self):
        return Sillon(
            nombre="Sillón Reclinable",
            material="Cuero",
            color="Marrón",
            precio_base=400.0,
            es_reclinable=True
        )

    # Pruebas de setters en capacidad_personas
    def test_propiedad_capacidad_personas_setter(self, silla_basica):
        silla_basica.capacidad_personas = 2
        assert silla_basica.capacidad_personas == 2

    def test_propiedad_capacidad_personas_setter_invalido(self, silla_basica):
        with pytest.raises(ValueError, match="debe ser mayor a 0"):
            silla_basica.capacidad_personas = 0

    def test_propiedad_capacidad_personas_setter_negativo(self, silla_basica):
        with pytest.raises(ValueError, match="debe ser mayor a 0"):
            silla_basica.capacidad_personas = -1

    # Pruebas de setters en tiene_respaldo
    def test_propiedad_tiene_respaldo_setter(self, silla_basica):
        silla_basica.tiene_respaldo = False
        assert silla_basica.tiene_respaldo is False

    def test_propiedad_tiene_respaldo_setter_true(self, silla_basica):
        silla_basica.tiene_respaldo = True
        assert silla_basica.tiene_respaldo is True

    # Pruebas de setters en material_tapizado
    def test_propiedad_material_tapizado_setter(self, silla_basica):
        silla_basica.material_tapizado = "cuero"
        assert silla_basica.material_tapizado == "cuero"

    def test_propiedad_material_tapizado_setter_none(self, silla_basica):
        silla_basica.material_tapizado = None
        assert silla_basica.material_tapizado is None

    # Pruebas de calcular_factor_comodidad
    def test_calcular_factor_comodidad_con_respaldo(self, silla_basica):
        # Factor = 1.0 + 0.1 (respaldo) + 0.1 (tela) + (1-1)*0.05 = 1.2
        factor = silla_basica.calcular_factor_comodidad()
        assert factor == pytest.approx(1.2, 0.01)

    def test_calcular_factor_comodidad_con_cuero(self):
        silla = Silla("Silla", "Cuero", "Negro", 100.0, tiene_respaldo=True,
                      material_tapizado="cuero")
        # Factor = 1.0 + 0.1 (respaldo) + 0.2 (cuero) + (1-1)*0.05 = 1.3
        factor = silla.calcular_factor_comodidad()
        assert factor == pytest.approx(1.3, 0.01)

    def test_calcular_factor_comodidad_sin_tapizado(self):
        silla = Silla("Silla", "Madera", "Natural", 100.0,
                      tiene_respaldo=True, material_tapizado=None)
        # Factor = 1.0 + 0.1 (respaldo) + 0 (sin tapizado) + 0 = 1.1
        factor = silla.calcular_factor_comodidad()
        assert factor == pytest.approx(1.1, 0.01)

    def test_calcular_factor_comodidad_sofa_multiusuario(self, sofa_basico):
        # Factor = 1.0 + 0.1 (respaldo) + 0.1 (tela) + (3-1)*0.05 = 1.3
        factor = sofa_basico.calcular_factor_comodidad()
        assert factor == pytest.approx(1.3, 0.01)

    # Pruebas de obtener_info_asiento
    def test_obtener_info_asiento_silla(self, silla_basica):
        info = silla_basica.obtener_info_asiento()
        assert "Capacidad: 1 personas" in info
        assert "Respaldo: Sí" in info
        assert "Tapizado: tela" in info

    def test_obtener_info_asiento_sofa(self, sofa_basico):
        info = sofa_basico.obtener_info_asiento()
        assert "Capacidad: 3 personas" in info
        assert "Respaldo: Sí" in info

    def test_obtener_info_asiento_sin_tapizado(self):
        silla = Silla("Silla", "Madera", "Natural", 100.0,
                      tiene_respaldo=False, material_tapizado=None)
        info = silla.obtener_info_asiento()
        assert "Capacidad: 1 personas" in info
        assert "Respaldo: No" in info
        assert "Tapizado:" not in info

    # Pruebas de compatibilidad
    def test_metodos_abstractos_implementados(self, silla_basica, sofa_basico, sillon_basico):
        # Verificar que los métodos abstractos están implementados
        assert hasattr(silla_basica, 'calcular_precio')
        assert callable(getattr(silla_basica, 'calcular_precio'))
        assert hasattr(sofa_basico, 'obtener_descripcion')
        assert callable(getattr(sofa_basico, 'obtener_descripcion'))
