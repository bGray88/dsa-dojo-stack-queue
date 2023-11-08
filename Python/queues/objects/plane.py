class Plane:
    def __init__(self, *args):
        self.name = args[0]               # Format: 'UA352'
        self.expected_departure = args[1] # Minutes from midnight: 510 == 8:30am
        self.expected_landing = args[2]   # Minutes from midnight: 615 == 10:15am
