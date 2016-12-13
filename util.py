import os

def get_env_variable(var):
    try:
        return os.environ[var]
    except KeyError:
        print("Environment var '%s' not found." % var)
