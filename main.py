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
        timerr = 1
        if e.route == "/card":
            page.clean()
            page.add(ft.Text("Benifits of Meditation",color=ft.colors.INDIGO_800,size=30))
            page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("Meditation reduces stress and anxiety", color=ft.colors.BLACK87),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER_100,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Improved focus and concentration through meditation.", color=ft.colors.BLACK87),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.RED_200,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Better sleep quality with a regular meditation practice.", color=ft.colors.BLACK87),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.PURPLE_200,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Boosts creativity and problem-solving skills", color=ft.colors.BLACK87),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )
            page.add(ft.IconButton(ft.icons.ARROW_FORWARD_ROUNDED,on_click=lambda _:page.go("/name"),icon_color=ft.colors.INDIGO_200,width=100))
            page.update()
            

        elif e.route == "/name":
            page.clean()
            page.add(ft.Text("What do you love to be called today ?",color=ft.colors.INDIGO_800,size=30)) 
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
                page.add(ft.Text(x+"!! ,"+y,color=ft.colors.INDIGO_800,size=30))
                page.add(ft.Text("Start with a small amount like 3 minutes",color=ft.colors.INDIGO_400,size=15))
                page.add(ft.Text("Please select a time to proceed", color=ft.colors.INDIGO_200,size=10))
                def slider_changed(e):
                    nonlocal timerr
                    timerr = e.control.value 
                    page.update()
                    page.session.set("count", timerr)
                timer =  ft.Slider(width=300,min=1,max=20,divisions=20,label="{value}min",on_change=slider_changed)
                page.add(timer)
                page.update()
                page.add(ft.IconButton(ft.icons.ARROW_FORWARD_ROUNDED,on_click=lambda _:page.go("/music"),icon_color=ft.colors.INDIGO_200,width=100))
                page.update()

                
            page.add(ft.IconButton(ft.icons.ARROW_FORWARD_ROUNDED,on_click=button_clicked,icon_color=ft.colors.INDIGO_200,width=100))
            page.update() 

        elif e.route == "/music":
            page.clean()
            page.add(ft.Text("Which type of music needed ?",color=ft.colors.INDIGO_800,size=30))

            def button_clicked(e):
               
                ti = int(page.session.get('count'))
                
                minutes = ti * 60
                
                if dd.value == "Nature": 
                        page.clean()
                        def get_nature():
                            async def countdown(e):
                                audio1 = ft.Audio(
                                    src="nature.mp3", autoplay=True
                                )
                                page.overlay.append(audio1)
                                for i in range(minutes, 0, -1):  
                                    t.value = f"Time remaining: {i} seconds "  
                                    page.add(t)
                                    page.update()
                                    await asyncio.sleep(1)
                                  
                               
                                
                                audio1.release()
                                page.clean()
                                t.value = "Time's up!"
                                audio1.release()
                                page.add(t)
                                page.update() 

                    
                            countdown_loop = asyncio.new_event_loop()
                            asyncio.set_event_loop(countdown_loop)
                            asyncio.run(countdown(timerr))
                            page.add(ft.ElevatedButton(text="Restart",on_click=lambda _:page.go("/home")))

                        get_nature()

                        page.update()

                elif dd.value =="Rain":
                        page.clean()
                        def get_rain():
                            async def countdown(e):
                                audio2 = ft.Audio(
                                    src="rain.mp3", autoplay=True,
                                )
                                page.overlay.append(audio2)
                                for i in range(minutes, 0, -1):  
                                    t.value = f"Time remaining: {i} seconds "  
                                    page.add(t)
                                    page.update()
                                    await asyncio.sleep(1)
                                  
                               
                                audio2.release()
                                page.clean()
                                t.value = "Time's up!"
                                audio2.release()
                                page.add(t)
                                page.update() 

                    
                            countdown_loop = asyncio.new_event_loop()
                            asyncio.set_event_loop(countdown_loop)
                            asyncio.run(countdown(timerr))
                            page.add(ft.ElevatedButton(text="Restart",on_click=lambda _:page.go("/home")))
                            

                        get_rain()
                        page.update()
                        
                else:
                    def goto_meditate():
                        page.clean()
                        async def countdown(e):
                                for i in range(minutes, 0, -1):  
                                    t.value = f"Time remaining: {i} seconds "  
                                   

                                    page.add(t)
                                    page.update()
                                    await asyncio.sleep(1) 
                               
                                page.clean()
                                t.value = "Time's up!"
                                
                                page.add(t)
                                page.add(ft.ElevatedButton(text="Restart",on_click=lambda _:page.go("/home")))
                                page.update() 
                                
                    
                        countdown_loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(countdown_loop)
                        asyncio.run(countdown(timerr))

                    goto_meditate()
                    page.update()
                page.update()

            t = ft.Text(color=ft.colors.INDIGO_300,size=15)
            b = ft.ElevatedButton(text="Start", on_click=button_clicked)
            dd = ft.Dropdown(
                focused_color= ft.colors.INDIGO_300,   
               
            width=100,
            options=[
            ft.dropdown.Option("Nature"),
            ft.dropdown.Option("Rain"), 
            ft.dropdown.Option("None"),
            ],
            )
            page.add(dd, b,t)

          
            page.update()
        elif e.route=="/home":
                page.clean()
                page.add(ft.Text("MediFlet",color= ft.colors.INDIGO_500,size=50)) 
                page.add(ft.ElevatedButton("Start Again", on_click=lambda _: page.go("/card")))
                page.update()

 
 
    page.on_route_change = route_change
    page.update()

   

 
if __name__ == "__main__":
    ft.app(target=main) 