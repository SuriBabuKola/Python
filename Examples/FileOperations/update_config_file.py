def update_config_list(filepath, key, value):
    with open(filepath, "r") as file:
        file_lines = file.readlines()
    with open(filepath, "w") as file:
        for line in file_lines:
            if key in line:
                file.write(key + " = " + value + "\n")
            else:
                file.write(line)

update_config_list("server.conf", "MAX_CONNECTIONS", "1000")