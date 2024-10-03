import bcrypt

from models.model_class import User
from services.article_service import session


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')  # Convertir les octets en chaîne de caractères

def create_user(email, password):
    if session.query(User).filter_by(email=email).first():
        session.close()
        raise ValueError("Utilisateur déjà existant")
    user = User(email=email, password_hash=hash_password(password))
    session.add(user)
    session.commit()
    session.close()


def verify_password(email, provided_password):
    user = session.query(User).filter_by(email=email).first()
    session.close()
    if user:
        if isinstance(user.password_hash, str):
            password_hash_bytes = user.password_hash.encode('utf-8')
            return bcrypt.checkpw(provided_password.encode('utf-8'), password_hash_bytes)
    return False