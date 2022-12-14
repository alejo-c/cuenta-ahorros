from cuenta import Cuenta


class Beneficio(Cuenta):

    interes_beneficio: float = 0.05

    def __init__(self, nombre, apellido, cedula, edad, dinero) -> None:
        super().__init__(nombre, apellido, cedula, edad, dinero)

    def es_usuario_valido(self) -> bool:
        return 18 <= self._edad < 28

    def mostrar(self):
        dinero_auxiliar = self._dinero_ahorrado
        if self.es_usuario_valido():
            self._dinero_ahorrado *= 1 + self.interes_beneficio
        super().mostrar()
        self._dinero_ahorrado = dinero_auxiliar