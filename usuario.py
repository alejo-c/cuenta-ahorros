class Usuario:

    _nombre: str
    _apellido: str
    _cedula: str
    _edad: int

    def __init__(self, nombre, apellido, cedula, edad) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._edad = edad

    def get_nombre(self) -> str:
        return self._nombre

    def get_apellido(self) -> str:
        return self._apellido

    def get_cedula(self) -> str:
        return self._cedula

    def get_edad(self) -> int:
        return self._edad

    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def set_apellido(self, apellido: str) -> None:
        self._apellido = apellido

    def set_cedula(self, cedula: str) -> None:
        self._cedula = cedula

    def set_edad(self, edad: int) -> None:
        if edad <= 0:
            raise ValueError('[Set Edad]: Error: el valor de la edad no es válido')
        self._edad = edad
