def format_username(name):
    username = name.strip().lower().title().replace(" ", "-")
    return username

name = " aNnA kaRlSsOn "

print(format_username(name))