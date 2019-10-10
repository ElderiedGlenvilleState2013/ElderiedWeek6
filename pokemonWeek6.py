import sys
import logging
import time

import logstash

#logging.basicConfig(filename='python-application-log.log', level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s')
test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.setLevel(logging.WARNING)
test_logger.addHandler(logstash.LogstashHandler('54.91.193.4', 5959, version=1))

class Pokemon:
    def __init__(self, powerType, health):
        self.powerType = powerType
        self.health = health



class ElectricPokemon(Pokemon):
    def __init__(self, name):
         self.name = name
         self.attack = self.thunderBolt()
         self.health = 100
         self.powerType = 'Thunder'



    def thunderBolt(self):
        return "Thunder Bolt"


class FirePokemon(Pokemon):
    def __init__(self, name,):
        self.powerType = "Fire"
        self.name = name
        self.attack = self.fireSpin()
        self.health = self.health()



    def fireSpin(self):
        return "Fire Spin"

    def health(self):

        return 100



pikachu = ElectricPokemon("Pikachu")
charmander = FirePokemon('Charmander')

test_logger.info("{} I choose you".format(pikachu.name))

test_logger.warning("{0} use {1} attack ".format(pikachu.name, pikachu.attack))


test_logger.info("{} I choose you".format(charmander.name))

test_logger.info("{0} use {1} attack ".format(charmander.name, charmander.attack, charmander.health))
test_logger.debug("{0} health is {1}%".format(pikachu.name, pikachu.health))

extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 126,
    'test_list': [1,2,3],
    'pokemon_name': '{}'.format(pikachu.name),
    'pikachu_power_type': '{}'.format(pikachu.powerType),

}
test_logger.info('python-logstash: test extra fields', extra=extra)
