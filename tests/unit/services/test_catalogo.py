import pytest
from src.services.catalogo import Catalogo
from src.models.concretos.silla import Silla
from src.models.concretos.mesa import Mesa


class TestCatalogo:

    @pytest.fixture
    def catalogo(self):
        # Silla precio_base=100 → calcular_precio() ≈ 110 (factor comodidad)
        # Mesa precio_base=200 → calcular_precio() depende de forma/capacidad
        # Usamos rango amplio para capturar ambos
        silla = Silla("Silla Básica", "Madera", "Café", 100.0)
        mesa = Mesa("Mesa Comedor", "Madera", "Roble", 200.0,
                    forma="rectangular", capacidad_personas=4)
        return Catalogo([silla, mesa])

    def test_buscar_por_nombre(self, catalogo):
        resultado = catalogo.buscar_por_nombre("Silla")
        assert len(resultado) == 1
        assert resultado[0].nombre == "Silla Básica"

    def test_filtrar_por_precio(self, catalogo):
        # Rango amplio para capturar ambos muebles con sus precios calculados
        resultado = catalogo.filtrar_por_precio(50, 500)
        assert len(resultado) == 2

    def test_filtrar_por_material(self, catalogo):
        resultado = catalogo.filtrar_por_material("Madera")
        assert len(resultado) == 2

    def test_obtener_todos(self, catalogo):
        resultado = catalogo.obtener_todos()
        assert len(resultado) == 2