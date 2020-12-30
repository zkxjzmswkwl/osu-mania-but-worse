import configparser


class Settings:

    def __init__(self, path):
        self._path = path

        self.config = configparser.ConfigParser()
        self.config.read(path)
        self.keys = ('64', '192', '320', '448')

        if 'THEME' not in self.config:
            print('No \'THEME\' section found in settings.ini!')
            print('Writing default theme..')
            self.write_default_theme()

    def write(self):
        with open(self._path, 'w') as conf_file:
            self.config.write(conf_file)

    def read(self, section, key):
        return self.config[section][key]

    def write_default_theme(self):
        self.config['THEME'] = {
            '64_R': 255, '64_G': 0, '64_B': 0,
            '192_R': 0, '192_G': 255, '192_B': 0,
            '320_R': 0, '320_G': 0, '320_B': 255,
            '448_R': 255, '448_G': 0, '448_B': 255}
        self.write()

    def get_theme(self):
        keys_rgb = {}
        for key in self.keys:
            tmp = (
                int(self.read('THEME', f'{key}_r')),
                int(self.read('THEME', f'{key}_g')),
                int(self.read('THEME', f'{key}_b'))
            )
            keys_rgb[key] = tmp
        return keys_rgb

