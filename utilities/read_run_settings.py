import configparser
import os
import cryptocode

from CONSTS import ROOT_DIR

abs_path = os.path.abspath(fr"{ROOT_DIR}/configurations/run_settings.ini")
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_application_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_user_email():
        return config.get('app_info', 'user_name')

    @staticmethod
    def get_password():
        decoded = cryptocode.decrypt(config.get('app_info', 'password'), "mypassword")
        return decoded

    @staticmethod
    def get_browser():
        return int(config.get('browser', 'browser_id'))

    @staticmethod
    def get_browser_mod():
        if config.get('browser', 'headless') in ['False', 0, 'false']:
            return False
        else:
            return True

    @staticmethod
    def get_logging_level():
        return config.get('logging_level', 'logging_level')

    @staticmethod
    def get_api_base_url():
        return config.get('api_data', 'base_url')

    @staticmethod
    def get_souse_labs_configuration():
        return dict(config.items('souse_labs'))
