import yaml


class ConfigReader:

    @staticmethod
    def load():

        with open("config/config.yaml") as file:
            return yaml.safe_load(file)