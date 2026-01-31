def add_setting(settings, keyvalue):
    key, value = keyvalue
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, keyvalue):
    key,value = keyvalue
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"

def view_settings(settings):
    if len(settings) == 0:
        return 'No settings available.'
    
    return "Current User Settings:\n" + "\n".join(f"{key.capitalize()}: {value}" for key,value in settings.items()) + "\n"

test_settings = {
    'theme':'dark',
    'language':'spanish',
}

keyvalue = ('Notifications','Off')

print(view_settings(test_settings))