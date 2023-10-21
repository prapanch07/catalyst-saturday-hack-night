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
            page.add(ft.Text("what do you love to be called today ?",color=ft.colors.INDIGO_800,size=30)) 
            page.add(ft.TextField(label="Name",text_size=18 ,color=ft.colors.INDIGO_800,width=350,border_color=ft.colors.BLACK12))
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.add(ft.IconButton(ft.icons.ARROW_FORWARD_IOS_ROUNDED,on_click=lambda _:page.go("/time")))
            page.update()
        elif e.route == "/time":
            page.clean()
            page.add(ft.Text("how much time do you need to meditate ?",color=ft.colors.INDIGO_800,size=30)) 
            page.add(ft.Slider(width=300,value=5,min=0,max=20,divisions=20,label="{value}min")) 
            page.add(ft.IconButton(ft.icons.ARROW_FORWARD_IOS_ROUNDED,on_click=lambda _:page.go("/music")))
            page.update()  
        elif e.route == "/music":
            page.clean()
            page.add(ft.Text("which type of music needed ?",color=ft.colors.INDIGO_800,size=30)) 
         
            page.update()
 
 
 
    page.on_route_change = route_change
    page.update()

   

 
if __name__ == "__main__":
    ft.app(target=main) 