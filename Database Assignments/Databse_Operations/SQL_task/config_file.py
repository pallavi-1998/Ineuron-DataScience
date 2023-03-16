# importing config parser
from configparser import ConfigParser

# creating object of configparser
config = ConfigParser()

# creating a section
config.add_section("mysql")

# adding key-value pairs
config.set("mysql", "host", "localhost")
config.set("mysql", "user", "root")
config.set("mysql", "password", "mysql")

with open("config.ini","w") as f:
    config.write(f)