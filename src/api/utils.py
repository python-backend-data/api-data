"""
Funciones con utilidades generales
"""

import json
import yaml  # type: ignore


def read_json(file_path):
    """
    funcion que lee un archivo en formato json
    """
    data = None
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[read_json] error {e}")
    return data


def read_yml(file_path):
    """
    funcion que lee un archivo en formato yml
    """
    with open(file_path, 'r') as f:
        data = yaml.full_load(f)

    return data
