"""
mod_wsgi gateway wsgi file
"""

from rest_VariantValidator.app import application as application
if __name__ == '__main__':
    from configparser import ConfigParser
    from VariantValidator.settings import CONFIG_DIR
    config = ConfigParser()
    config.read(CONFIG_DIR)
    if config["logging"]["log"] == "True":
        application.debug = True
        application.config['PROPAGATE_EXCEPTIONS'] = True
    else:
        application.debug = False
        application.config['PROPAGATE_EXCEPTIONS'] = False
    application.run(host="127.0.0.1", port=8080)
