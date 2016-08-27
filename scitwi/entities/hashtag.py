class Hashtag(object):

    def __init__(self, hashtag):

        self.indices = hashtag['indices']
        self.text = hashtag['text']

    def __str__(self):

        str_out = 'HASHTAGS\n'
        str_out += '--------\n\n'
        str_out += 'Indices:\n'
        str_out += '\t%s\n' % self.indices
        str_out += 'Text:\n'
        str_out += '\t%s\n' % self.text
