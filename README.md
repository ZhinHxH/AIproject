<h1 align="center">
  <br>
  <img src="[https://yourlinkscribeimageurl.com/logo.png](https://play-lh.googleusercontent.com/sLENPy71gZS2u-8deRY1LaAaEWidPF570HfsGF9XGAm4kqTUjLCdDyeQdDVTQSVV9KYO=w240-h480-rw)" alt="LinkScribe" width="200">
  <br>
  LinkScribe
  <br>
</h1>

<h4 align="center">Organizador de enlaces inteligente</h4>

<p align="center">
  <a href="#funcionalidades">Funcionalidades</a> •
  <a href="#requisitos-de-instalación">Requisitos de instalación</a> •
  <a href="#instalación">Instalación</a> •
  <a href="#contribución">Contribución</a> •
  <a href="#licencia">Licencia</a>
</p>

<p align="center">
  <img src="https://yourlinkscribeimageurl.com/demo.gif" alt="Demo">
</p>

## Descripción

LinkScribe es una aplicación web/mobile/desktop que utiliza procesamiento de lenguaje natural (NLP) para permitir a los usuarios crear y organizar listas de enlaces de forma fácil y eficiente. Con LinkScribe, los usuarios pueden simplemente copiar y pegar un enlace web, y la aplicación lo procesará automáticamente, extrayendo información sobre el contenido de la página y clasificándolos de acuerdo a la información obtenida.

## Funcionalidades

- **Creación y organización de listas de enlaces:** Los usuarios pueden crear listas de enlaces en dependencia de las categorias del data set usado.
- **Procesamiento de lenguaje natural (NLP):** Utiliza NLP para extraer información sobre el contenido de las páginas vinculadas y clasificar automáticamente los enlaces.
- **Interfaz intuitiva:** Diseño de interfaz de usuario atractivo y fácil de usar.

## Requisitos de instalación

- Poetry
- Python
- Pip
- Vite
- NPM (Node Package Manager)
- MySQL

## Instalación

1. **Clona el repositorio:**

```bash
git clone https://github.com/ZhinHxH/AIproject
```
2. **Posicionate en la carpeta de backend e instala los elementos con Poetry:**
Poetry install

4. **Posicionate en la carpeta de frontend e instala los paquete de node:**
npm install

5. **Crea una tabla en una base de datos de mysql llamada ygp1:**
CREATE TABLES classifier (
  ID AUTO_INCREMENT PRIMARY KEY,
  URL VARCHAR(100),
  TEXTO VARCHAR(1000),
  CLASIFICACION VARCHAR(100)
);

## Contribucion
Este proyecto fue desarrollado por Jhon Freddy Bolanos y Jhos Ben Xavio Hurtado para la materia de Proyectos de AI.

## Licencia

Este `readme.md` presenta una estructura organizada y visualmente atractiva, con imágenes, enlaces y bloques de código formateados. Puedes personalizarlo según las necesidades específicas de tu proyecto, asegurándote de incluir información relevante y atractiva para los usuarios potenciales.



