
import logging

logging.basicConfig(filename='pokemon.log', level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s')


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

logging.debug("{} I choose you".format(pikachu.name))

logging.debug("{0} use {1} attack ".format(pikachu.name, pikachu.attack))


logging.debug("{} I choose you".format(charmander.name))

logging.debug("{0} use {1} attack ".format(charmander.name, charmander.attack))


