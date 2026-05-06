import pytest
from src.services.catalogo import Catalogo
from src.models.concretos.silla import Silla
from src.models.concretos.mesa import Mesa


class TestCatalogoCompleto:
    """Tests adicionales para cubrir líneas faltantes de catalogo.py."""

    @pytest.fixture
    def catalogo_vacio(self):
        return Catalogo()

    @pytest.fixture
    def catalogo_con_muebles(self):
        silla = Silla("Silla Roja", "madera", "rojo", 100.0)
        mesa = Mesa("Mesa Cristal", "vidrio", "transparente", 200.0)
        return Catalogo([silla, mesa])

    # agregar (línea 20)
    def test_agregar_mueble(self, catalogo_vacio):
        silla = Silla("Nueva", "metal", "gris", 50.0)
        catalogo_vacio.agregar(silla)
        assert len(catalogo_vacio.obtener_todos()) == 1

    # obtener_todos (línea 25)
    def test_obtener_todos(self, catalogo_con_muebles):
        assert len(catalogo_con_muebles.obtener_todos()) == 2

    def test_obtener_todos_vacio(self, catalogo_vacio):
        assert catalogo_vacio.obtener_todos() == []

    # buscar_por_nombre vacío (línea 36)
    def test_buscar_nombre_vacio(self, catalogo_con_muebles):
        assert catalogo_con_muebles.buscar_por_nombre("") == []

    def test_buscar_nombre_none(self, catalogo_con_muebles):
        assert catalogo_con_muebles.buscar_por_nombre(None) == []

    # filtrar_por_material vacío (líneas 52-54)
    def test_filtrar_material_vacio(self, catalogo_con_muebles):
        assert catalogo_con_muebles.filtrar_por_material("") == []

    def test_filtrar_material_none(self, catalogo_con_muebles):
        assert catalogo_con_muebles.filtrar_por_material(None) == []

    # filtrar_por_precio con valores inválidos (líneas 64-66)
    def test_filtrar_precio_min_invalido(self, catalogo_con_muebles):
        assert catalogo_con_muebles.filtrar_por_precio("no_numero", 500) == []

    def test_filtrar_precio_max_invalido(self, catalogo_con_muebles):
        assert catalogo_con_muebles.filtrar_por_precio(0, "no_numero") == []

    def test_filtrar_precio_none(self, catalogo_con_muebles):
        assert catalogo_con_muebles.filtrar_por_precio(None, None) == []

    def test_filtrar_precio_rango_valido(self, catalogo_con_muebles):
        resultado = catalogo_con_muebles.filtrar_por_precio(50, 500)
        assert len(resultado) >= 1