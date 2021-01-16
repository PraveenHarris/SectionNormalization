import csv
import re


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
                # print(line)

                section_id = line['section_id'].strip().lstrip('0').lower()
                section_name = line['section_name'].strip().lower()
                row_id = line['row_id'].strip().lower()
                row_name = line['row_name'].strip().lstrip('0').lower()

                # print(section_id, section_name, row_id, row_name)
                section_name = ''.join(
                    dig for dig in section_name if dig.isdigit())
                # print(section)

                if section_name in self.data.keys():
                    self.data[section_name.lower()].update({row_name: row_id})
                else:
                    self.data[section_name.lower()] = {
                        'section_id': section_id, row_name: row_id}

        # count = 0
        # for x, y in zip(self.data.keys(), self.data.values()):
        #     count += 1
        #     print(x, y)
        # print(self.data)
        # print('count', count)
        # a = self.data['Left Field Pavilion 311']
        # print(a)
        # Your code goes here

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

        section = ''.join(dig for dig in section if dig.isdigit())
        # print(section)

        try:
            section_info = self.data[section]
            section_id = section_info['section_id']
        except:
            return '', '', False

        try:
            row_id = section_info[row]
            print(section, section_info)
            return section_id, row_id, True
        except:
            return section_id, '', False

        # return section_id, row_id, True
