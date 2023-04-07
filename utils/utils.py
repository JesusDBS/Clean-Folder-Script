import json
import platform as p
import os

def load_config_json(json_path:str) -> tuple:
    r"""
    Documentation here
    """
    assert isinstance(json_path, str), f'Jason path: {json_path} must be a string!'

    try:

        with open(json_path, "r") as j:
            config_json = json.load(j)
        
        path = config_json["dir_path"]
        remove_folders_too = config_json["remove_folders_too"]

        return path, remove_folders_too

    except:

        raise FileNotFoundError("Json file not found")
    
def check_if_windows():
    r"""
    Documentation here
    """
    if p.system() == "Windows":
        return True
    
    return False

def fix_path(path:list) -> str:
    r"""
    Documentation here
    """
    assert isinstance(path, list), f"Path {path} must be a list"

    if path:

        if check_if_all_elements_are_strings(path=path):
            
            if check_if_windows():

                path[0] = fr'\{path[0]}'
            else:
                path[0] = f'/{path[0]}'
            
            return os.sep.join(path)
        
        
        raise ValueError(f"All elements in path: {path} must be strings")
    
    raise ValueError("Path can't be an empty list")


def check_if_all_elements_are_strings(path:list) -> bool:
    r"""
    Documentation here
    """
    assert isinstance(path, list), f'Path: {path} must be a string'

    return all(isinstance(el, str) for el in path)