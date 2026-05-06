import pytest
from src.models.concretos.sofacama import SofaCama


class TestSofaCama:

    @pytest.fixture
    def sofacama_basica(self):
        return SofaCama(
            nombre="Sofá Cama Moderno",
            material="Tela",
            color="Gris",
            precio_base=500.0,
            capacidad_personas=3,
            material_tapizado="microfibra",
            tamaño_cama="queen",
        )

    @pytest.fixture
    def sofacama_king(self):
        return SofaCama(
            nombre="Sofá Cama King",
            material="Cuero",
            color="Negro",
            precio_base=800.0,
            capacidad_personas=4,
            tamaño_cama="king",
            incluye_colchon=True,
            mecanismo_conversion="electrico"
        )

    @pytest.fixture
    def sofacama_sin_colchon(self):
        return SofaCama(
            nombre="Sofá Cama Sin Colchón",
            material="Tela",
            color="Beige",
            precio_base=400.0,
            tamaño_cama="matrimonial",
            incluye_colchon=False
        )

    # Pruebas de inicialización y herencia
    def test_herencia_multiple(self, sofacama_basica):
        assert sofacama_basica.capacidad_personas == 3
        assert sofacama_basica.nombre == "Sofá Cama Moderno"
        assert sofacama_basica.material == "Tela"
        assert sofacama_basica.color == "Gris"

    def test_resolucion_metodos(self, sofacama_basica):
        precio = sofacama_basica.calcular_precio()
        assert isinstance(precio, (int, float))
        assert precio > 0

    # Pruebas de cálculo de precio
    def test_calcular_precio_matrimonial(self, sofacama_sin_colchon):
        # Sofá: 400*1.2 + 150 (brazos) = 630
        # Matrimonial: +300, Sin colchón: +0, plegable: +0
        # Total: 630 + 300 = 930
        precio = sofacama_sin_colchon.calcular_precio()
        assert precio == pytest.approx(930, 0.1)

    def test_calcular_precio_queen(self, sofacama_basica):
        # Sofá: 500*1.2 + 150 (brazos) = 750
        # Queen: +500, Colchón: +250, plegable: +0
        # Total: 750 + 500 + 250 = 1500
        precio = sofacama_basica.calcular_precio()
        assert precio == pytest.approx(1500, 0.1)

    def test_calcular_precio_king(self, sofacama_king):
        # Sofá: 800*1.2 + 150 (brazos) = 1110
        # King: +700, Colchón: +250, eléctrico: +300
        # Total: 1110 + 700 + 250 + 300 = 2360
        precio = sofacama_king.calcular_precio()
        assert precio == pytest.approx(2360, 0.1)

    def test_calcular_precio_con_colchon(self, sofacama_basica):
        assert sofacama_basica.incluye_colchon is True
        precio = sofacama_basica.calcular_precio()
        assert precio > 0

    def test_calcular_precio_sin_colchon(self, sofacama_sin_colchon):
        assert sofacama_sin_colchon.incluye_colchon is False
        precio = sofacama_sin_colchon.calcular_precio()
        assert precio > 0

    def test_calcular_precio_mecanismo_plegable(self):
        sofacama = SofaCama(
            nombre="Sofá Cama Plegable",
            material="Tela",
            color="Azul",
            precio_base=500.0,
            mecanismo_conversion="plegable"
        )
        # Sofá: 500*1.2 + 150 (brazos) = 750
        # Matrimonial default: +300, Colchón default: +250, plegable: +0
        # Total: 750 + 300 + 250 = 1300
        precio = sofacama.calcular_precio()
        assert precio == pytest.approx(1300, 0.1)

    def test_calcular_precio_mecanismo_hidraulico(self):
        sofacama = SofaCama(
            nombre="Sofá Cama Hidráulico",
            material="Cuero",
            color="Rojo",
            precio_base=600.0,
            mecanismo_conversion="hidraulico"
        )
        # Sofá: 600*1.4 (cuero) + 150 (brazos) = 990
        # Matrimonial default: +300, Colchón default: +250, hidráulico: +150
        # Total: 990 + 300 + 250 + 150 = 1690
        precio = sofacama.calcular_precio()
        assert precio == pytest.approx(1690, 0.1)

    # Pruebas de propiedades
    def test_propiedad_mecanismo_conversion(self, sofacama_basica):
        assert sofacama_basica.mecanismo_conversion == "plegable"

    def test_propiedad_modo_actual_inicial(self, sofacama_basica):
        assert sofacama_basica.modo_actual == "sofa"

    def test_propiedad_tamaño(self, sofacama_basica):
        assert sofacama_basica.tamaño == "queen"

    def test_propiedad_tamaño_cama(self, sofacama_basica):
        assert sofacama_basica.tamaño_cama == "queen"

    def test_propiedad_incluye_colchon(self, sofacama_basica, sofacama_sin_colchon):
        assert sofacama_basica.incluye_colchon is True
        assert sofacama_sin_colchon.incluye_colchon is False

    # Pruebas de conversión a cama
    def test_convertir_a_cama(self, sofacama_basica):
        resultado = sofacama_basica.convertir_a_cama()
        assert "Sofá convertido a cama" in resultado
        assert sofacama_basica.modo_actual == "cama"

    def test_convertir_a_cama_ya_es_cama(self, sofacama_basica):
        sofacama_basica.convertir_a_cama()
        resultado = sofacama_basica.convertir_a_cama()
        assert "ya está en modo cama" in resultado

    # Pruebas de conversión a sofá
    def test_convertir_a_sofa(self, sofacama_basica):
        sofacama_basica.convertir_a_cama()  # Primero convertir a cama
        resultado = sofacama_basica.convertir_a_sofa()
        assert "Cama convertida a sofá" in resultado
        assert sofacama_basica.modo_actual == "sofa"

    def test_convertir_a_sofa_ya_es_sofa(self, sofacama_basica):
        resultado = sofacama_basica.convertir_a_sofa()
        assert "ya está en modo sofá" in resultado

    def test_convertir_multiples_veces(self, sofacama_basica):
        # Convertir múltiples veces
        sofacama_basica.convertir_a_cama()
        assert sofacama_basica.modo_actual == "cama"
        sofacama_basica.convertir_a_sofa()
        assert sofacama_basica.modo_actual == "sofa"
        sofacama_basica.convertir_a_cama()
        assert sofacama_basica.modo_actual == "cama"

    # Pruebas de descripción
    def test_obtener_descripcion(self, sofacama_basica):
        descripcion = sofacama_basica.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert "Sofá-Cama:" in descripcion
        assert sofacama_basica.nombre in descripcion
        assert sofacama_basica.material in descripcion
        assert sofacama_basica.color in descripcion

    def test_obtener_descripcion_contiene_tamaño(self, sofacama_basica):
        descripcion = sofacama_basica.obtener_descripcion()
        assert "Tamaño como cama:" in descripcion
        assert "queen" in descripcion.lower()

    def test_obtener_descripcion_contiene_colchon(self, sofacama_basica, sofacama_sin_colchon):
        desc1 = sofacama_basica.obtener_descripcion()
        assert "Incluye colchón: Sí" in desc1

        desc2 = sofacama_sin_colchon.obtener_descripcion()
        assert "Incluye colchón: No" in desc2

    def test_obtener_descripcion_contiene_mecanismo(self, sofacama_basica):
        descripcion = sofacama_basica.obtener_descripcion()
        assert "Mecanismo:" in descripcion

    def test_obtener_descripcion_contiene_modo(self, sofacama_basica):
        descripcion_inicial = sofacama_basica.obtener_descripcion()
        assert "Modo actual: sofa" in descripcion_inicial

        sofacama_basica.convertir_a_cama()
        descripcion_cama = sofacama_basica.obtener_descripcion()
        assert "Modo actual: cama" in descripcion_cama

    # Pruebas de compatibilidad de herencia
    def test_metodos_sofa_disponibles(self, sofacama_basica):
        # Métodos heredados de Sofa
        assert hasattr(sofacama_basica, 'obtener_info_asiento')
        assert callable(getattr(sofacama_basica, 'obtener_info_asiento'))

    def test_metodos_cama_disponibles(self, sofacama_basica):
        # Métodos heredados de Cama
        assert hasattr(sofacama_basica, 'tamaño_cama')
        assert hasattr(sofacama_basica, 'incluye_colchon')