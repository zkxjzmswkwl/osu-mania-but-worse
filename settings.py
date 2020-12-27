import configparser


class Settings:

    def __init__(self, path):
        self._path = path

        self.config = configparser.ConfigParser()
        self.config.read(path)
        self.keys = ('d', 'f', 'j', 'k')

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
            'D_R': 255, 'D_G': 0, 'D_B': 0,
            'F_R': 0, 'F_G': 255, 'F_B': 0,
            'J_R': 0, 'J_G': 0, 'J_B': 255,
            'K_R': 255, 'K_G': 0, 'K_B': 255}
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

