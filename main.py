from beneficio import Beneficio


def main():
    c1 = Beneficio('Pepito', 'Pérez', '30701040', 30, 30000)

    print('\n- Mostrar datos cuenta 1 ----------------------')
    print(f'Nombre: {c1.get_nombre()}')
    print(f'Apellido: {c1.get_apellido()}')
    print(f'Cedula: {c1.get_cedula()}')
    print(f'Edad: {c1.get_edad()}')
    print(f'Dinero ahorrado: {c1.get_dinero_ahorrado()}')
    print(f'Es usuario beneficiario? {"sip" if c1.es_usuario_valido() else "pues no"}')

    print('\n- Modificar datos cuenta 1 --------------------')
    c1.set_nombre('Pedro')
    c1.set_apellido('Pereira')
    c1.set_cedula('10905040')
    c1.set_edad(40)
    c1.set_dinero_ahorrado(40000)

    c1.mostrar()

    print('\n- Ingresar y Retirar en Cuenta 2 --------------')
    cuenta_cliente_joven = Beneficio('María', 'Magdalena', '1080305003', 20, 20000)

    test_function(cuenta_cliente_joven.ingresar, -1000)
    test_function(cuenta_cliente_joven.ingresar, 0)
    test_function(cuenta_cliente_joven.ingresar, 1000)

    test_function(cuenta_cliente_joven.retirar, -1000)
    test_function(cuenta_cliente_joven.retirar, 0)
    test_function(cuenta_cliente_joven.retirar, 100000)
    test_function(cuenta_cliente_joven.retirar, 1000)
    cuenta_cliente_joven.mostrar()


def test_function(function, value):
    try:
        return function(value)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
