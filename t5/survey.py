# code for importing and translating ISS Second Survey data
# example:
#   http://travellermap.com/SEC.aspx?sector=Spinward%20Marches
import csv
import os
import re

from t5 import system

def parse_txt_sector(text_stream):
    """Parses data from the original column formatted sector survey data """
    for line in text_stream:
        if line.startswith('#'):
            pass
        if len(line) > 80:
            name = line[0:25].strip()
            hex = line[26:30].strip()
            uwp = line[31:40].strip()
            base = line[41]
            remarks = line[43:68].strip()
            zone = line[69]
            pbg = line[71:74]
            allegiance = line[75:77].strip()
            stellar = line[78:98].strip()

def parse_tab_sector_row(row_data, sector):
    """Parses row data from T5 second survey data format into relevant objects
    and strings.
    """
    # valid length?
    if len(row_data) == 17:
        hexcode_match = re.match(system.HEXCODE_REGEX, row_data[2])
        if hexcode_match:
            this_system = system.SolarSystem(
                    sector=sector,
                    name = row_data[3],
                    hex_x = hexcode_match.group(1),
                    hex_y = hexcode_match.group(2),
                    world = system.World(row_data[4]),
                    bases = row_data[5],
                    tradecodes = parse_tradecodes(row_data[6]),
                    zone = row_data[7],
                    pbg = row_data[8],
                    allegiance = row_data[9],
                    stellar = row_data[10],
                    importance = row_data[11],
                    economic = row_data[12],
                    cultural = row_data[13],
                    nobles = row_data[14],
                    worlds = row_data[15],
                    ru = row_data[16])
            print world

LOCAL_PATH = 'static/sectors'

def spinwardmarches():
    local_file = os.path.join(os.path.dirname(__file__),
                              LOCAL_PATH,
                              'spinwardmarches.tab')
    secreader = csv.reader(open(local_file, 'rb'), delimiter='\t')
    for row in secreader:
        parse_tab_sector_row(row, 'Spin')


if __name__ == '__main__':
    spinwardmarches()
