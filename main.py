import flet as ft
from views.welcome_view import WelcomeView
from views.login_View import LoginView
from views.register_View import RegisterView

def main(page: ft.Page):
    page.title = "HydroBoost"
    page.window_width = 400
    page.window_height = 700
    page.theme_mode = ft.ThemeMode.LIGHT 

    def cambiar_ruta(e):
        ruta = page.route 
        print(f"--- DISPARANDO RUTEADOR: {ruta} ---")
        
        page.views.clear()
        
        if ruta == "/":
            # Nota: Mantenemos el .build() porque así diseñamos nuestras clases actuales
            content = WelcomeView(page).build()
            page.views.append(
                ft.View(
                    route="/", 
                    controls=[content],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
            
        elif ruta == "/login":
            content = LoginView(page).build()
            page.views.append(
                ft.View(
                    route="/login", 
                    controls=[content],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

        elif ruta == "/register":
            content = RegisterView(page).build()
            page.views.append(
                ft.View(
                    route="/register", 
                    controls=[content],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
            
        page.update()

    def retroceder_vista(e):
        page.views.pop()
        vista_anterior = page.views[-1]
        page.go(vista_anterior.route)

    # 1. Asignamos los eventos
    page.on_route_change = cambiar_ruta
    page.on_view_pop = retroceder_vista
    
    # 2. TU SOLUCIÓN: Inicializamos la ruta si está vacía
    if not page.route:
        page.route = "/"
    
    # 3. TU SOLUCIÓN: Forzamos la ejecución del ruteador la primera vez
    cambiar_ruta(None)

# Usaremos ft.app clásico para evitar que se detenga
ft.app(target=main)