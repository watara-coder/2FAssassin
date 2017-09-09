#!/usr/bin/env python


import OpenSSL.crypto
from Crypto.Util import asn1
from leakcheck import *

c=OpenSSL.crypto

# The certificate - an X509 object
#cert=...
cert="ClientCert.pfx"

# The private key - a PKey object
#priv=...

priv="private_key.pem"

pub=cert.get_pubkey()

# Only works for RSA (I think)
if pub.type()!=c.TYPE_RSA or priv.type()!=c.TYPE_RSA:
    raise Exception('Can only handle RSA keys')

# This seems to work with public as well
pub_asn1=c.dump_privatekey(c.FILETYPE_ASN1, pub)
priv_asn1=c.dump_privatekey(c.FILETYPE_ASN1, priv)

# Decode DER
pub_der=asn1.DerSequence()
pub_der.decode(pub_asn1)
priv_der=asn1.DerSequence()
priv_der.decode(priv_asn1)

# Get the modulus
pub_modulus=pub_der[1]
priv_modulus=priv_der[1]

if pub_modulus==priv_modulus:
    print('Match')
else:
    print('Oops')
