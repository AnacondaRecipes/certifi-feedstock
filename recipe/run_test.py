import certifi
import pip

if hasattr(pip, 'main'):
    pip.main(['install', "pem"])
else:
    pip._internal.main(['install', "pem"])

certificate = certifi.where()
assert certificate[-10::] == "cacert.pem", "Unable to find the certificate"
import pem
certs = pem.parse_file(certificate)
cert_key = str(certs[0])
assert cert_key != None, "Failed to find the valid certificate "