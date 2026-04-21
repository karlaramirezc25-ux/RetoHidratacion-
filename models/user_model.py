import json
import os
from typing import Dict, List, Optional

class UserModel:
    def __init__(self, data_file: str = "users.json"):
        self.data_file = data_file
        self._ensure_data_file()

    def _ensure_data_file(self):
        """Asegura que el archivo de datos existe"""
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump([], f)

    def save_user(self, user_data: Dict[str, str]) -> bool:
        """Guarda un nuevo usuario"""
        try:
            # Leer usuarios existentes
            with open(self.data_file, 'r') as f:
                users = json.load(f)

            # Verificar si el correo ya existe
            for user in users:
                if user.get('correo') == user_data.get('correo'):
                    return False  # Usuario ya existe

            # Agregar nuevo usuario
            users.append(user_data)

            # Guardar
            with open(self.data_file, 'w') as f:
                json.dump(users, f, indent=2)

            return True
        except Exception as e:
            print(f"Error al guardar usuario: {e}")
            return False

    def get_all_users(self) -> List[Dict[str, str]]:
        """Obtiene todos los usuarios"""
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except:
            return []

    def find_user_by_email(self, email: str) -> Optional[Dict[str, str]]:
        """Busca un usuario por correo electrónico"""
        users = self.get_all_users()
        for user in users:
            if user.get('correo') == email:
                return user
        return None