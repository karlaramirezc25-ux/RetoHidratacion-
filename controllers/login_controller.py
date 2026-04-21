from models.user_model import UserModel
from typing import Tuple

class LoginController:
    def __init__(self):
        self.user_model = UserModel()

    def authenticate_user(self, email: str, password: str) -> Tuple[bool, str, dict]:
        """
        Autentica a un usuario
        Returns: (success: bool, message: str, user_data: dict)
        """
        # Validar campos obligatorios
        if not email.strip():
            return False, "El correo electrónico es obligatorio", {}

        if not password.strip():
            return False, "La contraseña es obligatoria", {}

        # Buscar usuario por email
        user = self.user_model.find_user_by_email(email.strip().lower())

        if user is None:
            return False, "Usuario no encontrado", {}

        # Por ahora, como no tenemos contraseñas reales, aceptamos cualquier contraseña
        # En un sistema real, aquí verificaríamos el hash de la contraseña
        return True, f"Bienvenido {user['nombre']}!", user