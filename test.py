import flet as ft

def main(page: ft.Page):
    page.title = "MediFlet"
    page.bgcolor=ft.colors.BLUE_50
   
    page.update()
   

 
if __name__ == "__main__":
    ft.app(target=main) 