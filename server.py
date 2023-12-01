import http.server
import socketserver
import ssl

# Configura el nombre del archivo del certificado y la clave privada
certfile = './cert/vod.vcmedios.tv.crt'  # Reemplaza con la ruta de tu certificado
keyfile = './cert/vod.vcmedios.tv.key'  # Reemplaza con la ruta de tu clave privada

# Configura el número de puerto y el servidor
port = 8443  # Puerto para HTTPS

# Configura el manejador del servidor
handler = http.server.SimpleHTTPRequestHandler

# Crea un objeto SSLContext para configurar el servidor SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile, keyfile)

# Crea el servidor HTTP con SSL
with socketserver.TCPServer(("", port), handler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print(f"Servidor HTTPS ejecutándose en el puerto {port}")
    httpd.serve_forever()
