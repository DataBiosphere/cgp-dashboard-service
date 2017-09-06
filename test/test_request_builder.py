#!/usr/bin/python

import json
import difflib
import unittest
from responseobjects.api_response import KeywordSearchResponse, FileSearchResponse
from responseobjects.elastic_request_builder import ElasticTransformDump as EsTd


class MyTestCase(unittest.TestCase):
    def test_create_request(self):
        """
        Tests creation of a simple request
        :return: True or False depending on the assertion
        """
        # Load files required for this test
        request_config = EsTd.open_and_return_json('test_request_config.json')
        expected_output = EsTd.open_and_return_json('request_builder_test1.json')
        # Create a simple filter to test on
        sample_filter = {"file": {"projectCode": {"is": ["CGL"]}}}
        # Need to work on a couple cases:
        # - The empty case
        # - The 1 filter case
        # - The complex multiple filters case

        # Create ElasticTransformDump instance
        es_ts_instance = EsTd()
        # Create a request object
        es_search = EsTd.create_request(sample_filter, es_ts_instance.es_client, request_config, post_filter=True)
        # Convert objects to be compared to strings
        expected_output = json.dumps(expected_output, sort_keys=True)
        actual_output = json.dumps(es_search.to_dict(), sort_keys=True)
        # Print the 2 strings for reference
        print "Printing expected output: \n %s" % expected_output
        print "Printing actual output: \n %s" % actual_output
        # Now show differences so message is helpful
        print "Comparing the two dictionaries built."
        print('{}... => {}...'.format(actual_output[:20], expected_output[:20]))
        for i, s in enumerate(difflib.ndiff(actual_output, expected_output)):
            if s[0] == ' ':
                continue
            elif s[0] == '-':
                print(u'Delete "{}" from position {}'.format(s[-1], i))
            elif s[0] == '+':
                print(u'Add "{}" to position {}'.format(s[-1], i))
        # Testing first case with 1 filter
        self.assertEqual(actual_output, expected_output)

    def test_create_request_empty(self):
        # Testing with default (that is, no) filter
        sample_filter = {"file": {"projectCode": {"is": []}}}
        # Load files required for this test
        es_ts_instance = EsTd()
        request_config = EsTd.open_and_return_json('test_request_config.json')
        es_search = EsTd.create_request(sample_filter, es_ts_instance.es_client, request_config)
        expected_output = EsTd.open_and_return_json('request_builder_test2.json')
        expected_output = json.dumps(expected_output, sort_keys=True)
        actual_output = json.dumps(es_search.to_dict(), sort_keys=True)
        # Print the 2 strings for reference
        print "Printing expected output: \n %s" % expected_output
        print "Printing actual output: \n %s" % actual_output
        # Now show differences so message is helpful
        print "Comparing the two dictionaries built."
        print('{}... => {}...'.format(actual_output[:20], expected_output[:20]))
        for i, s in enumerate(difflib.ndiff(actual_output, expected_output)):
            if s[0] == ' ':
                continue
            elif s[0] == '-':
                print(u'Delete "{}" from position {}'.format(s[-1], i))
            elif s[0] == '+':
                print(u'Add "{}" to position {}'.format(s[-1], i))
        # Testing first case with 1 filter
        # NOT WORKING, SOMEHOW THE FILTERS ARE MAKING IT INTO THE QUERY CONSTRUCTOR WHEN THERE SHOULDN'T BE ANY
        self.assertEqual(actual_output, expected_output)

    def test_transform_request(self):
        mapping_config = EsTd.open_and_return_json('test_mapping_config.json')
        pass

if __name__ == '__main__':
    unittest.main()
