import uasyncio as asyncio

def clear_request(request):
    """
    Extrae la ruta de una cadena de solicitud HTTP.

    Esta función toma una cadena de solicitud HTTP en bruto y extrae el 
    componente de la ruta de la misma. La ruta es la parte de la solicitud 
    que sigue al método HTTP y antes de la versión HTTP.

    Args:
        request (str): La cadena de solicitud HTTP en bruto. Ejemplo:
                       "GET /ruta/al/recurso HTTP/1.1"

    Returns:
        str: La ruta extraída de la solicitud HTTP. Ejemplo:
             "/ruta/al/recurso"
    """
    return str(request).split(" ")[1]

async def handle_client(reader, writer):
    # Lee la solicitud del cliente
    request = await asyncio.wait_for(reader.read(1024), timeout=5)  # Timeout de 5 segundos
    print("Solicitud recibida:", clear_request(request))

    # Respuesta HTTP básica
    response = """\
HTTP/1.1 200 OK
Content-Type: text/html

<html>
<head>
    <title>MicroPython Server</title>
</head>
<body>
    <h1>Hello from MicroPython!</h1>
</body>
</html>
"""
    # Envía la respuesta al cliente
    writer.write(response)
    await writer.drain()

    await writer.wait_closed()


async def run_server():
    # Inicia el servidor en la dirección y puerto especificados
    server = await asyncio.start_server(handle_client, "0.0.0.0", 8080)
    print("Servidor corriendo en 0.0.0.0:8080")
    while True:
        await asyncio.sleep(1)  # Mantén el servidor corriendo

try:
    # Ejecuta el servidor de manera asíncrona
    asyncio.run(run_server())

except KeyboardInterrupt:
    print("Servidor detenido")
