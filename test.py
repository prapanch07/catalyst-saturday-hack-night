import flet as ft

def main(page: ft.Page):
    page.bgcolor=ft.colors.BLUE_50
    def button_clicked(e):
        t.value = dd.value
        page.update()
        page.go("/time")

    t = ft.Text()
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    dd = ft.TextField(label="Standard")
    page.add(dd, b, t)

    def route_change(e: ft.RouteChangeEvent):
        if e.route == "/time":
            page.clean()
            tt = ft.Text("!!, How much time do you want to meditate ?",color=ft.colors.INDIGO_800,size=30)
            x = t.value
            y = tt.value
            page.add(ft.Text(x+y))
            page.add(ft.Text("Start with a small amount like 3 minutes",color=ft.colors.INDIGO_400,size=20)) 
            page.add(ft.Slider(width=300,value=5,min=0,max=20,divisions=20,label="{value}min")) 
            page.add(ft.IconButton(ft.icons.ARROW_FORWARD_IOS_ROUNDED,on_click=lambda _:page.go("/music")))
            page.update()  
      

 

    page.on_route_change = route_change
    page.update()

   

 
if __name__ == "__main__":
    ft.app(target=main) 
ft.app(target=main)