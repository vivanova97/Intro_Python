from pathlib import Path

__all__ = ['rename_files']

def rename_files(slice: tuple[int], serial_num: int, name: str = ''):
    """
    Renames all files in current working directory.  Takes a slice of the current file 
    name, concatenates it with a name provided by the 'name' function argument if 
    any is provided.  
    Adds an serial num based on the length of serial number chosen for the argument 'serial_num'.
    
    Example: 
    If mypyfile.py is the first file and the arguments provided for rename_files are:
    rename_files(slice=(2,5), serial_num=4, name='python')
    The resulting file name will be: pyfpython1000.py
    """
    serial_num = int('1'+'0'*(serial_num-1))
    p = Path(Path().cwd())
    for obj in p.iterdir():
        if obj.is_file():
            Path(obj.name).rename(f'{obj.name[slice[0]:slice[1]]}{name}{serial_num}{obj.suffix}' )
            serial_num+=1
