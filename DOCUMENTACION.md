# NUESTRO PROYECTO DE PROGRAMACION - GRUPO 14

## Quienes Somos

**Grupo:** 14

**Integrantes:**
- Ignacio Pita Carranza
- Ian Luka Szymkowickz
- Matias Rosental
- Lucas Garcia

## Objetivo del Proyecto

El objetivo del programa es crear un sistema de gestion para uso interno. El sistema permite iniciar sesion, administrar clientes, empleados, productos y promociones, y usar una calculadora corporal.

Los datos se guardan en archivos JSON para que no se pierdan cuando se cierra el programa.

## Estructura del Proyecto

El codigo oficial esta dentro de la carpeta `proyectoprogra1`.

```text
Proyecto Programacion UADE Grupo 14
├── README.md
├── DOCUMENTACION.md
├── .gitignore
├── version anterior
└── proyectoprogra1
    ├── main.py
    ├── login.py
    ├── clientes.py
    ├── empleados.py
    ├── productos.py
    ├── promociones.py
    ├── calculadora.py
    ├── colores.py
    ├── valids.py
    ├── persistencia.py
    └── data
        ├── usuarios.json
        ├── clientes.json
        ├── empleados.json
        ├── productos.json
        └── promociones.json
```

## Como Ejecutar el Programa

Desde la terminal:

```bash
python -m pip install -r requirements.txt
```

```bash
cd proyectoprogra1
python main.py
```

## Archivos Principales

### `main.py`

Es el archivo principal del sistema. Muestra el menu general y permite entrar a cada modulo.

Menu principal:

```text
1. Gestion de Clientes
2. Gestion de Empleados
3. Gestion de Productos
4. Gestion de Promociones
5. Calculadora corporal
0. Salir
```

### `login.py`

Maneja el inicio de sesion.

Los usuarios se cargan desde:

```text
proyectoprogra1/data/usuarios.json
```

Usuarios iniciales:

```text
admin   - admin123
ignacio - pita123
ian     - ian123
matias  - rosental123
lucas   - garcia123
```

Funciones:
- `login(usuario, password)`: revisa si el usuario y la contrasena son correctos.
- `iniciar_sesion()`: pide usuario y contrasena por consola.

### `persistencia.py`

Este archivo se encarga de leer y guardar datos en JSON.

Funciones:
- `obtener_ruta(nombre_archivo)`: arma la ruta del archivo dentro de `data`.
- `cargar_datos(nombre_archivo, datos_iniciales)`: lee un JSON. Si no existe, lo crea.
- `guardar_datos(nombre_archivo, datos)`: guarda los datos en un JSON.

Esta parte permite que clientes, empleados, productos, promociones y usuarios queden guardados.

### `valids.py`

Contiene funciones para validar datos ingresados por el usuario.

Funciones:
- `validar_dni(dni)`: verifica que el DNI tenga 8 numeros.
- `validar_telefono(telefono)`: verifica un formato de telefono valido.
- `validar_email(email)`: verifica que el email tenga un formato correcto.
- `formatear_nombre(nombre)`: convierte nombres a formato titulo.

### `colores.py`

Este archivo lo agregamos para que la consola sea mas facil de leer.

Antes todos los mensajes salian iguales y era medio incomodo distinguir si algo habia salido bien, si era un error o si era solo un aviso. Por eso usamos colores en algunos textos importantes.

Usamos la libreria `colorama`, que sirve para mostrar colores en la terminal. Igual dejamos el archivo preparado para que si `colorama` no esta instalada, el programa siga funcionando sin romperse.

Para instalarla se puede usar:

```bash
python -m pip install -r requirements.txt
```

Funciones:
- `titulo(texto)`: se usa para titulos de menus y secciones.
- `correcto(texto)`: se usa para mensajes de exito, por ejemplo cuando algo se guarda.
- `error(texto)`: se usa cuando hay datos invalidos o una opcion incorrecta.
- `aviso(texto)`: se usa para advertencias o mensajes informativos.

Ejemplo:

```python
print(correcto("Cliente registrado"))
print(error("Opcion invalida"))
print(aviso("No hay productos activos"))
print(titulo("GESTION DE CLIENTES"))
```

No le pusimos color a todo porque si no se vuelve confuso. La idea fue usarlo solo donde ayuda a entender mejor lo que esta pasando.

## Gestion de Clientes

Archivo:

```text
proyectoprogra1/clientes.py
```

JSON usado:

```text
proyectoprogra1/data/clientes.json
```

Estructura de un cliente:

```python
cliente = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Perez",
    "dni": "12345678",
    "email": "juan@email.com",
    "telefono": "11 1234 5678",
    "activo": True
}
```

Funciones principales:
- `crear_cliente()`: registra un cliente nuevo.
- `buscar_cliente_id(id_cliente)`: busca un cliente por ID.
- `listar_clientes()`: muestra clientes activos.
- `modificar_cliente()`: permite modificar nombre, apellido, email o telefono.
- `baja_cliente()`: marca un cliente como inactivo.
- `buscar_clientes()`: busca por nombre, apellido o DNI.

## Gestion de Empleados

Archivo:

```text
proyectoprogra1/empleados.py
```

JSON usado:

```text
proyectoprogra1/data/empleados.json
```

Estructura de un empleado:

```python
empleado = {
    "id": 1,
    "nombre": "Maria",
    "apellido": "Garcia",
    "dni": "87654321",
    "email": "maria@empresa.com",
    "telefono": "11 9876 5432",
    "cargo": "Gerente",
    "activo": True
}
```

Funciones principales:
- `crear_empleado()`: registra un empleado nuevo.
- `buscar_empleado_id(id_empleado)`: busca un empleado por ID.
- `listar_empleados()`: muestra empleados activos.
- `modificar_empleado()`: permite modificar datos del empleado.
- `baja_empleado()`: marca un empleado como inactivo.
- `buscar_empleados()`: busca por nombre, apellido o DNI.

## Gestion de Productos

Archivo:

```text
proyectoprogra1/productos.py
```

JSON usado:

```text
proyectoprogra1/data/productos.json
```

Estructura de un producto:

```python
producto = {
    "id": 1,
    "nombre": "Proteina",
    "precio": 10000.0,
    "stock": 15,
    "activo": True
}
```

Funciones principales:
- `crear_producto()`: registra un producto nuevo.
- `buscar_producto_id(id_producto)`: busca un producto por ID.
- `listar_productos()`: muestra productos activos.
- `modificar_producto()`: permite modificar nombre, precio o stock.
- `baja_producto()`: marca un producto como inactivo.
- `buscar_productos()`: busca productos por nombre.

## Gestion de Promociones

Archivo:

```text
proyectoprogra1/promociones.py
```

JSON usado:

```text
proyectoprogra1/data/promociones.json
```

Estructura de una promocion:

```python
promocion = {
    "id": 1,
    "nombre": "Promo Verano",
    "descuento": 20.0,
    "activa": True
}
```

Funciones principales:
- `crear_promocion()`: registra una promocion nueva.
- `buscar_promocion_id(id_promocion)`: busca una promocion por ID.
- `listar_promociones()`: muestra promociones activas.
- `modificar_promocion()`: permite modificar nombre y descuento.
- `baja_promocion()`: marca una promocion como inactiva.
- `buscar_promociones()`: busca promociones por nombre.

## Calculadora Corporal

Archivo:

```text
proyectoprogra1/calculadora.py
```

La calculadora pide peso, altura y objetivo. Luego muestra:
- IMC.
- Categoria del IMC.
- Recomendacion diaria de proteinas.

Funciones principales:
- `obtener_float(mensaje, minimo, maximo)`: pide un numero decimal con rango valido.
- `obtener_int(mensaje, opciones_validas)`: pide una opcion numerica.
- `calcular_imc(peso, altura)`: calcula el indice de masa corporal.
- `clasificar_imc(imc)`: devuelve la categoria del IMC.
- `calcular_proteinas(peso, objetivo)`: calcula los gramos recomendados.
- `calculadora_corporal()`: ejecuta toda la calculadora.

## Guardado de Datos

El sistema usa archivos JSON dentro de:

```text
proyectoprogra1/data
```

Cada modulo carga sus datos al iniciar:
- `clientes.py` carga `clientes.json`.
- `empleados.py` carga `empleados.json`.
- `productos.py` carga `productos.json`.
- `promociones.py` carga `promociones.json`.
- `login.py` carga `usuarios.json`.

Cuando se crea, modifica o da de baja un registro, el archivo JSON correspondiente se actualiza.

## Estado de los Registros

El sistema no elimina clientes, empleados, productos ni promociones de forma definitiva.

En lugar de borrar registros:
- Clientes, empleados y productos usan `"activo": True` o `"activo": False`.
- Promociones usan `"activa": True` o `"activa": False`.

Esto permite conservar el historial dentro del archivo JSON.

## Backup

La carpeta `version anterior` contiene una copia del proyecto antes de reorganizar la estructura.

Esa carpeta sirve como respaldo. El codigo oficial actual esta en `proyectoprogra1`.

## Funcionalidades Implementadas

- Login de administrador.
- Gestion de clientes.
- Gestion de empleados.
- Gestion de productos.
- Gestion de promociones.
- Calculadora corporal.
- Persistencia de datos con JSON.
- Colores en los mensajes principales de la consola.
- Menus por consola.
- Validaciones basicas de datos.

## Funcionalidades Pendientes o Posibles Mejoras

- Historial de pagos.
- Venta de productos a clientes.
- Asociar promociones automaticamente segun condiciones.
- Reportes o estadisticas.
- Mejorar seguridad de contrasenas.
- Validar que no se repitan DNI o emails.

