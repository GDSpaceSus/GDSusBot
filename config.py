import ast

def cmdsplit(text):
    parts = text.split(',')
    stripped_parts = [part.strip() for part in parts]
    return stripped_parts

def read_list_from_file(filename="idlist.txt"):
    with open(filename, 'r') as f:
        content = f.read()
        list_definition = content.split("=")[1].strip()
        return ast.literal_eval(list_definition)

def write_list_to_file(data, filename="idlist.txt"):
    with open(filename, 'w') as f:
        f.write(f"ids = {data}")
