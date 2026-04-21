import flet as ft
from controllers.login_controller import LoginController

class LoginView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.controller = LoginController()

    def build(self):
        titulo = ft.Text(value="Iniciar Sesión", size=30, color=ft.Colors.BLUE_900, weight=ft.FontWeight.BOLD)
        
        self.input_usuario = ft.TextField(label="Correo Electrónico", border_color=ft.Colors.BLUE_400, prefix_icon=ft.Icons.PERSON_OUTLINE)
        self.input_password = ft.TextField(label="Contraseña", border_color=ft.Colors.BLUE_400, prefix_icon=ft.Icons.LOCK, password=True, can_reveal_password=True)
        
        # Área para mensajes
        self.mensaje_text = ft.Text("", size=14)
        
        boton_ingresar = ft.ElevatedButton(
            "Ingresar", 
            bgcolor=ft.Colors.CYAN_700, 
            color=ft.Colors.WHITE, 
            width=200,
            on_click=self._handle_login
        )
        
        # Agregamos on_click para ir a la ruta /register
        boton_registro = ft.TextButton(
            "¿No tienes cuenta? Regístrate aquí",
            icon=ft.Icons.APP_REGISTRATION,
            icon_color=ft.Colors.BLUE_600,
            # ACTUALIZADO AQUÍ:
            on_click=lambda e: self.page.go("/register")
        )
        

        columna_login = ft.Column(
            controls=[
                titulo, 
                ft.Container(height=20), 
                self.input_usuario, 
                self.input_password, 
                ft.Container(height=10),
                self.mensaje_text,
                ft.Container(height=10),
                boton_ingresar, 
                boton_registro
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=320 
        )
        
        return columna_login

    def _handle_login(self, e):
        """Maneja el proceso de login"""
        # Limpiar mensaje anterior
        self.mensaje_text.value = ""
        self.page.update()

        # Obtener valores de los campos
        email = self.input_usuario.value or ""
        password = self.input_password.value or ""

        # Intentar autenticar
        success, message, user_data = self.controller.authenticate_user(email, password)

        if success:
            # Login exitoso
            self.mensaje_text.color = ft.Colors.GREEN_700
            self.mensaje_text.value = message

            # Limpiar campos
            self.input_usuario.value = ""
            self.input_password.value = ""

            # Actualizar página
            self.page.update()

            # Aquí podrías navegar a una vista de dashboard o welcome
            # Por ahora, solo mostramos el mensaje de éxito
        else:
            # Error en login
            self.mensaje_text.color = ft.Colors.RED_700
            self.mensaje_text.value = message
            self.page.update()