import re

WORLD_REGEX = (r'^([0-9A-HYX])'  # starport
               '([0-9A-F])'      # size
               '([0-9A-F])'      # atmo
               '([0-9A-F])'      # hydro
               '([0-9A-F])'      # pop
               '([0-9A-F])'      # gov
               '([0-9A-J])'      # law
               '-([0-9A-R])$')   # TL

STARPORT_DETAIL = {'A': 'Excellent starport',
                   'B': 'Good starport',
                   'C': 'Routine starport',
                   'D': 'Poor starport',
                   'E': 'Frontier starport',
                   'F': 'Good spaceport',
                   'G': 'Poor spaceport',
                   'H': 'Basic spaceport',
                   'X': 'No starport',
                   'Y': 'No spaceport'}

SIZE_DETAIL = {'0': 'Asteroid belt',
               '1': '1,600km',
               '2': '3,200km',
               '3': '4,800km',
               '4': '6,400km',
               '5': '8,000km',
               '6': '9,600km',
               '7': '12,200km',
               '8': '13,800km',
               '9': '14,400km',
               'A': '16,000km',
               'B': '17,600km',
               'C': '19,200km',
               'D': '20,800km',
               'E': '22,400km',
               'F': '24,000km'}

ATMO_DETAIL = {'0': 'Vacuum',
               '1': 'Trace',
               '2': 'Very Thin, Tainted',
               '3': 'Very Thin',
               '4': 'Thin, Tainted',
               '5': 'Thin',
               '6': 'Standard',
               '7': 'Standard, Tainted',
               '8': 'Dense',
               '9': 'Dense, Tainted',
               'A': 'Exotic',
               'B': 'Corrosive',
               'C': 'Insidious',
               'D': 'Dense High',
               'E': 'Ellipsoid',
               'F': 'Thin Low'}

HYDRO_DETAIL = {'0': 'Desert World',
                '1': '10% water',
                '2': '20% water',
                '3': '30% water',
                '4': '40% water',
                '5': '50% water',
                '6': '60% water',
                '7': '70% water',
                '8': '80% water',
                '9': '90% water',
                'A': 'Water World'}


class World(object):

    @classmethod
    def generate():
        pass

    def __init__(self, uwp=None):
        # UWP should be a string in the format of X000000-0
        if uwp is None:
            self.starport = None
            self.size = None
            self.atmosphere = None
            self.hydrographics = None
            self.population = None
            self.government = None
            self.lawlevel = None
            self.techlevel = None
            self.tradecodes = []
        uwpmatch = re.match(WORLD_REGEX, uwp.upper())
        if uwpmatch:
            self.starport = uwpmatch.group(1)
            self.size = uwpmatch.group(2)
            self.atmosphere = uwpmatch.group(3)
            self.hydrographics = uwpmatch.group(4)
            self.population = uwpmatch.group(5)
            self.government = uwpmatch.group(6)
            self.lawlevel = uwpmatch.group(7)
            self.techlevel = uwpmatch.group(8)
        else:
            raise ValueError('Unable to parse UWP: %s' % uwp)

    def starport_txt(self):
        return STARPORT_DETAIL[self.starport]

    def size_txt(self):
        return SIZE_DETAIL.get(self.starport)

    def atmosphere_text(self):
        return ATMO_DETAIL.get(self.atmosphere)

    def hydrographics_text(self):
        return HYDRO_DETAIL.get(self.hydrographics)
