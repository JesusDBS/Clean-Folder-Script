import os
import glob
import platform as p
import shutil

from utils.utils import load_config_json, fix_path

#main program
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
                    print(f'....{filename} has been deleted....', '\n')
                    continue
                
                if remove_folders_too and os.path.isdir(filename):
                    shutil.rmtree(filename)
                    print(f'....{filename} has been deleted....', '\n')

            except:
                raise Exception("An error has occurred please check the files in your folder.")
            
        print(f'{path_from_config[-1]} has been cleaned!')
                
    else:
        raise Exception(f'You have to provide a valid directory path: {path}.')


if __name__ == "__main__":
    main()