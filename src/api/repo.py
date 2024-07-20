"""
funciones encardas de administrar la capa de datos
"""
from api.utils import read_json

from typing import Dict, List, Any


class Repo():
    datos: Dict[str, Any] = {}
    lista_items: List[str] = []

    def __init__(self, path) -> None:
        self.path = path
        self.leer_datos()
        self.generar_lista_items()

    def leer_datos(self):
        """
        Funcion que lee el json para generar un
        listado de los identificadores
        """
        try:
            self.datos = read_json(self.path)
            print(f"lectura del archivo de configuracion{self.datos}")
        except Exception as e:
            print(f"[leer_datos] error {e}")

    def generar_lista_items(self):
        """
        Funcion que lee la variable datos y crea un listado
        con los items
        """
        try:
            self.lista_items = list(self.datos.keys())
        except Exception as e:
            print(f"[generar_lista_items] error {e}")
