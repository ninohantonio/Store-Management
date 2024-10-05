import os

import bcrypt

from models.model_class import User
from services.article_service import session

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv('MAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

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

def check_if_mail_is_admin(email):
    user = session.query(User).filter_by(email=email).first()
    return user is not None

def send_email_confirmation_to_admin(email, object, message):
    try:
        # Création du message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email
        msg['Subject'] = object

        msg.attach(MIMEText(message, 'plain'))

        # Connexion au serveur SMTP
        serveur = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        serveur.starttls()  # Sécuriser la connexion
        serveur.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # Envoi de l'email
        texte = msg.as_string()
        serveur.sendmail(EMAIL_ADDRESS, email, texte)

        # Fermeture de la connexion
        serveur.quit()

        return True
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email: {e}")
        return False

def confirm_by_email(email):
    pass

def change_password(email):
    pass