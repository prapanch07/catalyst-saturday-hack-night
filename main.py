from ast import Lambda
import flet as ft

def main(page: ft.Page):
    page.title = "MediFlet"
    page.bgcolor=ft.colors.BLUE_50
    page.add(ft.Text("MediFlet",color= ft.colors.INDIGO_500,size=50)) 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.update()

    page.add(ft.ElevatedButton("Get Started", on_click=lambda _: page.go("/card")))

    def route_change(e: ft.RouteChangeEvent):
        if e.route == "/card":
            page.clean()
            page.add(ft.Text("Meditation is good for health",color=ft.colors.INDIGO_800,size=30))
            page.add(ft.IconButton(ft.icons.ARROW_FORWARD_IOS_ROUNDED,on_click=lambda _:page.go("/name")))
            page.update()
        elif e.route == "/name":
            page.clean()

        


    page.on_route_change = route_change
    page.update()

   

 
if __name__ == "__main__":
    ft.app(target=main) 