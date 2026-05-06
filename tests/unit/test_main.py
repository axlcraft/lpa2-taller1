import pytest
from unittest.mock import patch, MagicMock
from src.services.tienda import TiendaMuebles


class TestMainFunciones:
    """
    Cubre las funciones de main.py que no están cubiertas:
    - mostrar_estadisticas_iniciales (línea 329)
    - main() completa (líneas 343-374): flujo normal, KeyboardInterrupt, Exception
    """

    @pytest.fixture
    def tienda_con_datos(self):
        from src.main import crear_catalogo_inicial, crear_comedores_ejemplo, aplicar_descuentos_ejemplo
        tienda = TiendaMuebles("Test")
        crear_catalogo_inicial(tienda)
        crear_comedores_ejemplo(tienda)
        aplicar_descuentos_ejemplo(tienda)
        return tienda

    # ------------------------------------------------------------------ mostrar_estadisticas_iniciales (línea 329)

    def test_mostrar_estadisticas_iniciales(self, tienda_con_datos, capsys):
        from src.main import mostrar_estadisticas_iniciales
        mostrar_estadisticas_iniciales(tienda_con_datos)
        captured = capsys.readouterr()
        assert "Total de muebles" in captured.out or "Estadísticas" in captured.out

    def test_mostrar_estadisticas_tienda_vacia(self, capsys):
        from src.main import mostrar_estadisticas_iniciales
        tienda = TiendaMuebles("Vacía")
        mostrar_estadisticas_iniciales(tienda)
        captured = capsys.readouterr()
        assert "0" in captured.out

    # ------------------------------------------------------------------ main() flujo normal (343-374)

    def test_main_flujo_normal(self, capsys):
        """
        Cubre el bloque try de main(): inicializa tienda, crea catálogo,
        comedores, descuentos y estadísticas. Se mockea input() y menu.ejecutar()
        para que no espere entrada del usuario ni lance el bucle.
        """
        from src.main import main
        with patch("builtins.input", return_value=""), \
             patch("src.main.MenuTienda") as MockMenu:
            mock_menu_instance = MagicMock()
            MockMenu.return_value = mock_menu_instance
            main()
        captured = capsys.readouterr()
        assert "Bienvenido" in captured.out or "Mueblería" in captured.out
        mock_menu_instance.ejecutar.assert_called_once()

    def test_main_keyboard_interrupt(self, capsys):
        """Cubre el bloque except KeyboardInterrupt de main()."""
        from src.main import main
        with patch("builtins.input", side_effect=KeyboardInterrupt()):
            main()
        captured = capsys.readouterr()
        assert "interrumpido" in captured.out or "👋" in captured.out

    def test_main_excepcion_generica(self, capsys):
        """Cubre el bloque except Exception de main()."""
        from src.main import main
        with patch("src.main.TiendaMuebles", side_effect=Exception("error de prueba")):
            main()
        captured = capsys.readouterr()
        assert "Error" in captured.out or "error" in captured.out.lower()