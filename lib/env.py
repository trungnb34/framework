def env(key):
    f = open(".env", "r")
    data = f.read()
    lines = data.split()
    for line in lines:
        item = line.split('=')
        if item[0] == key:
            return item[1]
    return None