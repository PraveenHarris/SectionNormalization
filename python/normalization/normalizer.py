import csv
import re
from difflib import SequenceMatcher


class Normalizer(object):
    def __init__(self):
        self.data = {}

    def read_manifest(self, manifest):
        """reads a manifest file

        manifest should be a CSV containing the following columns
            * section_id
            * section_name
            * row_id
            * row_name

        Arguments:
            manifest {[str]} -- /path/to/manifest
        """
        with open(manifest) as file:
            reader = csv.DictReader(file)
            for line in reader:
                assert len(line) == 4

                section_id = line['section_id'].strip().lstrip('0').lower()
                section_name = line['section_name'].strip().lower()
                row_id = line['row_id'].strip().lower()
                row_name = line['row_name'].strip().lstrip('0').lower()

                # print(section_id, section_name, row_id, row_name)
                section_name_int = ''.join(
                    dig for dig in section_name if dig.isdigit())
                # print(section)

                builder = ''
                splitted = section_name.split(' ')
                for word in splitted:
                    if word.isalpha():
                        builder += word[0]
                    elif word.isdigit():
                        if len(builder) == 0:
                            builder = word
                        else:
                            builder += ' ' + word

                # print(splitted, builder, len(builder))

                if section_name_int in self.data.keys():
                    match = self.data[section_name_int]

                    if builder in match.keys():
                        section_match = match[builder]
                        assert section_match[0] == section_id

                        self.data[section_name_int][builder][1].update(
                            {row_name: row_id})

                    else:
                        self.data[section_name_int][builder] = [
                            section_id, {row_name: row_id}]

                else:
                    self.data[section_name_int] = {
                        builder: [section_id, {row_name: row_id}]}

        count = 0

    def normalize(self, section, row):
        """normalize a single (section, row) input

        Given a (Section, Row) input, returns (section_id, row_id, valid)
        where
            section_id = int or None
            row_id = int or None
            valid = True or False

        Arguments:
            section {[type]} -- [description]
            row {[type]} -- [description]
        """
        row = row.strip().lstrip('0').lower()
        section = section.strip().lower()

        section_id = -1
        row_id = -1
        valid = False

        section_int = ''.join(dig for dig in section if dig.isdigit())

        builder = ''
        splitted = section.split(' ')
        if len(splitted) == 1:
            letters = ''
            digits = ''
            for s in splitted[0]:
                if s.isdigit():
                    digits += s
                else:
                    letters += s
            builder = letters + ' ' + digits

        else:
            for word in splitted:
                if word.isalpha():
                    builder += word[0]
                elif word.isdigit():
                    if len(builder) == 0:
                        builder = word
                    else:
                        builder += ' ' + word
        # print(splitted, builder, len(builder))

        try:
            # print(section, self.data[section_int].keys())

            section_num_keys = self.data[section_int].keys()
            most_similar = section_num_keys[0]
            max_accuracy = SequenceMatcher(None, builder, most_similar).ratio()

            for code in section_num_keys[1:]:
                acc = SequenceMatcher(None, builder, code).ratio()
                if acc > max_accuracy:
                    most_similar = code
                    max_accuracy = acc

            section_id = self.data[section_int][most_similar][0]
        except:
            return '', '', False

        try:
            row_id = self.data[section_int][most_similar][1][row]
            # print(section, section_num_info)
            return section_id, row_id, True
        except:
            return section_id, '', False
