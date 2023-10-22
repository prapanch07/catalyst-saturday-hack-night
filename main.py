from ast import Lambda
import flet as ft
import asyncio


def main(page: ft.Page):
    
    page.title = "MediFlet"
    page.bgcolor=ft.colors.BLUE_50
    page.add(ft.Text("MediFlet",color= ft.colors.INDIGO_500,size=50)) 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.update()

    page.add(ft.ElevatedButton("Get Started", on_click=lambda _: page.go("/card")))

    def route_change(e: ft.RouteChangeEvent):
        timerr =0
        if e.route == "/card":
            page.clean()
            page.add(ft.Text("Meditation is good for health",color=ft.colors.INDIGO_800,size=30))
            page.add(ft.IconButton(ft.icons.ARROW_FORWARD_IOS_ROUNDED,on_click=lambda _:page.go("/name")))
            page.update()
            

        elif e.route == "/name":
            page.clean()
            page.add(ft.Text("what do you love to be called today ?",color=ft.colors.INDIGO_800,size=30)) 
            t = ft.Text()
            name = ft.TextField(label="Your name",text_size=18 ,color=ft.colors.INDIGO_800,width=350,border_color=ft.colors.BLACK12)
            page.add(name)
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            
            def button_clicked(e):
                nonlocal timerr
                t.value = name.value
                page.update()
                page.clean()
                tt = ft.Text("how much time do you want to meditate ?",color=ft.colors.INDIGO_800,size=30)
                x = t.value
                y = tt.value
                page.add(ft.Text(x+"!! ,"+y,color=ft.colors.INDIGO_800,size=20))
                page.add(ft.Text("Start with a small amount like 3 minutes",color=ft.colors.INDIGO_400,size=20))
                
                def slider_changed(e):
                    nonlocal timerr
                    timerr = f"{e.control.value}"
                    page.update()
                timer =  ft.Slider(width=300,value=0,min=0,max=20,divisions=10,label="{value}min",on_change=slider_changed)
                page.add(timer)
                page.add(ft.Text(timerr))
                page.update()
                page.add(ft.IconButton(ft.icons.ARROW_FORWARD_IOS_ROUNDED,on_click=lambda _:page.go("/music")))
                page.update()

               
            page.add(ft.IconButton(ft.icons.ARROW_FORWARD_IOS_ROUNDED,on_click=button_clicked))
            page.update()

        elif e.route == "/music":
            page.clean()
            page.add(ft.Text("Which type of music needed ?",color=ft.colors.INDIGO_800,size=30))

            def button_clicked(e):
                t.value = f"Selected : {dd.value}"
                if dd.value == "Nature":
                        page.clean()
                        def get_nature():
                            async def countdown(timerr):
                                for i in range(timerr, 0, -1):  
                                    t.value = f"Time remaining: {i} seconds"
                                    page.add(t)
                                    page.update()
                                    await asyncio.sleep(1)
                        
                                t.value = "Time's up!"
                                page.add(t)
                                page.update()

                   
                            countdown_loop = asyncio.new_event_loop()
                            asyncio.set_event_loop(countdown_loop)
                            asyncio.run(countdown(timerr))

                        get_nature()
                        page.update()

                elif dd =="Rain":
                        def get_rain():
                            pass
                        get_rain()
                else:
                    def goto_meditate():
                        pass
                    goto_meditate()
                page.update()

            t = ft.Text(color=ft.colors.INDIGO_300,size=15)
            b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
            dd = ft.Dropdown(
            width=100,
            options=[
            ft.dropdown.Option("Nature"),
            ft.dropdown.Option("Rain"),
            ft.dropdown.Option("None"),
            ],
            )
            page.add(dd, b,t)

          
            page.update()

 
 
    page.on_route_change = route_change
    page.update()

   

 
if __name__ == "__main__":
    ft.app(target=main) 