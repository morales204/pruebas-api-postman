# Ejemplo de API para Pruebas Automatizadas con Postman y GitHub Actions

Este proyecto contiene una API simple creada con FastAPI, diseñada para demostrar cómo automatizar pruebas de API utilizando Postman CLI y GitHub Actions.

## Estructura del Proyecto

```
.
├── .github/workflows/
│   └── test-api.yml      # Workflow de GitHub Actions
├── main.py               # Código de la API con FastAPI
├── requirements.txt      # Dependencias de Python
└── README.md             # Este archivo
```

## Uso en Local y Obtención de openapi.json

1.  **Crear y activar un entorno virtual:**
    Se recomienda encarecidamente usar un entorno virtual para aislar las dependencias del proyecto.

    ```bash
    # Crear el entorno virtual (puedes usar venv o .venv)
    python -m venv .venv

    # Activar en Linux/macOS
    source .venv/bin/activate

    # Para desactivar el entorno, simplemente ejecuta:
    # deactivate
    ```
    *Nota: Para activar en Windows, el comando puede variar (ej. `.\.venv\Scripts\Activate.ps1` en PowerShell).* 

2.  **Instalar dependencias:**
    Una vez que el entorno virtual esté activado, instale los paquetes necesarios.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar la API localmente:**
    ```bash
    uvicorn main:app --reload
    ```
    La API estará disponible en `http://127.0.0.1:8000`.

4.  **Acceder a la documentación y obtener `openapi.json`:**
    Abra su navegador y vaya a `http://127.0.0.1:8000/docs`. En la parte superior de la página, haga clic en el enlace `OpenAPI` (al lado del título de la API) para ver el JSON. Copie este contenido y guárdelo en un archivo `openapi.json` para usarlo en Postman.

## 🚀 Guía de Automatización de Pruebas de API (Postman CLI + GitHub Actions)

**Requerimientos:** Cuenta de Postman, Cuenta de GitHub.

### 1. Preparación en Postman
*   **Importación:** Cree una nueva API en su Workspace de Postman. En la sección **Define**, importe el archivo `openapi.json` que generó en el paso anterior.
*   **Generar Colección:** Postman usará la definición para generar automáticamente una colección de requests. Puede usar esta colección para las pruebas.
*   **Conexión:** Conecte la API de Postman a su repositorio de GitHub.
*   **Configuración CI/CD:** En la sección **Test and Automation**, Postman le permitirá generar una configuración para **GitHub Actions**. Copie el ID de la colección que se usará en el *workflow*.
*   **API Key:** Genere y **Copie la API Key** de Postman desde el [panel de configuración de su cuenta](https://go.postman.co/settings/me/api-keys).

### 2. Configuración de Seguridad en GitHub
*   **Secreto de Acción:** En su repositorio de GitHub, vaya a **Settings** → **Secrets and variables** → **Actions**.
*   **Registro de Clave:** Registre la clave copiada como un *Action Secret* con el nombre **`POSTMAN_API_KEY`**.

### 3. Configuración del Workflow
*   Abra el archivo `.github/workflows/test-api.yml`.
*   Reemplace el valor `YOUR_COLLECTION_ID` con el ID de la colección de Postman que obtuvo en el paso 1.

### 4. Ejecución y Verificación
*   **Subir Cambios:** Realice un **Commit y Push** de sus cambios al repositorio.
*   **Ejecución:** El GitHub Action se disparará automáticamente. Instalará **Postman CLI**, hará *login* con su API Key y ejecutará las pruebas de la colección especificada.
*   **Verificar:** Revise los *logs* en la pestaña **Actions** de su repositorio de GitHub para confirmar la ejecución de las pruebas y sus resultados.
