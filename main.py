from ast import Lambda
import flet as ft

def main(page: ft.Page):
    page.title = "MediFlet"
    page.bgcolor=ft.colors.BLUE_50
    page.add(ft.Text("MediFlet",color= ft.colors.INDIGO_500,size=50)) 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(ft.IconButton(icon=ft.icons.ARROW_FORWARD,icon_color=ft.colors.INDIGO_500,icon_size=25,on_click= Lambda:page.go("/test.py")))
    
    page.update()
   

 
if __name__ == "__main__":
    ft.app(target=main) 