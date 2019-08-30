# keymap_sublime


# software
- Sublime text 3 version 3.2.1 build 3207

# SO
- windows 7 profesional service pack 1

# Instalacion 

Dentro de `git bash` ir la siguiente ruta

```php
~/AppData/Roaming/'Sublime Text 3'/Packages/user
```
Clonar el repositorio en esta ruta

```php
git clone https://github.com/hhklik/keymap_sublime.git
```

## Modificar el archivo sublime-keymap --user

Dentro de `sublieme text` en la barra de herramientas buscar `Preferences`y luego dar click en `Key bindings` y dentro de los corchetes `[    ]` pegar el siguiente codigo.

```php
{ "keys": ["ctrl+7"], "command": "insert_snippet", "args": {"name": "Packages/User/comentario.sublime-snippet"}},
{ "keys": ["ctrl+8"], "command": "insert_snippet", "args": {"name": "Packages/User/comentarioMod.sublime-snippet"}},
{ "keys": ["ctrl+9"], "command": "insert_snippet", "args": {"name": "Packages/User/secundariasComent.sublime-snippet"}},
{ "keys": ["ctrl+0"], "command": "insert_snippet", "args": {"name": "Packages/User/ComentCodigo.sublime-snippet"}},
{ "keys": ["ctrl+6"], "command": "add_date_time_stamp"},
{ "keys": ["ctrl+5"], "command": "insert_snippet", "args": {"name": "Packages/User/fin.sublime-snippet"}},
{ "keys": ["ctrl+4"], "command": "insert_snippet", "args": {"name": "Packages/User/trans.sublime-snippet"}},
{ "keys": ["ctrl+3"], "command": "insert_snippet", "args": {"name": "Packages/User/tranlatePhp.sublime-snippet"}},
{ "keys": ["ctrl+2"], "command": "insert_snippet", "args": {"name": "Packages/User/TranslateDuplex.sublime-snippet"}},
{ "keys": ["ctrl+1"], "command": "insert_snippet", "args": {"name": "Packages/User/translatecode.sublime-snippet"}},
{"keys": ["alt+f10"], "command": "add_random_string_only_letters"},
{ "keys": ["ctrl+shift+7"], "command": "toggle_comment", "args": { "block": true } }
```

# Comandos python utiles

- `add_date_time_stamp`               ==> d/m/Y H:M:S
- `add_date_time_stamp`               ==> d/m/Y
- `add_time_stamp`                    ==> H:M:S        
- `add_random_string_all`             ==> cadena aleatoria; uppercase, lowercase , digits
- `add_random_string_only_letters`    ==> Cadena aleatoria solo letras; uppercase, lowercase
- `add_random_string_lowercase`       ==> Cadena aleatoria; lowercase
- `add_random_string_uppercase`       ==> Cadena aleatoria; uppercase

# Como utilizar un comando python en sublime-keymap

puede ingresar el siguiente codigo agregando la comibinacion de teclas para esta accion
```php
{ "keys": ["<Ctrl | Alt> + <shift | tacla> + <tecla> "], "command": "add_date_time_stamp"}
```
tecla :: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12
Precaucion no utilizar combianaciones necesarias para la operacion como por ejemplo `ctrl + v` o `ctrl + c` son para copia y pegar textos

# Cambiar el nombre del developer
ingresar la siguiente ruta en una carperta

```php
%APPDATA%\Sublime Text 3\Packages\User
```
modificar el archivo `comentario.sublime-snippet`

```php
<snippet>
	<content><![CDATA[
/*===================================================
=		       Bloque de comentarios             	=
=       <Nombre del developer> $1       			=
FUNCIÓN:
PARAMETROS:
POST:
GET:
DEVUELVE:
NOTA:
================= MODIFICACIONES ===================
====================================================
==================================================*/

/*========== Fin Bloque de comentarios ===========*/
]]></content>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	<tabTrigger>comentario</tabTrigger>
	<!-- Optional: Set a scope to limit where the snippet will trigger -->
	<!-- <scope>source.python</scope> -->
</snippet>
```

# Funcionalidades

## Como agregar un comentario para funciones

`ctrl + 7` inserta el comentario acto seguido `ctrl + 6` inserta la fecha actual

y aparecera el siguiente comentario
donde se puede ingresar la informacion de la funcion
```php
/*===================================================
=		       Bloque de comentarios             	=
=       HUMBERTO HERRADOR 29/08/2019       			=
FUNCIÓN:
PARAMETROS:
POST:
GET:
DEVUELVE:
NOTA:
================= MODIFICACIONES ===================
====================================================
==================================================*/

/*========== Fin Bloque de comentarios ===========*/
```

## Agregar una cadena aleatoria de caracteres ONLY LETTERS

`alt + F10` insertara una cadena aleatoria

por ejemplo : erpAUxElvH



# Autores ✒️

* **Humberto Herrador** - *Trabajo Inicial* - [hhklik](https://github.com/hhklik) [ada soft gt](http://adasoft.com.gt)









