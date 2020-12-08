from configparser import ConfigParser

parser = ConfigParser()
parser.read(r'C:\Users\preston.turner\Desktop\base_station\data_store_service\dev.ini')

print(parser.sections())
print(parser.get('MONGO','username'))