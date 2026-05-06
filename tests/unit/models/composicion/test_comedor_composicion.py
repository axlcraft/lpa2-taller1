import pytest
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


class TestComisorComposicion:
    """Tests para la clase Comedor que implementa composición."""

    @pytest.fixture
    def mesa_basica(self):
        return Mesa("Mesa Familiar", "Madera", "Roble", 500.0,
                    forma="rectangular", capacidad_personas=6)

    @pytest.fixture
    def silla_basica(self):
        return Silla("Silla Básica", "Madera", "Roble", 120.0, tiene_respaldo=True)

    @pytest.fixture
    def comedor_basico(self, mesa_basica, silla_basica):
        sillas = [silla_basica for _ in range(3)]
        return Comedor("Comedor Familiar", mesa=mesa_basica, sillas=sillas)

    @pytest.fixture
    def comedor_vacio(self, mesa_basica):
        return Comedor("Comedor Vacío", mesa=mesa_basica)

    # Pruebas de inicialización
    def test_inicializacion_con_sillas(self, comedor_basico):
        assert comedor_basico.nombre == "Comedor Familiar"
        assert comedor_basico.mesa is not None
        assert len(comedor_basico.sillas) == 3

    def test_inicializacion_sin_sillas(self, comedor_vacio):
        assert comedor_vacio.nombre == "Comedor Vacío"
        assert comedor_vacio.mesa is not None
        assert len(comedor_vacio.sillas) == 0

    # Pruebas de propiedades
    def test_propiedad_nombre(self, comedor_basico):
        assert comedor_basico.nombre == "Comedor Familiar"

    def test_propiedad_mesa(self, comedor_basico):
        assert comedor_basico.mesa is not None

    def test_propiedad_sillas_es_copia(self, comedor_basico):
        sillas_copy = comedor_basico.sillas
        assert len(sillas_copy) == 3
        # Verificar que es una copia (modificar la copia no afecta el original)
        sillas_copy_len_antes = len(comedor_basico.sillas)
        sillas_copy.clear()
        sillas_copy_len_despues = len(comedor_basico.sillas)
        assert sillas_copy_len_antes == sillas_copy_len_despues

    # Pruebas de agregar silla
    def test_agregar_silla_exitosa(self, comedor_vacio, silla_basica):
        resultado = comedor_vacio.agregar_silla(silla_basica)
        assert "exitosamente" in resultado
        assert len(comedor_vacio.sillas) == 1

    def test_agregar_silla_al_maximo(self, comedor_basico, silla_basica):
        # Agregar 3 sillas más para alcanzar el máximo (capacidad de mesa = 6)
        for _ in range(3):
            comedor_basico.agregar_silla(silla_basica)
        # Intentar agregar una séptima
        resultado = comedor_basico.agregar_silla(silla_basica)
        assert "Capacidad máxima" in resultado

    # Pruebas de quitar silla
    def test_quitar_silla_sin_lista(self, comedor_vacio):
        resultado = comedor_vacio.quitar_silla()
        assert "No hay sillas para quitar" in resultado

    def test_quitar_silla_ultima(self, comedor_basico):
        initial_count = len(comedor_basico.sillas)
        resultado = comedor_basico.quitar_silla()
        assert "removida" in resultado
        assert len(comedor_basico.sillas) == initial_count - 1

    def test_quitar_silla_por_indice(self, comedor_basico):
        initial_count = len(comedor_basico.sillas)
        resultado = comedor_basico.quitar_silla(0)
        assert "removida" in resultado
        assert len(comedor_basico.sillas) == initial_count - 1

    def test_quitar_silla_indice_invalido(self, comedor_basico):
        resultado = comedor_basico.quitar_silla(999)
        assert "Índice" in resultado and "inválido" in resultado

    # Pruebas de calcular precio total
    def test_calcular_precio_total(self, comedor_basico):
        precio_total = comedor_basico.calcular_precio_total()
        assert isinstance(precio_total, float)
        assert precio_total > 0

    def test_calcular_precio_con_descuento(self, mesa_basica, silla_basica):
        # Crear comedor con 4 sillas (debe aplicar descuento del 5%)
        sillas = [silla_basica for _ in range(4)]
        comedor = Comedor("Comedor Descuento", mesa=mesa_basica, sillas=sillas)
        precio_total = comedor.calcular_precio_total()
        # Precio: (mesa + 4*silla) * 0.95 = (574 + 4*132) * 0.95 = 1046.9
        assert precio_total == pytest.approx(1046.9, 0.1)

    def test_calcular_precio_sin_descuento(self, mesa_basica, silla_basica):
        # Crear comedor con 3 sillas (sin descuento)
        sillas = [silla_basica for _ in range(3)]
        comedor = Comedor("Comedor Sin Descuento", mesa=mesa_basica, sillas=sillas)
        precio_total = comedor.calcular_precio_total()
        # Precio: mesa + 3*silla = 574 + 3*132 = 970
        assert precio_total == pytest.approx(970, 0.1)

    # Pruebas de descripción completa
    def test_obtener_descripcion_completa(self, comedor_basico):
        descripcion = comedor_basico.obtener_descripcion_completa()
        assert isinstance(descripcion, str)
        assert "COMEDOR COMEDOR FAMILIAR" in descripcion
        assert "MESA:" in descripcion
        assert "SILLAS (3 unidades):" in descripcion

    def test_obtener_descripcion_completa_sin_sillas(self, comedor_vacio):
        descripcion = comedor_vacio.obtener_descripcion_completa()
        assert "SILLAS: Ninguna incluida" in descripcion

    def test_obtener_descripcion_con_descuento(self, mesa_basica, silla_basica):
        sillas = [silla_basica for _ in range(4)]
        comedor = Comedor("Comedor", mesa=mesa_basica, sillas=sillas)
        descripcion = comedor.obtener_descripcion_completa()
        assert "5% de descuento" in descripcion

    # Pruebas de resumen
    def test_obtener_resumen(self, comedor_basico):
        resumen = comedor_basico.obtener_resumen()
        assert isinstance(resumen, dict)
        assert resumen["nombre"] == "Comedor Familiar"
        assert resumen["total_muebles"] == 4  # 1 mesa + 3 sillas
        assert "precio_mesa" in resumen
        assert "precio_sillas" in resumen
        assert "precio_total" in resumen

    def test_obtener_resumen_capacidad(self, comedor_basico):
        resumen = comedor_basico.obtener_resumen()
        assert resumen["capacidad_personas"] == 3  # número de sillas

    def test_obtener_resumen_materiales(self, comedor_basico):
        resumen = comedor_basico.obtener_resumen()
        assert "materiales_utilizados" in resumen
        assert isinstance(resumen["materiales_utilizados"], list)

    # Pruebas de métodos mágicos
    def test_str(self, comedor_basico):
        str_repr = str(comedor_basico)
        assert "Comedor Comedor Familiar" in str_repr
        assert "3 sillas" in str_repr

    def test_len(self, comedor_basico):
        assert len(comedor_basico) == 4  # 1 mesa + 3 sillas

    def test_len_vacio(self, comedor_vacio):
        assert len(comedor_vacio) == 1  # Solo la mesa

    # Pruebas de métodos privados
    def test_obtener_materiales_unicos(self, comedor_basico):
        # El test es indirecto a través de obtener_resumen
        resumen = comedor_basico.obtener_resumen()
        materiales = resumen["materiales_utilizados"]
        assert len(materiales) > 0
        assert "Madera" in materiales or "Roble" in materiales

    def test_calcular_capacidad_maxima(self, comedor_basico):
        # El test es indirecto a través de agregar_silla
        # La capacidad máxima debería ser 6 (capacidad de la mesa)
        silla = comedor_basico.sillas[0]
        for _ in range(3):
            resultado = comedor_basico.agregar_silla(silla)
            if len(comedor_basico.sillas) >= 6:
                break
        # Intentar agregar más
        resultado = comedor_basico.agregar_silla(silla)
        assert "Capacidad máxima" in resultado
