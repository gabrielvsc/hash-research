import hashlib
import bcrypt
import argon2

def generate_hashes(password):
    """Generates hashes for a set of algorithms."""
    hashes = {
        "MD5": hashlib.md5(password.encode()).hexdigest(),
        "SHA-1": hashlib.sha1(password.encode()).hexdigest(),
        "SHA-256": hashlib.sha256(password.encode()).hexdigest(),
        "bcrypt": bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode(),
        "Argon2": argon2.PasswordHasher().hash(password)
    }
    return hashes
