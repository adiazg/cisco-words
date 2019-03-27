from cisco.challenge import words

import os
import unittest


class TestWordsMethods(unittest.TestCase):

    def get_file_text(self, file_name):
        """Returns the text contained in a test file """
        file = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.join("files", file_name))
        f = open(file, 'r+')
        return f.read()

    def test_count_words_empty(self):
        """Test count_words method with empty list"""
        expected = {}
        count = words.count_words([])
        self.assertDictEqual(count, expected)

    def test_count_words_none(self):
        """Test count_words method with no list"""
        expected = {}
        count = words.count_words(None)
        self.assertDictEqual(count, expected)

    def test_count_words(self):
        """Test count_words method"""
        expected = {
            "simple": 1,
            "sentence": 1,
            "for": 1,
            "words": 2,
            "counting": 1,
            "all": 1
        }
        count = words.count_words(["simple", "sentence", "for", "words", "counting", "all", "words"])
        self.assertDictEqual(count, expected)

    def test_separate_words_empty(self):
        """Test separate_words method with empty text"""
        expected = []
        count = words.separate_words("")
        self.assertEqual(count, expected)

    def test_separate_words_none(self):
        """Test separate_words method with no text"""
        expected = []
        count = words.separate_words(None)
        self.assertEqual(count, expected)

    def test_separate_words(self):
        """Test separate_words method"""
        expected = []
        count = words.separate_words("")
        self.assertEqual(count, expected)

    def test_proces_text_files(self):
        """Test multiple test files"""
        expected = {'coach': 1, 'athletic': 1, 'sporting': 1, 'four': 7, 'held': 1, 'selection': 2, 'through': 1, 'committee': 1, 'its': 1, 'before': 1, 'regions': 1, 'chosen': 1, 'elite': 1, 'weekends': 1, 'to': 2, '4': 1, '8': 1, 'include': 1, 'midwest': 1, 'tuesday': 1, 'division': 3, 'over': 1, 'march': 2, 'famous': 1, 'game': 1, 'course': 2, 'during': 3, 'sixteen': 1, 'association': 2, 'level': 1, 'wednesday': 1, 'teams': 9, 'coaches': 1, 'each': 3, 'become': 1, 'automatic': 1, 'round': 4, 'week': 2, 'spring': 1, 'national': 4, 'idea': 1, 'across': 1, 'college': 1, 'are': 3, 'event': 1, 'pre-selected': 1, 'televised': 1, 'for': 3, 'currently': 2, 'sites': 1, 'state': 1, 'then': 1, 'occurs': 1, 'announced': 1, 'harold': 1, 'respectively': 1, 'team': 3, 'men': 1, 'elimination': 1, 'ranked': 1, 'olsen': 1, 'ohio': 2, '1939': 1, 'beginning': 1, 'by': 3, 'seeded': 2, 'on': 1, 'last': 1, 'created': 1, 'receive': 1, '32': 2, 'region': 2, 'annual': 1, '36': 1, 'april': 1, 's': 1, 'games': 3, 'usually': 1, 'or': 1, 'south': 1, 'first': 7, 'berths': 1, 'madness': 1, 'sweet': 1, 'into': 2, 'within': 1, 'rank': 1, 'one': 2, '64': 1, 'play-in': 1, 'determine': 1, '68': 2, 'next': 2, 'rounds': 1, 'east': 1, 'basketball': 3, 'from': 4, 'proceed': 1, 'west': 1, 'three': 1, 'awarded': 1, 'needed': 1, 'featuring': 1, 'branded': 1, 'was': 2, 'final': 2, 'location': 1, 'citation': 1, 'mostly': 1, 'low-seeded': 1, 'neutral': 1, 'known': 1, 'with': 1, 'champions': 1, 'begins': 1, 'has': 1, '16': 1, 'these': 2, 'single-elimination': 2, 'bids': 1, 'will': 1, 'dubbed': 1, 'preselected': 1, 'pre-determines': 1, 'of': 10, 'and': 10, 'ncaa': 4, 'conferences': 1, 'played': 3, 'is': 3, 'tournament': 6, 'organized': 1, 'it': 2, 'an': 1, 'states': 3, 'as': 1, 'at': 1, 'in': 9, 'face': 1, 'united': 3, 'divided': 1, 'when': 1, '1': 2, 'also': 1, 'sunday': 2, 'at-large': 2, 'which': 4, 'events': 1, 'single-game': 1, 'championship': 2, 'dayton': 1, 'preceding': 1, 'after': 1, 'nationally': 1, 'most': 1, 'eight': 1, 'weekend': 3, 'consisting': 2, 'a': 11, 'i': 3, 'wins': 1, 'collegiate': 1, 'bracket': 2, 'compete': 1, 'position': 1, 'the': 30, 'playing': 2}
        count = words.process_text(self.get_file_text("basketball"))
        print count
        self.assertEqual(count, expected)
