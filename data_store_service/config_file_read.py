from configparser import ConfigParser

parser = ConfigParser()
parser.read('dev.ini')

print(parser.sections())
print(parser.get('MONGO_CREDS','username'))