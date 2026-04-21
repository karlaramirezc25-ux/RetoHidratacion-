import flet as ft

class WelcomeView:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        icono = ft.Icon(ft.Icons.WATER_DROP, color=ft.Colors.BLUE_400, size=100)
        titulo = ft.Text("¡Bienvenido a HydroBoost!", size=30, color=ft.Colors.BLUE_900)
        
        # Agregamos on_click para ir a la ruta /login
        boton = ft.ElevatedButton(
            "Entrar", 
            bgcolor=ft.Colors.CYAN_700, 
            color=ft.Colors.WHITE,
            on_click=lambda e: self.page.go("/login")
        )

        columna_principal = ft.Column(
            controls=[icono, titulo, boton],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        return columna_principal