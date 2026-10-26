import ssl

import certifi

certificate = certifi.where()
assert certificate.endswith("cacert.pem")

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile=certificate)
assert context.cert_store_stats()["x509"] > 0
