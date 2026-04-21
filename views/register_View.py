import flet as ft
from controllers.register_controller import RegisterController

class RegisterView:
    def __init__(self, page: ft.Page):
        self.page = page
        self.controller = RegisterController()

    def build(self):
        # 1. Título con estilo
        titulo = ft.Text(
            value="Crear Cuenta",
            size=30,
            color=ft.Colors.BLUE_900,
            weight=ft.FontWeight.BOLD
        )

        subtitulo = ft.Text(
            value="¡Únete al reto de la hidratación!",
            size=16,
            color=ft.Colors.BLUE_GREY_700
        )

        # 2. Campos de entrada de datos
        self.input_nombre = ft.TextField(
            label="Nombre Completo",
            prefix_icon=ft.Icons.PERSON_OUTLINE,
            border_color=ft.Colors.BLUE_400,
            hint_text="Ej. Ana Rodríguez"
        )

        self.input_correo = ft.TextField(
            label="Correo Electrónico",
            prefix_icon=ft.Icons.EMAIL_OUTLINED,
            border_color=ft.Colors.BLUE_400,
            keyboard_type=ft.KeyboardType.EMAIL,
            hint_text="ejemplo@correo.com"
        )

        self.input_edad = ft.TextField(
            label="Edad",
            prefix_icon=ft.Icons.CAKE_OUTLINED,
            border_color=ft.Colors.BLUE_400,
            keyboard_type=ft.KeyboardType.NUMBER,
            width=150 # La edad no necesita tanto espacio
        )

        # Área para mensajes
        self.mensaje_text = ft.Text("", size=14)

        # 3. Botones
        boton_registrar = ft.ElevatedButton(
            "Finalizar Registro",
            bgcolor=ft.Colors.CYAN_700,
            color=ft.Colors.WHITE,
            width=250,
            height=50,
            on_click=self._handle_register
        )

        boton_regresar = ft.TextButton(
            "¿Ya tienes cuenta? Inicia sesión",
            on_click=lambda _: self.page.go("/login")
        )

        # 4. Organización visual (Layout)
        # Usamos una columna para apilar todo verticalmente
        registro_container = ft.Column(
            controls=[
                titulo,
                subtitulo,
                ft.Container(height=10), # Espaciador
                self.input_nombre,
                self.input_correo,
                self.input_edad,
                ft.Container(height=10), # Espaciador
                self.mensaje_text,
                ft.Container(height=10), # Espaciador
                boton_registrar,
                boton_regresar
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )

        return registro_container

    def _handle_register(self, e):
        """Maneja el proceso de registro"""
        # Limpiar mensaje anterior
        self.mensaje_text.value = ""
        self.page.update()

        # Obtener valores de los campos
        nombre = self.input_nombre.value or ""
        correo = self.input_correo.value or ""
        edad = self.input_edad.value or ""

        # Intentar registrar
        success, message = self.controller.register_user(nombre, correo, edad)

        if success:
            # Registro exitoso
            self.mensaje_text.color = ft.Colors.GREEN_700
            self.mensaje_text.value = message

            # Limpiar campos
            self.input_nombre.value = ""
            self.input_correo.value = ""
            self.input_edad.value = ""

            # Actualizar página
            self.page.update()

            # Navegar al login después de 2 segundos
            import time
            self.page.run_task(self._delayed_navigation)
        else:
            # Error en registro
            self.mensaje_text.color = ft.Colors.RED_700
            self.mensaje_text.value = message
            self.page.update()

    async def _delayed_navigation(self):
        """Navegación retardada al login"""
        import asyncio
        await asyncio.sleep(2)
        self.page.go("/login")