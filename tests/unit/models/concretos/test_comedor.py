import pytest
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


class TestComedor:

    @pytest.fixture
    def comedor_basico(self):
        mesa = Mesa("Mesa Familiar", "Madera", "Roble", 500.0,
                    forma="rectangular", capacidad_personas=6)
        sillas = [
            Silla(f"Silla {i}", "Madera", "Roble", 120.0, tiene_respaldo=True)
            for i in range(1, 5)
        ]
        return Comedor("Comedor Familiar", mesa=mesa, sillas=sillas)

    def test_composicion_correcta(self, comedor_basico):
        assert comedor_basico.mesa is not None
        assert len(comedor_basico.sillas) == 4

    def test_calcular_precio_total(self, comedor_basico):
        # El método correcto es calcular_precio_total, no calcular_precio
        precio_total = comedor_basico.calcular_precio_total()
        assert isinstance(precio_total, float)
        assert precio_total > 0