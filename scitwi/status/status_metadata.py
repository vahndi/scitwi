from scitwi.utils.attrs import str_attr
from scitwi.utils.strs import attr_string


class StatusMetadata(object):

    def __init__(self, metadata: dict):

        self.iso_language_code = str_attr(metadata, 'iso_language_code')
        self.result_type = str_attr(metadata, 'result_type')

    def __str__(self):

        str_out = ''
        str_out += attr_string('ISO Language Code', self.iso_language_code)
        str_out += attr_string('Result Type', self.result_type)
        return str_out
