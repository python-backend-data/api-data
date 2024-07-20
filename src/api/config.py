"""
Configuraciones
"""
import os
from api.utils import read_yml
from typing import Dict, Any


class Config():
    configuracion: Dict[str, Any] = {}

    def __init__(self) -> None:
        self.path_configuracion = os.environ['API_CONFIG_PATH']
        self.get_configuration()

    def get_configuration(self):
        """
        funcion que lee el archivo de configuracion
        """
        try:
            self.configuracion = read_yml(self.path_configuracion)
        except Exception as e:
            print(f"[get_configuration] error {e}")
