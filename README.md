# Proyecto Programacion UADE Grupo 14

Sistema de gestion por consola hecho para Programacion 1.

El codigo oficial esta dentro de la carpeta `proyectoprogra1`.

## Integrantes

- Ignacio Pita Carranza
- Ian Luka Szymkowickz
- Matias Rosental
- Lucas Garcia

## Como Ejecutar

```bash
cd proyectoprogra1
python main.py
```

## Funcionalidades

- Login de administrador.
- Gestion de clientes.
- Gestion de empleados.
- Gestion de productos.
- Gestion de promociones.
- Calculadora corporal.
- Guardado de datos en archivos JSON.

## Estructura

```text
proyectoprogra1/
├── main.py
├── login.py
├── clientes.py
├── empleados.py
├── productos.py
├── promociones.py
├── calculadora.py
├── valids.py
├── persistencia.py
└── data/
    ├── usuarios.json
    ├── clientes.json
    ├── empleados.json
    ├── productos.json
    └── promociones.json
```

## Usuarios Iniciales

```text
admin   - admin123
ignacio - pita123
ian     - ian123
matias  - rosental123
lucas   - garcia123
```

## Guardado de Datos

Los datos se guardan en archivos JSON dentro de `proyectoprogra1/data`.

Esto permite que clientes, empleados, productos, promociones y usuarios sigan disponibles despues de cerrar el programa.

## Backup

La carpeta `version anterior` guarda una copia del proyecto antes de la reorganizacion.
