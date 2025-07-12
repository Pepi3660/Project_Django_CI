
# Proyecto Django CI

Este proyecto es una base para el desarrollo colaborativo de una aplicación Django con integración continua (CI). Aquí encontrarás las instrucciones para contribuir y mantener un flujo de trabajo ordenado.

## 📁 Estructura de Ramas

- `master`: Versión estable y lista para producción.
- `develop`: Versión en desarrollo donde se integran nuevas funcionalidades.
- `feature/nombre-funcionalidad`: Ramas temporales para el desarrollo de nuevas funciones.

## 🚀 Cómo contribuir

### 1. Clona el repositorio

git clone https://github.com/Pepi3660/Project_Django_CI.git
cd Project_Django_CI
## 2. Crea tu rama desde develop

git checkout develop
git pull origin develop
git checkout -b feature/nombre-funcionalidad

## Ejemplo: git checkout -b feature/login

# 3. Trabaja, guarda y haz commit

git add .
git commit -m "Implementa formulario de login"

# 4. Sube tu rama al repositorio
git push -u origin feature/login


# 5. Crea un Pull Request (PR)
Ve a GitHub y crea un PR desde tu rama feature/... hacia develop.
Agrega una descripción clara de los cambios realizados.
Espera la revisión y aprobación.

# 🔁 Sincronizar tu rama con develop
Antes de seguir trabajando:

git checkout develop
git pull origin develop
git checkout feature/nombre-funcionalidad
git merge develop

# ✅ Mezclar a producción
Una vez probados los cambios en develop, se puede hacer merge a master:

git checkout master
git pull origin master
git merge develop
git push origin master
# 🧹 Limpieza de ramas
Después de hacer merge de una funcionalidad:

git branch -d feature/nombre-funcionalidad     # Eliminar localmente
git push origin --delete feature/nombre-funcionalidad  # Eliminar remoto

# Buenas prácticas
No trabajes directamente en develop ni master.
Usa commits descriptivos.
Haz pull frecuentemente.
Revisa el código de antes de aprobar.
