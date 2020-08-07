import unittest
from trie import Trie


class TrieTest(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_trie_size(self):
        self.trie.addWord('apple')
        self.assertEqual(self.trie.height(), 6)

    def test_prefix_not_found_as_whole_word(self):
        self.trie.addWord('apple')
        self.trie.addWord('appreciate')
        self.assertEqual(self.trie.find('app'), None)

    def test_prefix_is_also_whole_word(self):
        self.trie.addWord('apple')
        self.trie.addWord('appreciate')
        self.trie.addWord('app')
        # 10: [app], [appr], [appre], [apprec], [appreci], [apprecia]
        # [appreciat], [appreciate], [appl], and [apple]
        self.assertEqual(self.trie.height(self.trie.find('app')), 10)
        self.assertEqual(self.trie.find('app').isWord, True)

    def test_starts_with(self):
        self.trie.addWord('apple')
        self.trie.addWord('appreciate')
        self.trie.addWord('aposematic')
        self.trie.addWord('apoplectic')
        self.trie.addWord('appendix')
        self.assertEqual(self.trie.begin_with('app'), ['apple', 'appreciate', 'appendix'])

    def test_starts_with_self(self):
        self.trie.addWord('app')
        self.assertEqual(self.trie.begin_with('app'), ['app'])

    def test_bigger_size(self):
        self.trie.addWord('bad')
        self.trie.addWord('bat')
        self.trie.addWord('cat')
        self.trie.addWord('cage')
        self.assertEqual(self.trie.height(), 10)

    def test_starts_with_empty_and_no_words(self):
        self.assertEqual(self.trie.begin_with(''), [])

    def test_starts_with_empty_returns_all_words(self):
        self.trie.addWord('bad')
        self.trie.addWord('bat')
        self.trie.addWord('cat')
        self.trie.addWord('cage')
        self.assertEqual(self.trie.begin_with(''), ['bad', 'bat', 'cat', 'cage'])


if __name__ == '__main__':
    unittest.main()