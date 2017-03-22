from signxml import XMLSigner, XMLVerifier

signer = XMLSigner()
verifier = XMLVerifier()

def sign(tree, key, cert, **kwargs):
    return signer.sign(tree, key=key, cert=cert, **kwargs)

def verify(tree, **kwargs):
    return bool(verifier.verify(tree, **kwargs).signed_xml)
