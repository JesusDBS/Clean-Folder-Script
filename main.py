import os
import glob
import json
import platform as p

def load_config_json(json_path:str="config.json") -> tuple:
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

    if check_if_windows():

        path[0] = fr'\{path[0]}'
    else:
        path[0] = f'/{path[0]}'
    
    return os.sep.join(path)

def main(json_path:str="config.json"):
    r"""
    Documentation here
    """
    assert isinstance(json_path, str), f'Path: {json_path} must be a string!'

    #Load folder path from config and fit it to os
    path_from_config, remove_folders_too = load_config_json(json_path=json_path)
    path = fix_path(path=path_from_config)

    if os.path.isdir(path):

        #Change current dir to dir to clean
        os.chdir(path)

        for filename in glob.glob('*'):
            filename = os.path.join(path, filename)
            
            try:
                if os.path.isfile(filename):
                    os.remove(filename)
                    continue
                
                if remove_folders_too and os.path.isdir(filename):
                    os.remove(filename)

            except:
                raise Exception("An error has occurred please check the files in your folder.")
            
        print(f'{path_from_config[-1]} has been cleaned!')
                
    else:
        raise Exception(f'You have to provide a valid directory path: {path}.')


if __name__ == "__main__":
    main()