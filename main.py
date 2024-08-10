import uasyncio as asyncio

async def handle_client(reader, writer):
    # Lee la solicitud del cliente
    request = await asyncio.wait_for(reader.read(1024), timeout=5)  # Timeout de 5 segundos

    print("Solicitud recibida:", request)

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
