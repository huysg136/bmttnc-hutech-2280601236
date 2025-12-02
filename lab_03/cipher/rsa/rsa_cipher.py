import rsa
import os

KEYS_DIR = "./Lab-03/cipher/rsa/keys"
os.makedirs(KEYS_DIR, exist_ok=True)

PUBLIC_KEY_FILE = os.path.join(KEYS_DIR, "public.pem")
PRIVATE_KEY_FILE = os.path.join(KEYS_DIR, "private.pem")

class RSACipher:
    def generate_keys(self):
        (pub_key, priv_key) = rsa.newkeys(2048)
        with open(PUBLIC_KEY_FILE, "wb") as f:
            f.write(pub_key.save_pkcs1("PEM"))
        with open(PRIVATE_KEY_FILE, "wb") as f:
            f.write(priv_key.save_pkcs1("PEM"))
        return {"message": "RSA keys generated successfully!"}

    def load_keys(self):
        with open(PRIVATE_KEY_FILE, "rb") as f:
            priv_key = rsa.PrivateKey.load_pkcs1(f.read())
        with open(PUBLIC_KEY_FILE, "rb") as f:
            pub_key = rsa.PublicKey.load_pkcs1(f.read())
        return priv_key, pub_key

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode(), key)

    def decrypt(self, ciphertext, key):
        return rsa.decrypt(ciphertext, key).decode()

    def sign(self, message, key):
        return rsa.sign(message.encode(), key, "SHA-256")

    def verify(self, message, signature, key):
        try:
            rsa.verify(message.encode(), signature, key)
            return True
        except rsa.VerificationError:
            return False