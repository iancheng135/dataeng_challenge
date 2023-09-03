import unittest
import os
import tempfile

from main import read_csv, count_by_ofns_desc, count_by_age_and_pdcd, export_to_csv, exportToSQLite

class TestFunctions(unittest.TestCase):

    def setUp(self):
         self.temp_dir = tempfile.mkdtemp()

    def test_read_csv(self):
        csv_content = "OFNS_DESC,AGE_GROUP,PD_CD\n" \
                      "ASSAULT,18-24,123\n" \
                      "ROBBERY,25-34,456\n" \
                      "ASSAULT,25-34,123\n" \
                      "BURGLARY,35-44,789\n"
        with open('test_data.csv', 'w') as test_file:
            test_file.write(csv_content)

        data = read_csv('test_data.csv')

        self.assertEqual(len(data), 4)
        self.assertEqual(data[0]['OFNS_DESC'], 'ASSAULT')
        self.assertEqual(data[1]['AGE_GROUP'], '25-34')

    def test_count_by_ofns_desc(self):
        data = [
            {'OFNS_DESC': 'ASSAULT'},
            {'OFNS_DESC': 'ASSAULT'},
            {'OFNS_DESC': 'ROBBERY'},
            {'OFNS_DESC': 'BURGLARY'},
        ]

        counts = count_by_ofns_desc(data)
        expected_counts = {'ASSAULT': 2, 'ROBBERY': 1, 'BURGLARY': 1}

        self.assertEqual(counts, expected_counts)

    def test_export_to_csv(self):
        data = [
            {'OFNS_DESC': 'ASSAULT', 'AGE_GROUP': '18-24'},
            {'OFNS_DESC': 'ROBBERY', 'AGE_GROUP': '25-34'},
            {'OFNS_DESC': 'ASSAULT', 'AGE_GROUP': '25-34'},
        ]

        export_to_csv(data, 'ASSAULT', 'test_exported_data.csv')

        self.assertTrue(os.path.exists('test_exported_data.csv'))

    def test_exportToSQLite(self):
        data = [
            {'OFNS_DESC': 'ASSAULT', 'AGE_GROUP': '18-24'},
            {'OFNS_DESC': 'ROBBERY', 'AGE_GROUP': '25-34'},
            {'OFNS_DESC': 'ASSAULT', 'AGE_GROUP': '25-34'},
        ]

        exportToSQLite("nypd-arrest-data-2018-1.csv")
        
        self.assertTrue(os.path.exists('nypd-arrest-data-2018-1.db'))

if __name__ == '__main__':
    unittest.main()
