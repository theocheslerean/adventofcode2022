


def get_file_contents(filename: str) -> dict:
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    return "".join(lines)
