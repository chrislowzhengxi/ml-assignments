import http.server
import ssl

server_address = ('localhost', 4443)
key_file = "key.pem"
cert_file = "cert.pem"

httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=cert_file, keyfile=key_file)

# Wrap the socket using the context
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Starting HTTPS server on https://{server_address[0]}:{server_address[1]} ...")
httpd.serve_forever()
