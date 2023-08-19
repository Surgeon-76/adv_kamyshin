import binascii
import hashlib
import os


def hash_password(password: str) -> str:
    """Hash a password for storing."""
    salt = b'__hash__' + hashlib.sha256(
        os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def is_hash(pw: str) -> bool:
    return pw.startswith('__hash__') and len(pw) == 200


def verify_password(stored_password: str, provided_password: str) -> bool:
    """Verify a stored password against one provided by user"""
    salt = stored_password[:72]
    stored_password = stored_password[72:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)

    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
