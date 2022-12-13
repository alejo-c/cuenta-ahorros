from usuario import Usuario  # Módulo de usuario


class Cuenta(Usuario):

    _dinero_ahorrado: float

    def __init__(self, nombre, apellido, cedula, edad, dinero) -> None:
        super().__init__(nombre, apellido, cedula, edad)
        self._dinero_ahorrado = dinero

    def get_dinero_ahorrado(self) -> float:
        return self._dinero_ahorrado

    def set_dinero_ahorrado(self, dinero: float) -> None:
        self._dinero_ahorrado = dinero

    def mostrar(self) -> None:
        reporte = [
            '',
            '- Resumen de Cliente -',
            f'Nombre:   {self._nombre}',
            f'Apellido: {self._apellido}',
            f'Cedula:   {self._cedula}',
            f'Edad:     {self._edad}',
            f'Dinero:   {self._dinero_ahorrado}',
        ]
        print('\n'.join([i for i in reporte]))

    # Simular Ingreso
    def ingresar(self, ingreso: float) -> None:
        if ingreso <= 0:
            c = '-' if ingreso < 0 else ''
            raise ValueError(f'[Ingresar]: Error: No es válido ingresar {c}${-ingreso}')
        
        print(f'[Ingresar]: Dinero actual = ${self._dinero_ahorrado + ingreso}')

    # Simular Retiro
    def retirar(self, retiro: float) -> None:
        if retiro <= 0:
            c = '-' if retiro < 0 else ''
            raise ValueError(f'[Retirar]: Error: No es válido retirar {c}${-retiro}')

        if retiro > self._dinero_ahorrado:
            raise ValueError(f'[Retirar]: No hay suficiente para retirar ${retiro}')

        print(f'[Retirar]: Dinero actual = ${self._dinero_ahorrado - retiro}')