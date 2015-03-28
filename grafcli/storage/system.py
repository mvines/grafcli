import os
import json

from grafcli.exceptions import DocumentNotFound


def to_file_format(filename):
    return "{}.json".format(filename)


def from_file_format(filename):
    return filename.replace('.json', '')


def list_files(path, *paths):
    full_path = os.path.join(path, *paths)
    if not os.path.isdir(full_path):
        raise DocumentNotFound("No documents found")

    return [from_file_format(file)
            for file in os.listdir(full_path)]


def read_file(directory, name):
    full_path = os.path.join(directory, to_file_format(name))
    if not os.path.isfile(full_path):
        raise DocumentNotFound("File not found: {}".format(full_path))

    with open(full_path, 'r') as f:
        return json.loads(f.read())


def write_file(directory, name, data):
    full_path = os.path.join(directory, to_file_format(name))

    with open(full_path, 'w') as f:
        f.write(json.dumps(data))


def remove_file(directory, name):
    full_path = os.path.join(directory, to_file_format(name))
    if not os.path.isfile(full_path):
        raise DocumentNotFound("File not found: {}".format(full_path))

    os.unlink(full_path)


def makepath(path):
    os.makedirs(path, mode=0o755, exist_ok=True)