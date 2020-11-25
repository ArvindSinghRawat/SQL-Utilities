"""
    Utilities to Create and Explore directories
"""
import os


def create_nested_directories(parent_path: str, dir_name_list: list) -> str:
    """Create a series of Nested directories inside the parent_path

    Args:
        parent_path (str): Directory where generated directories
        will be created
        dir_name_list (list): List of directorie names where each
        directory is created inside another

    Returns:
        str: Path to innermost created directory
    """
    copy = parent_path + ""
    for dir_name in dir_name_list:
        if not create_directory(copy, dir_name):
            break
        copy = os.path.join(copy, dir_name)
    return copy


def create_directory(
        parent_path: str, dir_name: str, verbosity: bool = False) -> bool:
    """Creates a "dir_name" directory in "parent_path" directory,
    suppresses  FileExistsError and,
    return True, if required directory is generated/exists,
    otherwise return False

    Args:
        parent_path (str): Path to Target Directory,
        where new directory is needed to be created
        dir_name (str): Name of new directory
        verbosity (bool, optional): Prints error if Found, Defaults to False.

    Returns:
        bool: Returns True, if desired directory is created/exists,
        otherwise False
    """
    try:
        os.mkdir(os.path.join(parent_path, dir_name), mode=0o771)
    except FileExistsError:
        pass
    except FileNotFoundError:
        if verbosity:
            print("Target directory does not exist")
        return False
    return True
