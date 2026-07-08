import subprocess

comprobantes = [
    # PayPal Receipts
    {
        "id": "0KJ003486E694464E",
        "cliente": "Klaus Espinoza",
        "fecha": "10 de junio de 2026",
        "monto": "9.00",
        "plan": "Optimización Estándar",
        "plataforma": "PayPal"
    },
    {
        "id": "0KL92031W89018100",
        "cliente": "JOSE PEREZ",
        "fecha": "6 de junio de 2026",
        "monto": "9.00",
        "plan": "Optimización Estándar",
        "plataforma": "PayPal"
    },
    {
        "id": "1A047551XY880674Y",
        "cliente": "Hector Cardenas",
        "fecha": "22 de mayo de 2026",
        "monto": "9.00",
        "plan": "Optimización Estándar",
        "plataforma": "PayPal"
    },
    {
        "id": "1C701186FV4351730",
        "cliente": "Mario Najera",
        "fecha": "29 de mayo de 2026",
        "monto": "27.00",
        "plan": "Mantenimiento Avanzado",
        "plataforma": "PayPal"
    },
    # dLocal Go Receipt
    {
        "id": "2176158326540103",
        "cliente": "Maria Fernanda Peñarrieta García",
        "fecha": "30 de junio de 2026",
        "monto": "9.00",
        "plan": "Optimización Estándar",
        "plataforma": "dLocal Go"
    },
    # Whop Receipt
    {
        "id": "pay_2x8zjX16m4o7tC",
        "cliente": "Salvador Rivera",
        "fecha": "6 de julio de 2026",
        "monto": "49.00",
        "plan": "Soporte Integral",
        "plataforma": "Whop"
    }
]

for c in comprobantes:
    print(f"Generando comprobante para {c['cliente']} ({c['plataforma']})...")
    cmd = [
        "python",
        "generar_comprobante_v2.py",
        "--id", c["id"],
        "--cliente", c["cliente"],
        "--fecha", c["fecha"],
        "--monto", c["monto"],
        "--plan", c["plan"],
        "--plataforma", c["plataforma"]
    ]
    subprocess.run(cmd, shell=True)

print("¡Todos los comprobantes se han regenerado exitosamente!")
