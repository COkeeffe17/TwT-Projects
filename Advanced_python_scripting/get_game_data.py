import os
import json
import shutil
from subprocess import PIPE, run
import sys


GAME_DIR_PATTERN = "game"
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]


def find_all_game_paths(source):
    game_paths = []

    # Walk gives the roots, directories, and files in the directory you give it
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            # If it has game in the name
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_paths.append(path)

        # Break because we only need to do this one time, top layer
        break

    return game_paths


def get_name_from_paths(paths, to_strip):
    new_names = []
    for path in paths:
        # Gives just the last part of the path
        _, dir_name = os.path.split(path)
        # Removes "game"
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)

    return new_names


def create_dir(path):
    # Creates target directory if it doesn't exists already
    if not os.path.exists(path):
        os.mkdir(path)


def copy_and_overwrite(source, destination):
    # Recursive copy
    if os.path.exists(destination):
        # Recursive delete
        shutil.rmtree(destination)

    shutil.copytree(source, destination)


def make_json_file(path, game_dirs):
    data = {
        "GameNames": game_dirs,
        "NumberOfGames": len(game_dirs)
    }

    # Just dumps the data into the json file
    with open(path, "w") as f:
        json.dump(data, f)


def compile_game_code(path):
    # Only works if theres only one .go file in the directory
    code_file_name = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break

        # Only do once
        break

    if code_file_name == None:
        return 
    
    # Compiles any .go files
    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command, path)


def run_command(command, path):
    cwd = os.getcwd()

    # Changes directory from dir with the python file in it to the "games" dir
    os.chdir(path)

    run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)

    # Change the directory back
    os.chdir(cwd)


def main(source, target):
    # Full path to target directory
    # Dont use concantenation, as wont work on all operating systems
    # cwd = current working directory
    cwd = os.getcwd()

    # Path to the directory containing all the files
    source_path = os.path.join(cwd, source)
    # Path to the target directory, in this case the "games" directory
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    
    new_game_dirs = get_name_from_paths(game_paths, GAME_DIR_PATTERN)

    create_dir(target_path)
    
    # For each set of (complete path to target directory, new name with game removed)
    for src, dest in zip(game_paths, new_game_dirs):
        # Full path to the destination
        dest_path = os.path.join(target_path, dest)
        # Copies the file at said path and overwrites it in the target directory
        copy_and_overwrite(src, dest_path)
        # Compiles any .go files
        compile_game_code(dest_path)

    # Just makes the path to the new json file
    json_path = os.path.join(target_path, "metadata.json")

    make_json_file(json_path, new_game_dirs) 


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and target directory only.")

    # Strips off the name of the python file
    source, target = args[1:]

    main(source, target)

