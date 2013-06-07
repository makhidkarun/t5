import re

HEXCODE_REGEX = (r'^(\d\d)(\d\d)$')

WORLD_REGEX = (r'^([0-9A-HYX])'  # starport
               '([0-9A-F])'      # size
               '([0-9A-F])'      # atmo
               '([0-9A-F])'      # hydro
               '([0-9A-F])'      # pop
               '([0-9A-F])'      # gov
               '([0-9A-J])'      # law
               '-([0-9A-R])$')   # TL

STARPORT_DETAIL = {'A': 'Excellent starport', 'B': 'Good starport',
                   'C': 'Routine starport',   'D': 'Poor starport',
                   'E': 'Frontier starport',  'F': 'Good spaceport',
                   'G': 'Poor spaceport',     'H': 'Basic spaceport',
                   'X': 'No starport',        'Y': 'No spaceport'}

SIZE_DETAIL = {'0': 'Asteroid belt', '1': '1,600km',
               '2': '3,200km',       '3': '4,800km',
               '4': '6,400km',       '5': '8,000km',
               '6': '9,600km',       '7': '12,200km',
               '8': '13,800km',      '9': '14,400km',
               'A': '16,000km',      'B': '17,600km',
               'C': '19,200km',      'D': '20,800km',
               'E': '22,400km',      'F': '24,000km'}

ATMO_DETAIL = {'0': 'Vacuum',             '1': 'Trace',
               '2': 'Very Thin, Tainted', '3': 'Very Thin',
               '4': 'Thin, Tainted',      '5': 'Thin',
               '6': 'Standard',           '7': 'Standard, Tainted',
               '8': 'Dense',              '9': 'Dense, Tainted',
               'A': 'Exotic',             'B': 'Corrosive',
               'C': 'Insidious',          'D': 'Dense High',
               'E': 'Ellipsoid',          'F': 'Thin Low'}

HYDRO_DETAIL = {'0': 'Desert World', '1': '10% water',
                '2': '20% water',    '3': '30% water',
                '4': '40% water',    '5': '50% water',
                '6': '60% water',    '7': '70% water',
                '8': '80% water',    '9': '90% water',
                'A': 'Water World'}

POP_DETAIL = {'0': 'unpopulated',       '1': 'tens',
              '2': 'hundreds',          '3': 'thousands',
              '4': 'ten thousands',     '5': 'hundred thousands',
              '6': 'millions',          '7': 'ten millions',
              '8': 'hundred millions',  '9': 'billions',
              'A': 'ten billions',      'B': 'hundred billions',
              'C': 'trillions',         'D': 'ten trillions',
              'E': 'hundred trillions', 'F': 'quadrillions'}

GOV_DETAIL = {'0': 'No government structure. Family bonds predominate.',
              '1': 'Company/Corporation. Rule by managerial elite.',
              '2': 'Participating democracy. Rule by popular vote.',
              '3': 'Self-perpetuating rOigarchy. Rule by a restricted minority'
                   ' with little or no input from the masses',
              '4': 'Representative Democracy. Government by proxy.',
              '5': 'Feudal Technocracy. Governmental relationships based on'
                   ' mutally beneficial technical activities.',
              '6': 'Captive/Colony. Rule by a leadership answerable to an'
                   ' outside group.',
              '7': 'Balkanization. Rival governments continually compete for'
                   ' control of the world.',
              '8': 'Civil Service Bureaucracy. Rule by agencies employing'
                   ' individuals selected by merit',
              '9': 'Impersonal Bureaucracy. Impersonal agencies rule.',
              }

LAW_DETAIL = {'0': 'No Law. No prohibitions.',
              '1': 'Low Law. Prohibition of WMD, Psi weapons.',
              '2': 'Low Law. Prohibition of "Portable" weapons.',
              '3': 'Low Law. Prohibition of Acid, Fire, Gas weapons.',
              '4': 'Moderate Law. Prohibition of Laser, Beam weapons.',
              '5': 'Moderate Law. Prohibition of Shock, EMP, Rad, Mag, Grav'
                   ' weapons.',
              '6': 'Moderate Law. Prohibition of machineguns.',
              '7': 'Moderate Law. Prohibition of pistols.',
              '8': 'High Law. Open display of weapons prohibited.',
              '9': 'High Law. Weapons outside the home prohibited.',
              'A': 'Extreme Law. Weapon possession prohibited.',
              'B': 'Extreme Law. Continental passports required.',
              'C': 'Extreme Law. Unrestricted invasion of privacy.',
              'D': 'Extreme Law. Paramilitary law enforcement.',
              'E': 'Extreme Law. Full-fledged police state.',
              'F': 'Extreme Law. Daily life rigidly controlled.',
              'G': 'Extreme Law. Disproportionate punishments.',
              'H': 'Extreme Law. Legalized oppressive practices.',
              'J': 'Extreme Law. Routinely oppressive and restrictive.'}


class World(object):

    @classmethod
    def generate():
        pass

    def __init__(self, uwp):
        # UWP should be a string in the format of X000000-0
        if uwp is None:
            raise ValueError('UWP was None')
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
            self.mainworld = True  # is this the mainworld
        else:
            raise ValueError('Unable to parse UWP: %s' % uwp)

    def _generate_trade_classifications(self):
        self.tc = []

    # properties to validate trade classifications. All codes are expected to
    # be in 'upper case' and string values

    @property
    def As(self):
        return ((self.size == '0' and
                 self.atmosphere == '0' and
                 self.hydrographics == '0'), 'Asteroid belt')

    @property
    def De(self):
        return ((self.hydrographics == '0' and
                 self.atmosphere in '23456789'), 'Desert')

    @property
    def Fl(self):
        return ((self.atmosphere in 'ABC' and
                 self.hydrographics in '123456789A'), 'Fluid')

    @property
    def Ga(self):
        return ((self.size in '678' and
                 self.atmosphere in '568' and
                 self.hydrographics in '567'), 'Garden World')

    @property
    def He(self):
        return ((self.size in '3459ABC' and
                 self.atmosphere in '2479ABC' and
                 self.hydrographics in '012'), 'Hellworld')

    @property
    def Ic(self):
        return ((self.atmosphere in '01' and
                 self.hydrographics in '123456789A'), 'Ice-capped')

    @property
    def Oc(self):
        return ((self.size in 'ABC' and
                 self.hydrographics == 'A'), 'Ocean world')

    @property
    def Va(self):
        return ((self.atmosphere == '0'), 'Vacuum')

    @property
    def Wa(self):
        return ((self.size in '3456789A' and
                 self.atmosphere in '3456789' and
                 self.hydrographics == 'A'), 'Water world')

    # ---------------------------------------------------------------------

    @property
    def Di(self):
        return ((self.population == '0' and
                 self.government == '0' and
                 self.lawlevel == '0' and
                 self.techlevel != '0'), 'Dieback (000-%s)' % self.techlevel)

    @property
    def Ba(self):
        return ((self.population == '0' and
                 self.government == '0' and
                 self.lawlevel == '0' and
                 self.techlevel == '0'), 'Barren')

    @property
    def Lo(self):
        return ((self.population in '123'), 'Low population')

    @property
    def Ni(self):
        return ((self.population in '456'), 'Non-industrial')

    @property
    def Ph(self):
        return ((self.population == '8'), 'Pre-high population')

    @property
    def Hi(self):
        return ((self.population in '9ABCDEF'), 'High population')

    # ---------------------------------------------------------------------

    @property
    def Pa(self):
        return ((self.atmosphere in '456789' and
                 self.hydrographics in '45678' and
                 self.population in '48'), 'Pre-agricultural')

    @property
    def Ag(self):
        return ((self.atmosphere in '456789' and
                 self.hydrographics in '45678' and
                 self.population in '567'), 'Agricultural')

    @property
    def Na(self):
        return ((self.atmosphere in '0123' and
                 self.hydrographics in '0123' and
                 self.population in '6789ABCDEF'), 'Non-agricultural')

    @property
    def Pi(self):
        return ((self.atmosphere in '012479' and
                 self.population in '78'), 'Pre-Industrial')

    @property
    def In(self):
        return ((self.atmosphere in '0123479ABC' and
                 self.population in '9ABCDEF'), 'Industrial')

    @property
    def Po(self):
        return ((self.atmosphere in '2345' and
                 self.hydrographics in '0123'), 'Poor')

    @property
    def Pr(self):
        return ((self.atmosphere in '68' and
                 self.population in '59'), 'Pre-rich')

    @property
    def Ri(self):
        return ((self.atmosphere in '68' and
                 self.population in '678'), 'Rich')

    # ---------------------------------------------------------------------

    @property
    def Fa(self):
        return ((self.atmosphere in '456789' and
                 self.hydrographics in '45678' and
                 self.population in '23456' and
                 not self.mainworld and
                 self.hz), 'Farming')

    @property
    def Mi(self):
        return ((self.population in '23456' and
                 not self.mainworld and
                 not self.hz  # and mainworld is In
                 ), 'Mining')

    @property
    def Px(self):
        return ((self.atmosphere in '23AB' and
                 self.hydrographics in '12345' and
                 self.population in '3456' and
                 self.government != '6' and
                 self.lawlevel in '6789'), 'Prison, Exile camp')

    @property
    def Pe(self):
        return ((self.atmosphere in '23AB' and
                 self.hydrographics in '12345' and
                 self.population in '3456' and
                 self.government == '6' and
                 self.lawlevel in '6789'), 'Penal Colony')

    @property
    def Re(self):
        return ((self.population in '1234' and
                 self.government == '6' and
                 self.lawlevel in '45'), 'Reserve')

    @property
    def Cy(self):
        return ((self.population in '56789A' and
                 self.government == '6' and
                 self.lawlevel in '0123'), 'Colony')

    # ---------------------------------------------------------------------

    def starport_txt(self):
        return STARPORT_DETAIL[self.starport]

    def size_txt(self):
        return SIZE_DETAIL.get(self.starport)

    def atmosphere_text(self):
        return ATMO_DETAIL.get(self.atmosphere)

    def hydrographics_text(self):
        return HYDRO_DETAIL.get(self.hydrographics)

    def population_text(self):
        return POP_DETAIL.get(self.population)

    def government_text(self):
        return GOV_DETAIL.get(self.government)

    def law_text(self):
        return LAW_DETAIL.get(self.lawlevel)
