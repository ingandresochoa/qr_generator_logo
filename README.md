# QR Generator Logo - Web Application

Una aplicación web para generar códigos QR personalizados con logos. Esta herramienta permite a los usuarios crear códigos QR únicos combinando sus URLs o texto con logos personalizados.

## 🚀 Características

- Generación de códigos QR con logos personalizados
- Interfaz web intuitiva y responsiva
- Vista previa instantánea del QR generado
- Opción de descarga del QR en formato PNG
- Manejo de errores y validaciones
- Soporte para diferentes formatos de imagen para el logo

## 📋 Prerequisitos

```bash
- Python 3.7 o superior
- pip (gestor de paquetes de Python)
```

## 🔧 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/ingandresochoa/qr_generator_logo
cd qr-generator
```

2. **Crear y activar un entorno virtual (opcional pero recomendado)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar las dependencias**
```bash
pip install flask pillow qrcode flask-cors
```

## 📁 Estructura del Proyecto

```
qr_generator_logo/
│
├── main.py              # Servidor Flask
├── README.md            # Este archivo
├── static/              # Archivos estáticos
│   └── uploads/         # Carpeta para uploads temporales
└── templates/
    └── index.html       # Interfaz de usuario
```

## 🚀 Ejecución del Proyecto

1. **Iniciar el servidor Flask**
```bash
python main.py
```

2. **Acceder a la aplicación**
- Abrir el navegador y visitar: `http://127.0.0.1:5000`

## 💻 Uso

1. Ingresar la URL o texto que se desea codificar en el QR
2. Seleccionar un archivo de imagen para usar como logo
3. Hacer clic en "Generar QR"
4. Visualizar el QR generado
5. Descargar el QR usando el botón "Descargar QR"

## 📝 Notas Importantes

- Los logos deben tener un formato de imagen válido (PNG, JPG, JPEG)
- El tamaño del logo se ajusta automáticamente al 25% del código QR
- El código QR mantiene su funcionalidad gracias al nivel alto de corrección de errores

## ⚙️ Configuración Adicional

El archivo `main.py` contiene variables que pueden ser modificadas según necesidades específicas:

```python
# Tamaño del logo respecto al QR
logo_size_ratio=0.25

# Configuración del QR
version=1
box_size=10
border=4
```

## 🛠️ Construido con

- [Flask](https://flask.palletsprojects.com/) - Framework web
- [qrcode](https://github.com/lincolnloop/python-qrcode) - Generación de códigos QR
- [Pillow](https://python-pillow.org/) - Procesamiento de imágenes
- [Bootstrap](https://getbootstrap.com/) - Framework CSS

## ✨ Mejoras Futuras Posibles

- [ ] Personalización de colores del QR
- [ ] Ajuste del tamaño del logo
- [ ] Vista previa del logo antes de generar
- [ ] Diferentes formatos de salida (SVG, PDF)
- [ ] Historial de QRs generados

## 🎯 Resolución de Problemas Comunes

### Error: "Method Not Allowed"
- Asegúrese de que el servidor Flask esté corriendo
- Verifique que está usando la URL correcta

### Error al subir imagen
- Verifique que el formato de imagen es soportado
- Compruebe los permisos de la carpeta `uploads`
- Verifique el tamaño del archivo

### QR no escanenable
- Use imágenes de logo más pequeñas o transparentes
- Reduzca la complejidad del texto codificado
- Aumente el nivel de corrección de errores

## 👥 Contacto y Soporte

Para reportar problemas o sugerir mejoras, por favor:
1. Abra un issue en el repositorio
2. Envíe un pull request con sus mejoras
3. Contacte al equipo de desarrollo

---
⌨️ with ❤️ ingandresochoa 💡
