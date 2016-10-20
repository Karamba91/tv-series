from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class Episode_HTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []
    def handle_starttag(self, tag, attrs):
        if tag == 'pre':
            self.recording = 1

    def handle_endtag(self, tag):
        if tag == 'pre':
            self.recording = 0

    def handle_data(self, data):
        self.data.append(data)