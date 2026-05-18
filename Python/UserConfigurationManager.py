test_settings = {
    'theme': 'dark'
}

def add_setting(dict_settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    print(key, value)
    if key in dict_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dict_settings.update({key: value})
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dict_settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in dict_settings:
        dict_settings.update({key: value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dict_setting, key):
    key = key.lower()
    if key in dict_setting:
        dict_setting.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(dict_settings):
    if not dict_settings:
        return "No settings available."
    else:
        msg = "Current User Settings:"
        for key, value in dict_settings.items():
            msg += f"\n{key.capitalize()}: {value}"
        msg += '\n'
        return msg

print(add_setting({'Theme': 'light'}, ('THEME', 'dark')))
print(add_setting({'theme': 'light'}, ('volume', 'high')))

print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))
