from models.user_model import UserModel
from typing import Dict, Tuple

class RegisterController:
    def __init__(self):
        self.user_model = UserModel()

    def register_user(self, nombre: str, correo: str, edad: str) -> Tuple[bool, str]:
        """
        Registra un nuevo usuario
        Returns: (success: bool, message: str)
        """
        # Validar campos obligatorios
        if not nombre.strip():
            return False, "El nombre es obligatorio"

        if not correo.strip():
            return False, "El correo electrónico es obligatorio"

        if not edad.strip():
            return False, "La edad es obligatoria"

        # Validar formato de correo (básico)
        if '@' not in correo or '.' not in correo:
            return False, "El correo electrónico no tiene un formato válido"

        # Validar que la edad sea un número
        try:
            edad_int = int(edad)
            if edad_int < 1 or edad_int > 120:
                return False, "La edad debe estar entre 1 y 120 años"
        except ValueError:
            return False, "La edad debe ser un número válido"

        # Preparar datos del usuario
        user_data = {
            'nombre': nombre.strip(),
            'correo': correo.strip().lower(),
            'edad': edad.strip()
        }

        # Intentar guardar
        if self.user_model.save_user(user_data):
            return True, f"¡Registro exitoso! Bienvenido {nombre}"
        else:
            return False, "El correo electrónico ya está registrado"