# NUESTRO PROYECTO DE PROGRAMACIÓN - GRUPO 14

## Quiénes Somos

**Grupo:** 14 (somos 4 estudiantes de primer año)

**Los integrantes:**
- Ignacio Pita Carranza
- Ian Luka Szymkowickz  
- Matías Rosental
- Lucas García

## Qué Quisimos Hacer

Básicamente queríamos hacer un programa que sirva para manejar clientes y empleados de una empresa. Es como una agenda digital pero más completa. La idea es que un administrador pueda cargar datos, buscar personas, modificar información y esas cosas que necesita cualquier negocio.

---

## Cómo Organizamos el Código

Dividimos todo en varios archivos para no hacer un desastre:

```
Nuestro Proyecto
├── main.py          # El archivo principal que ejecutás
├── login.py         # Para que no entre cualquiera al sistema
├── clientes.py      # Todo lo relacionado con clientes
├── empleados.py     # Todo lo relacionado con empleados
├── valids.py        # Para verificar que los datos estén bien
├── README.md        # Info básica del proyecto
└── DOCUMENTACION.md # Este archivo que estás leyendo
```

---

## El Login (login.py)

### Para Qué Sirve
Es para que no cualquiera pueda usar nuestro programa. Funciona como cuando te logueas en Instagram o cualquier app.

### Usuarios y Contraseñas que Funcionan
```
Usuario       | Contraseña
------------- | -----------
admin         | admin123
ignacio       | pita123
ian           | ian123
matias        | rosental123
lucas         | garcia123
```

### Las Funciones Que Hicimos

#### `login(usuario, password)`
Esta función básicamente chequea si el usuario y la contraseña que pusiste existen en nuestra "base de datos" (que en realidad es solo un diccionario). Si están bien, te deja entrar. Si no, te dice que está mal.

#### `iniciar_sesion()`
Esta es la función principal del login. Te pide usuario y contraseña, y si te equivocás te deja intentar otra vez. Si ponés "-1" como usuario, el programa se cierra. Es bastante simple pero funciona.

---

## Las Validaciones (valids.py)

### Para Qué Sirven
Estas funciones verifican que los datos que ingresa el usuario estén bien. Porque si alguien pone "asdasd" como DNI, obviamente está mal.

#### `validar_dni(dni)`
Chequea que el DNI tenga exactamente 8 números. Nada más, nada menos. Si ponés letras o menos números, te dice que está mal.
- **Ejemplo que funciona:** "12345678"
- **Ejemplo que NO funciona:** "1234567A" o "123"

#### `validar_telefono(telefono)`
Verifica que el teléfono tenga formato argentino. Puede tener guiones, espacios o estar todo junto.
- **Ejemplos que funcionan:** 
  - "011-1234-5678"
  - "011 1234 5678" 
  - "01112345678"

#### `validar_email(email)`
Se fija que el email tenga arroba (@) y punto, básicamente que parezca un email real.
- **Ejemplo que funciona:** "usuario@dominio.com"

#### `formatear_nombre(nombre)`
Esta función toma cualquier nombre y lo pone con la primera letra en mayúscula. Es para que todo quede prolijo.
- **Ejemplo:** si escribís "JUAN PÉREZ" te lo convierte en "Juan Pérez"

---

## Gestión de Clientes (clientes.py)

### Estructura de Datos
Los clientes se almacenan en una lista de diccionarios con la siguiente estructura:
```python
cliente = {
    "id": 1,                    # ID autogenerado
    "nombre": "Juan",           # Nombre formateado
    "apellido": "Pérez",        # Apellido formateado
    "dni": "12345678",          # DNI validado
    "email": "juan@email.com",  # Email validado en minúsculas
    "telefono": "11 1234 5678", # Teléfono validado
    "activo": True              # Estado del cliente
}
```

### Funciones Principales

#### `crear_cliente()`
- **Propósito:** Registrar nuevos clientes
- **Proceso:**
  1. Asigna ID automático (length + 1)
  2. Solicita y valida cada campo
  3. Formatea nombres y apellidos
  4. Valida DNI, email y teléfono
  5. Marca como activo por defecto
  6. Confirma registro

#### `buscar_cliente_id(id_cliente)`
- **Propósito:** Buscar cliente por ID específico
- **Parámetros:** `id_cliente` (int)
- **Retorna:** Diccionario del cliente o `False` si no existe

#### `listar_clientes()`
- **Propósito:** Mostrar todos los clientes activos
- **Implementación:** Usa `filter()` con lambda para obtener solo activos
- **Formato:** Muestra ID, nombre completo, DNI y teléfono

#### `modificar_cliente()`
- **Propósito:** Actualizar datos de cliente existente
- **Características:**
  - Permite reactivar clientes inactivos
  - Menú interactivo para seleccionar campo a modificar
  - Valida nuevos datos antes de guardar
  - Permite cancelar sin cambios

#### `baja_cliente()`
- **Propósito:** Dar de baja cliente (soft delete)
- **Funcionamiento:** Marca `activo = False` sin eliminar el registro

#### `buscar_clientes()`
- **Propósito:** Buscar clientes por término parcial
- **Campos de búsqueda:** Nombre, apellido o DNI
- **Características:**
  - Búsqueda insensible a mayúsculas/minúsculas
  - Muestra múltiples resultados
  - Indica estado (activo/inactivo)

---

## Gestión de Empleados (empleados.py)

### Estructura de Datos
Similar a clientes pero incluye campo adicional:
```python
empleado = {
    "id": 1,                      # ID autogenerado
    "nombre": "María",            # Nombre formateado
    "apellido": "García",         # Apellido formateado
    "dni": "87654321",            # DNI validado y único
    "email": "maria@empresa.com", # Email validado
    "telefono": "11 9876 5432",   # Teléfono validado
    "cargo": "Gerente",           # Cargo del empleado
    "activo": True                # Estado del empleado
}
```

### Funciones Principales

#### `crear_empleado()`
- **Diferencias con clientes:**
  - Validación de DNI único entre empleados
  - Campo cargo obligatorio
  - Validaciones adicionales de campos no vacíos

#### `buscar_empleado_id(id_empleado)`
- **Igual funcionamiento que en clientes**

#### `listar_empleados()`
- **Formato:** ID, nombre completo, cargo y teléfono

#### `modificar_empleado()`
- **Incluye opción adicional:** Modificar cargo
- **Misma lógica de reactivación que clientes**

#### `baja_empleado()`
- **Igual funcionamiento que baja de clientes**

#### `buscar_empleados()`
- **Igual lógica que búsqueda de clientes**
- **Muestra cargo en los resultados**

---

## Sistema Principal (main.py)

### Flujo del Sistema

#### Inicialización
```python
if iniciar_sesion():    # Si el login es exitoso
    menu_principal()    # Muestra el menú principal
```

### Estructura de Menús

#### `menu_principal()`
```
SISTEMA DE GESTION - GRUPO 14
=============================
1. Gestion de Clientes
2. Gestion de Empleados  
0. Salir
```

#### `menu_clientes()`
```
GESTION DE CLIENTES
===================
1. Alta de cliente
2. Listar clientes activos
3. Buscar cliente
4. Modificar cliente
5. Baja de cliente
0. Volver al menu principal
```

#### `menu_empleados()`
```
GESTION DE EMPLEADOS
====================
1. Alta de empleado
2. Listar empleados activos
3. Buscar empleado
4. Modificar empleado
5. Baja de empleado
0. Volver al menu principal
```

### Características de la Navegación
- **Bucles persistentes:** Los menús permanecen activos hasta que el usuario seleccione "0"
- **Validación de opciones:** Muestra "Opción inválida" para entradas incorrectas
- **Navegación jerárquica:** Regreso automático al menú superior
- **Importaciones modulares:** Cada funcionalidad se importa de su módulo correspondiente

---

### Flujo de Uso
1. **Inicio:** Ejecutar `main.py`
2. **Autenticación:** Ingresar credenciales válidas
3. **Navegación:** Usar menús para acceder a funcionalidades
4. **Operaciones:** Realizar altas, bajas, modificaciones y búsquedas
5. **Salida:** Seleccionar opción "0" para salir

---

## Consideraciones Técnicas

### Almacenamiento
- **Tipo:** Listas en memoria (no persistente)
- **Vida útil:** Los datos se pierden al cerrar el programa
- **Escalabilidad:** Limitada por memoria RAM

### Validaciones
- **DNI:** Formato argentino estándar (8 dígitos)
- **Teléfono:** Formato flexible con separadores opcionales
- **Email:** Formato estándar internacional
- **Nombres:** Formateo automático a Title Case

### Gestión de Estados
- **Soft Delete:** Los registros no se eliminan físicamente
- **Reactivación:** Posibilidad de restaurar registros inactivos
- **Integridad:** IDs únicos y autogenerados

### Limitaciones Actuales
- **Persistencia:** No hay guardado en base de datos o archivos
- **Concurrencia:** No soporta múltiples usuarios simultáneos
- **Backup:** No hay sistema de respaldo automático
- **Logs:** No hay registro de actividades del sistema

---

## Funcionalidades Implementadas para Entrega (40%)

### Completadas
- [x] **Login del administrador** - Sistema de autenticación funcional
- [x] **Gestión de clientes** - Alta, baja y modificación completas  
- [x] **Gestión de empleados** - Alta, baja y modificación completas
- [x] **Interfaz funcional** - Menús navegables y operativos

### Funcionalidades Planificadas (Futuras)
- [ ] Gestión de Promociones
- [ ] Gestión de Productos  
- [ ] Calculadora de Masa Corporal
- [ ] Historial de Pagos
- [ ] Persistencia de datos
- [ ] Reportes y estadísticas

---

## Información de Contacto

Para dudas o consultas sobre el sistema, contactar a cualquier integrante del **Grupo 14**:
- Ignacio Pita Carranza
- Ian Luka Szymkowickz  
- Matías Rosental
- Lucas García

---

*Documentación actualizada al 20 de abril de 2026*  
*Sistema de Gestión - UADE Grupo 14*