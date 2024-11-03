#Mention what command line can be used to load data into Django?


# In Django, you can use the loaddata command to load data from a fixture (a file that contains serialized data) into your database.
# The command is executed from the command line within your Django project directory.

# Here’s the basic syntax:

# python manage.py loaddata <fixture_name>


# Where <fixture_name> is the name of the fixture file you want to load. 
# The fixture file should be in one of the formats supported by Django
# (such as JSON, XML, or YAML) and typically located in your app's fixtures directory or in the project root.