import os
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    generator_script = os.path.join(base_dir, "generar_comprobante.py")
    
    while True:
        clear_screen()
        print("=============================================================")
        print("   GENERADOR INTERACTIVO DE COMPROBANTES DE SOPORTE TI       ")
        print("=============================================================")
        print("Este script te ayudara a generar los PDFs para PayPal.")
        print("Escribe 'salir' en cualquier momento para terminar.\n")
        
        tx_id = input("1. ID de la Transaccion PayPal (ej: 1A047551XY880674Y): ").strip()
        if tx_id.lower() == 'salir':
            break
        if not tx_id:
            input("\nEl ID es obligatorio. Presiona Enter para continuar...")
            continue
            
        cliente = input("2. Nombre completo del Cliente (ej: Klaus Espinoza): ").strip()
        if cliente.lower() == 'salir':
            break
        if not cliente:
            input("\nEl nombre es obligatorio. Presiona Enter para continuar...")
            continue
            
        fecha = input("3. Fecha del Pago (ej: 10 de junio de 2026): ").strip()
        if fecha.lower() == 'salir':
            break
        if not fecha:
            input("\nLa fecha es obligatoria. Presiona Enter para continuar...")
            continue
            
        monto = input("4. Monto cobrado en USD (ej: 9.00 o 27.00): ").strip()
        if monto.lower() == 'salir':
            break
        if not monto:
            input("\nEl monto es obligatorio. Presiona Enter para continuar...")
            continue
            
        print("\nPlanes disponibles:")
        print("  1) Optimización Estándar ($9.00 USD)")
        print("  2) Mantenimiento Avanzado ($27.00 USD)")
        print("  3) Soporte Integral ($49.00 USD)")
        print("  4) Gestión VIP Corporativa ($95.00 USD)")
        plan_choice = input("5. Selecciona el numero de plan o escribe un nombre personalizado: ").strip()
        
        if plan_choice.lower() == 'salir':
            break
            
        if plan_choice == "1":
            plan = "Optimización Estándar"
        elif plan_choice == "2":
            plan = "Mantenimiento Avanzado"
        elif plan_choice == "3":
            plan = "Soporte Integral"
        elif plan_choice == "4":
            plan = "Gestión VIP Corporativa"
        elif plan_choice:
            plan = plan_choice
        else:
            plan = "Optimización Estándar"
            
        print("\n-------------------------------------------------------------")
        print("Generando comprobante...")
        
        # Call the generator script
        cmd = [
            "python", 
            generator_script,
            "--id", tx_id,
            "--cliente", cliente,
            "--fecha", fecha,
            "--monto", monto,
            "--plan", plan
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        print(result.stdout)
        if result.stderr:
            print("Detalles adicionales:", result.stderr)
            
        otra = input("\n¿Deseas generar otro comprobante? (s/n): ").strip().lower()
        if otra != 's' and otra != 'si':
            break
            
    print("\n¡Proceso finalizado! Los archivos PDF estan listos en la carpeta documentos_verificacion.")

if __name__ == "__main__":
    main()
