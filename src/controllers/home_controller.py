# Controladores para la página principal
from src.views.home_views import (
    contacto_page, home_page, noticias_page,
    servicios_page)

def init_routes(rt):
    HomeControler(rt)


class HomeControler:
    
    def __init__(self, rt):
        self.rt = rt
        self.init_routes()
    
    def init_routes(self):
        self.rt("/")(self.home)
        self.rt("/home")(self.home)
        self.rt("/servicios")(self.servicios)
        self.rt("/noticias")(self.noticias)
        self.rt("/contacto")(self.contacto)

    def home(self, session, request):
        return home_page(session=session, request=request)
    
    def servicios(self, session, request):
        return servicios_page(session=session, request=request)
    
    def noticias(self, session, request):
        return noticias_page(session=session, request=request)
    
    def contacto(self, session, request):
        return contacto_page(session=session, request=request)