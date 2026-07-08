import os
import sys
import subprocess
import argparse

def create_html_content(tx_id, client_name, date, amount, plan):
    # Determine plan description based on the plan name
    if "avanzado" in plan.lower():
        desc = "Mantenimiento avanzado de sistemas, actualización de controladores y soporte de red remota."
    elif "integral" in plan.lower():
        desc = "Auditoría de seguridad integral, remoción preventiva de malware y configuración de copias de seguridad."
    elif "vip" in plan.lower() or "corporativa" in plan.lower():
        desc = "Gestión VIP corporativa de sistemas, soporte 24/7 y consultoría técnica dedicada."
    else:
        desc = "Optimización estándar mensual para sistemas, limpieza lógica de temporales y diagnóstico remoto básico."

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Comprobante de Entrega - OptimaIT</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            color: #2D3748;
            line-height: 1.6;
            margin: 40px;
            background-color: #FFFFFF;
        }}
        .header {{
            border-bottom: 2px solid #2B6CB0;
            padding-bottom: 15px;
            margin-bottom: 25px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .logo {{
            font-size: 26px;
            font-weight: bold;
            color: #1A365D;
        }}
        .logo span {{
            color: #3182CE;
        }}
        .doc-type {{
            background-color: #EBF8FF;
            color: #2B6CB0;
            padding: 6px 12px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .provider-info {{
            font-size: 13px;
            color: #4A5568;
            margin-bottom: 20px;
        }}
        h1 {{
            color: #1A365D;
            font-size: 22px;
            margin-bottom: 20px;
        }}
        .details-table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 30px;
        }}
        .details-table th, .details-table td {{
            border: 1px solid #E2E8F0;
            padding: 12px;
            text-align: left;
            font-size: 14px;
        }}
        .details-table th {{
            background-color: #F7FAFC;
            color: #4A5568;
            width: 35%;
        }}
        .details-table td {{
            color: #2D3748;
            font-weight: bold;
        }}
        .fulfillment-box {{
            background-color: #F0FFF4;
            border: 1px solid #C6F6D5;
            border-radius: 6px;
            padding: 20px;
            margin-bottom: 30px;
        }}
        .fulfillment-title {{
            color: #22543D;
            font-weight: bold;
            font-size: 15px;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .fulfillment-desc {{
            color: #2F855A;
            font-size: 13.5px;
        }}
        .footer {{
            margin-top: 60px;
            border-top: 1px solid #E2E8F0;
            padding-top: 15px;
            font-size: 12px;
            color: #A0AEC0;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">Optima<span>IT</span></div>
        <div class="doc-type">Confirmación de Cumplimiento</div>
    </div>

    <div class="provider-info">
        <strong>Prestador del Servicio:</strong> Dantro Tech Solutions (Profesional Freelance)<br>
        <strong>Sitio Web Oficial:</strong> https://optimait.site/<br>
        <strong>Contacto:</strong> soporte@dantro.tech / WhatsApp: +51 914 326 729
    </div>

    <h1>Detalle del Servicio Entregado</h1>
    
    <table class="details-table">
        <tr>
            <th>ID de Transacción PayPal</th>
            <td>{tx_id}</td>
        </tr>
        <tr>
            <th>Cliente</th>
            <td>{client_name}</td>
        </tr>
        <tr>
            <th>Fecha de Pago</th>
            <td>{date}</td>
        </tr>
        <tr>
            <th>Concepto / Plan</th>
            <td>{plan} (${amount} USD)</td>
        </tr>
        <tr>
            <th>Tipo de Entrega</th>
            <td>Entrega Digital mediante Soporte Remoto</td>
        </tr>
        <tr>
            <th>Estado de Cumplimiento</th>
            <td style="color: #2F855A;">100% Entregado y Concluido</td>
        </tr>
    </table>

    <div class="fulfillment-box">
        <div class="fulfillment-title">✓ Declaración de Entrega del Servicio:</div>
        <div class="fulfillment-desc">
            El servicio de <strong>{plan}</strong> fue realizado y entregado a entera satisfacción del cliente. 
            Detalle del servicio ejecutado de forma remota: {desc} 
            Toda la coordinación de accesos se realizó por canales digitales directos (WhatsApp/Email) 
            y la intervención se ejecutó mediante software de asistencia remota segura.
        </div>
    </div>

    <div class="footer">
        Este documento certifica la correcta ejecución del servicio intangible contratado de manera digital.<br>
        OptimaIT — Dantro Tech Solutions © 2026. Todos los derechos reservados.
    </div>
</body>
</html>
"""
    return html

def main():
    parser = argparse.ArgumentParser(description="Generar PDF de comprobante de entrega para PayPal")
    parser.add_argument("--id", required=True, help="ID de la transacción")
    parser.add_argument("--cliente", required=True, help="Nombre del cliente")
    parser.add_argument("--fecha", required=True, help="Fecha del pago")
    parser.add_argument("--monto", required=True, help="Monto cobrado en USD")
    parser.add_argument("--plan", required=True, help="Nombre del plan (ej: Optimización Estándar)")
    
    args = parser.parse_args()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_filename = f"temp_{args.id}.html"
    pdf_filename = f"comprobante_{args.id}.pdf"
    
    html_path = os.path.join(base_dir, html_filename)
    pdf_path = os.path.join(base_dir, pdf_filename)
    
    # Write temporary HTML
    html_content = create_html_content(args.id, args.cliente, args.fecha, args.monto, args.plan)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"HTML temporal creado en: {html_path}")
    
    # Locate msedge
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_path):
        edge_path = "msedge"
        
    # Compile HTML to PDF
    print(f"Generando PDF {pdf_filename}...")
    subprocess.run([
        edge_path, 
        "--headless", 
        "--disable-gpu", 
        "--no-pdf-header-footer", 
        f"--print-to-pdf={pdf_path}", 
        html_path
    ], shell=True)
    
    # Clean up HTML
    if os.path.exists(html_path):
        os.remove(html_path)
        
    if os.path.exists(pdf_path):
        print(f"Exito: PDF generado correctamente en: {pdf_path}")
    else:
        print("Error: No se pudo generar el archivo PDF.")

if __name__ == "__main__":
    main()
