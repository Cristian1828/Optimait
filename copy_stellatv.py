import os
import shutil
from pathlib import Path
import sys

# Configuración
ORIGEN = r"C:\Users\dante\OneDrive\Documentos\Flujo-Landings(10)"
DESTINO_PADRE = os.path.join(ORIGEN, "stellatv")
EXCLUIR = {"node_modules", "dist", ".git", ".astro"}

def ignore_patterns(dir_name, files):
    """Función para ignorar directorios específicos"""
    ignored = set()
    for f in files:
        if f in EXCLUIR:
            ignored.add(f)
    return ignored

def main():
    # Crear carpeta destino
    os.makedirs(DESTINO_PADRE, exist_ok=True)
    print(f"✓ Carpeta destino creada: {DESTINO_PADRE}\n")
    
    # Listar todos los items
    try:
        items = sorted(os.listdir(ORIGEN))
    except Exception as e:
        print(f"✗ Error al listar {ORIGEN}: {e}")
        return
    
    # Procesar directorios FlujoTV
    carpetas_creadas = []
    
    for item in items:
        ruta_item = os.path.join(ORIGEN, item)
        
        # Verificar si es directorio y comienza con FlujoTV
        if os.path.isdir(ruta_item) and item.startswith("FlujoTV"):
            # Renombrar FlujoTV -> StellaTV
            nuevo_nombre = item.replace("FlujoTV", "StellaTV", 1)
            ruta_destino = os.path.join(DESTINO_PADRE, nuevo_nombre)
            
            try:
                # Copiar directorio excluyendo carpetas
                shutil.copytree(ruta_item, ruta_destino, ignore=ignore_patterns)
                carpetas_creadas.append(nuevo_nombre)
                print(f"✓ Copiada: {item} → {nuevo_nombre}")
            except Exception as e:
                print(f"✗ Error al copiar {item}: {e}")
    
    # Resumen
    print("\n" + "="*60)
    print("CARPETAS CREADAS EN stellatv:")
    print("="*60)
    
    for carpeta in carpetas_creadas:
        print(f"  • {carpeta}")
    
    print(f"\nTotal: {len(carpetas_creadas)} carpeta(s) copiada(s)")
    
    # Verificar que las carpetas existan
    print("\n" + "="*60)
    print("VERIFICACIÓN:")
    print("="*60)
    
    try:
        items_creados = sorted(os.listdir(DESTINO_PADRE))
        print(f"Contenido de {DESTINO_PADRE}:")
        for item in items_creados:
            ruta = os.path.join(DESTINO_PADRE, item)
            if os.path.isdir(ruta):
                try:
                    tamaño = sum(
                        f.stat().st_size 
                        for f in Path(ruta).rglob('*') 
                        if f.is_file()
                    ) / (1024*1024)  # MB
                    print(f"  • {item} ({tamaño:.2f} MB)")
                except:
                    print(f"  • {item}")
    except Exception as e:
        print(f"Error verificando: {e}")

if __name__ == "__main__":
    main()
