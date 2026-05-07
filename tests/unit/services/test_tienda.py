import pytest
from unittest.mock import Mock, patch
from src.services.tienda import Tienda
from src.models.concretos.silla import Silla
from src.models.concretos.mesa import Mesa
from src.models.concretos.cama import Cama
from src.models.composicion.comedor import Comedor

class TestTienda:
    @pytest.fixture
    def tienda_vacia(self):
        return Tienda()

    @pytest.fixture
    def tienda_con_muebles(self):
        tienda = Tienda()
        mesa = Mesa("Mesa Comedor", "Madera", "Roble", 500.0,
                    forma="rectangular", capacidad_personas=6)
        silla = Silla("Silla Madera", "Madera", "Roble", 120.0, tiene_respaldo=True)
        cama = Cama("Cama Matrimonial", "Madera", "Nogal", 800.0, tamaño="matrimonial")
        tienda.agregar_mueble(mesa)
        tienda.agregar_mueble(silla)
        tienda.agregar_mueble(cama)
        return tienda

    @pytest.fixture
    def silla_mock(self):
        mock_silla = Mock(spec=Silla)
        mock_silla.nombre = "Silla Mock"
        mock_silla.calcular_precio.return_value = 75.0
        return mock_silla

    # Pruebas de inicialización
    def test_inicializacion(self, tienda_vacia):
        assert tienda_vacia.nombre == "Mueblería OOP"
        assert len(tienda_vacia.inventario) == 0
        assert tienda_vacia.descuentos_activos == {}

    # Pruebas de agregar producto
    def test_agregar_producto(self, tienda_vacia, silla_mock):
        tienda_vacia.agregar_producto(silla_mock)
        assert len(tienda_vacia.inventario) == 1
        assert tienda_vacia.inventario[0] == silla_mock

    def test_vender_producto_existente(self, tienda_vacia, silla_mock):
        tienda_vacia.agregar_producto(silla_mock)

        with patch('builtins.print') as mock_print:
            resultado = tienda_vacia.vender_producto("Silla Mock")

            assert resultado is True
            assert len(tienda_vacia.inventario) == 0
            mock_print.assert_called_once()

    def test_vender_producto_inexistente(self, tienda_vacia):
        resultado = tienda_vacia.vender_producto("Producto Inexistente")
        assert resultado is False

    # Pruebas de agregar mueble
    def test_agregar_mueble_valido(self, tienda_vacia):
        mesa = Mesa("Mesa Test", "Madera", "Roble", 500.0,
                    forma="rectangular", capacidad_personas=6)
        resultado = tienda_vacia.agregar_mueble(mesa)
        assert "exitosamente" in resultado
        assert len(tienda_vacia.inventario) == 1

    def test_agregar_mueble_none(self, tienda_vacia):
        resultado = tienda_vacia.agregar_mueble(None)
        assert "Error" in resultado and "None" in resultado

    def test_agregar_comedor(self, tienda_vacia):
        mesa = Mesa("Mesa", "Madera", "Roble", 500.0,
                    forma="rectangular", capacidad_personas=6)
        silla = Silla("Silla", "Madera", "Roble", 120.0)
        comedor = Comedor("Comedor Test", mesa=mesa, sillas=[silla])
        resultado = tienda_vacia.agregar_comedor(comedor)
        assert "exitosamente" in resultado

    def test_agregar_comedor_none(self, tienda_vacia):
        resultado = tienda_vacia.agregar_comedor(None)
        assert "Error" in resultado

    # Pruebas de búsqueda
    def test_buscar_muebles_por_nombre(self, tienda_con_muebles):
        resultados = tienda_con_muebles.buscar_muebles_por_nombre("Mesa")
        assert len(resultados) == 1
        assert "Mesa" in resultados[0].nombre

    def test_buscar_muebles_por_nombre_vacio(self, tienda_con_muebles):
        resultados = tienda_con_muebles.buscar_muebles_por_nombre("")
        assert len(resultados) == 0

    def test_buscar_muebles_por_nombre_no_encontrado(self, tienda_con_muebles):
        resultados = tienda_con_muebles.buscar_muebles_por_nombre("Inexistente")
        assert len(resultados) == 0

    # Pruebas de filtrado por precio
    def test_filtrar_por_precio_rango_valido(self, tienda_con_muebles):
        resultados = tienda_con_muebles.filtrar_por_precio(500, 700)
        assert len(resultados) >= 1

    def test_filtrar_por_precio_min_invalido(self, tienda_con_muebles):
        resultados = tienda_con_muebles.filtrar_por_precio(-100, 1000)
        assert len(resultados) >= 0

    def test_filtrar_por_precio_sin_resultados(self, tienda_con_muebles):
        resultados = tienda_con_muebles.filtrar_por_precio(2000, 3000)
        assert len(resultados) == 0

    # Pruebas de filtrado por material
    def test_filtrar_por_material(self, tienda_con_muebles):
        resultados = tienda_con_muebles.filtrar_por_material("Madera")
        assert len(resultados) >= 1

    def test_filtrar_por_material_vacio(self, tienda_con_muebles):
        resultados = tienda_con_muebles.filtrar_por_material("")
        assert len(resultados) == 0

    def test_filtrar_por_material_no_encontrado(self, tienda_con_muebles):
        resultados = tienda_con_muebles.filtrar_por_material("Plástico")
        assert len(resultados) == 0

    # Pruebas de descuentos
    def test_aplicar_descuento_valido(self, tienda_vacia):
        resultado = tienda_vacia.aplicar_descuento("Sillas", 10)
        assert "Descuento del 10%" in resultado

    def test_aplicar_descuento_porcentaje_invalido(self, tienda_vacia):
        resultado = tienda_vacia.aplicar_descuento("Sillas", 0)
        assert "Error" in resultado

    def test_aplicar_descuento_porcentaje_alto(self, tienda_vacia):
        resultado = tienda_vacia.aplicar_descuento("Sillas", 150)
        assert "Error" in resultado

    def test_aplicar_descuento_plural(self, tienda_vacia):
        resultado = tienda_vacia.aplicar_descuento("Mesas", 15)
        assert "Descuento del 15%" in resultado
        assert "Mesa" in resultado

    # Pruebas de ventas
    def test_realizar_venta_exitosa(self, tienda_con_muebles):
        mueble = tienda_con_muebles.inventario[0]
        venta = tienda_con_muebles.realizar_venta(mueble, "Cliente Test")
        assert "error" not in venta
        assert venta["cliente"] == "Cliente Test"
        assert "precio_final" in venta

    def test_realizar_venta_mueble_no_disponible(self, tienda_vacia):
        mesa = Mesa("Mesa", "Madera", "Roble", 500.0,
                    forma="rectangular", capacidad_personas=6)
        venta = tienda_vacia.realizar_venta(mesa)
        assert "error" in venta

    def test_realizar_venta_con_descuento(self, tienda_con_muebles):
        tienda_con_muebles.aplicar_descuento("Mesa", 10)
        mueble = tienda_con_muebles.inventario[0]
        venta = tienda_con_muebles.realizar_venta(mueble)
        assert venta["descuento"] > 0

    def test_realizar_venta_sin_descuento(self, tienda_con_muebles):
        mueble = tienda_con_muebles.inventario[1]  # Una silla
        venta = tienda_con_muebles.realizar_venta(mueble)
        assert venta["descuento"] == 0

    # Pruebas de estadísticas
    def test_obtener_estadisticas_tienda_vacia(self, tienda_vacia):
        stats = tienda_vacia.obtener_estadisticas()
        assert stats["total_muebles"] == 0
        assert stats["valor_inventario"] == 0

    def test_obtener_estadisticas_con_muebles(self, tienda_con_muebles):
        stats = tienda_con_muebles.obtener_estadisticas()
        assert stats["total_muebles"] == 3
        assert stats["valor_inventario"] > 0
        assert "tipos_muebles" in stats

    def test_obtener_estadisticas_con_ventas(self, tienda_con_muebles):
        mueble = tienda_con_muebles.inventario[0]
        tienda_con_muebles.realizar_venta(mueble)
        stats = tienda_con_muebles.obtener_estadisticas()
        assert stats["total_muebles_vendidos"] == 1

    # Pruebas de reporte
    def test_generar_reporte_inventario_vacio(self, tienda_vacia):
        reporte = tienda_vacia.generar_reporte_inventario()
        assert "REPORTE DE INVENTARIO" in reporte
        assert "Mueblería OOP" in reporte
        assert "Total de muebles: 0" in reporte

    def test_generar_reporte_inventario_con_datos(self, tienda_con_muebles):
        reporte = tienda_con_muebles.generar_reporte_inventario()
        assert "Total de muebles: 3" in reporte
        assert "DISTRIBUCIÓN POR TIPOS:" in reporte

    def test_generar_reporte_con_descuentos(self, tienda_con_muebles):
        tienda_con_muebles.aplicar_descuento("Mesa", 10)
        reporte = tienda_con_muebles.generar_reporte_inventario()
        assert "DESCUENTOS ACTIVOS:" in reporte
        assert "10" in reporte

    def test_agregar_mueble_precio_invalido(self, tienda_vacia):
        mock_mueble = Mock()
        mock_mueble.nombre = "Mueble Gratis"
        mock_mueble.calcular_precio.return_value = 0

        resultado = tienda_vacia.agregar_mueble(mock_mueble)

        assert "Error" in resultado
        assert "precio válido" in resultado

    def test_agregar_mueble_error_calculo(self, tienda_vacia):
        mock_mueble = Mock()
        mock_mueble.nombre = "Mueble Fallido"
        mock_mueble.calcular_precio.side_effect = Exception("calculo fallido")

        resultado = tienda_vacia.agregar_mueble(mock_mueble)

        assert "Error al calcular precio" in resultado
        assert "calculo fallido" in resultado

    def test_filtrar_por_precio_salta_mueble_con_error(self, tienda_vacia):
        mock_mueble = Mock()
        mock_mueble.calcular_precio.side_effect = Exception("error de precio")
        mock_mueble.nombre = "Mueble Roto"
        tienda_vacia._inventario.append(mock_mueble)

        resultados = tienda_vacia.filtrar_por_precio(0, 1000)
        assert resultados == []

    def test_obtener_estadisticas_ignora_mueble_con_error(self, tienda_vacia):
        mock_mueble = Mock()
        mock_mueble.calcular_precio.side_effect = Exception("error estadisticas")
        mock_mueble.nombre = "Mueble Roto"
        tienda_vacia._inventario.append(mock_mueble)

        stats = tienda_vacia.obtener_estadisticas()
        assert stats["total_muebles"] == 1
        assert stats["valor_inventario"] == 0
        assert stats["tipos_muebles"] == {type(mock_mueble).__name__: 1}
