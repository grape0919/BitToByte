import yaml

class Config(dict):
    CONF_PATH = './conf/config.yaml'
    API_KEY = 'ADMIN_ID'
    SECRET_KEY = 'ADMIN_PASSWD'

    def load(self):
        print("config load")
        with open(self.CONF_PATH) as f:
            temp = yaml.load(f, Loader=yaml.FullLoader)
            self.update(temp)
            f.close()

    def save(self):
        print("Config save")
        with open(self.CONF_PATH, 'w', encoding='utf8') as f:
            self.update({
                self.API_KEY:self[self.API_KEY]
                ,self.SECRET_KEY:self[self.SECRET_KEY]
            })
            print('new config : ' + str(self.copy()))
            yaml.dump(self.copy(), f)
            f.close()

    def init_conf(self):
        print("Config initalize")
        self.save()

if __name__ == '__main__':
    conf = Config()
    # conf.init_conf()
    conf.load()
    print(conf)

    print(conf[conf.API_KEY])
