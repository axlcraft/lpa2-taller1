import pytest
from src.models.concretos.mesa import Mesa


class TestMesa:

    def test_instanciacion_correcta(self):
        mesa = Mesa("Mesa 1", "Madera", "Blanco", 200, "redonda", 150, 100, 75, 6)

        assert mesa.nombre == "Mesa 1"
        assert mesa.material == "Madera"
        assert mesa.color == "Blanco"
        assert mesa.precio_base == 200
        assert mesa.forma == "redonda"
        assert mesa.capacidad_personas == 6

    def test_setter_forma_valido(self):
        mesa = Mesa("Mesa 2", "Madera", "Negro", 200)

        mesa.forma = "ovalada"

        assert mesa.forma == "ovalada"

    def test_setter_forma_invalido(self):
        mesa = Mesa("Mesa 3", "Madera", "Negro", 200)

        with pytest.raises(ValueError):
            mesa.forma = "triangular"

    def test_setter_capacidad_valido(self):
        mesa = Mesa("Mesa 4", "Madera", "Negro", 200)

        mesa.capacidad_personas = 8

        assert mesa.capacidad_personas == 8

    def test_setter_capacidad_invalido(self):
        mesa = Mesa("Mesa 5", "Madera", "Negro", 200)

        with pytest.raises(ValueError):
            mesa.capacidad_personas = 0

    def test_calcular_precio_basico(self):
        mesa = Mesa("Mesa 6", "Madera", "Blanco", 200)

        precio = mesa.calcular_precio()

        # Solo factor tamaño (depende de Superficie, pero debe ser consistente)
        assert isinstance(precio, float)

    def test_calcular_precio_con_forma(self):
        mesa = Mesa("Mesa 7", "Madera", "Blanco", 200, "redonda")

        precio = mesa.calcular_precio()

        # Debe sumar 50 por no ser rectangular
        assert precio >= 250

    def test_calcular_precio_con_capacidad_media(self):
        mesa = Mesa("Mesa 8", "Madera", "Blanco", 200, "rectangular", 120, 80, 75, 5)

        precio = mesa.calcular_precio()

        # +50 por capacidad > 4
        assert precio >= 250

    def test_calcular_precio_con_capacidad_alta(self):
        mesa = Mesa("Mesa 9", "Madera", "Blanco", 200, "rectangular", 120, 80, 75, 8)

        precio = mesa.calcular_precio()

        # +100 por capacidad > 6
        assert precio >= 300

    def test_obtener_descripcion(self):
        mesa = Mesa("Mesa 10", "Madera", "Blanco", 200, "ovalada", 150, 100, 75, 6)

        desc = mesa.obtener_descripcion()

        assert "Mesa 10" in desc
        assert "Madera" in desc
        assert "Blanco" in desc
        assert "ovalada" in desc
        assert "Capacidad: 6" in desc