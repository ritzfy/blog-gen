import configparser

config = configparser.ConfigParser()
config.read('config.ini')

config_dict = {}

for section in config.sections():
    # Adding a new sub-dictionary for each section
    config_dict[section] = {}
    
    # Looping through each option in the section
    for option in config.options(section):
        # Add the option and its value to the section's dictionary
        config_dict[section][option] = config.get(section, option)
