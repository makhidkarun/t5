# code for importing and translating ISS Second Survey data
# example:
#   http://travellermap.com/SEC.aspx?sector=Spinward%20Marches

def parse_sector(text_stream):
    pass
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




if __name__ == '__main__':
    sm = open('spinwardmarches.sec')
    results = parse_sector(sm)
    print results
