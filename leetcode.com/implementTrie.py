"""
Description:

  208. Implement Trie (Prefix Tree)

  A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

  Implement the Trie class:

  Trie() Initializes the trie object.
  void insert(String word) Inserts the string word into the trie.
  boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
  boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

  Input
  ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
  [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

  Output
  [null, null, true, false, true, null, true]

  Explanation
  Trie trie = new Trie();
  trie.insert("apple");
  trie.search("apple");   // return True
  trie.search("app");     // return False
  trie.startsWith("app"); // return True
  trie.insert("app");
  trie.search("app");     // return True

Usage:
    `python <file_name.py>`

Arguments:
    None

Date:
    2024-12-04

Version:
    1.0.0

Algorithm Implementation:



Complexities:



Tryouts:

      .
     a
    p
   p
  l
 e


"""


class TrieNode:
    def __init__(self):
        self.children = {}  # dictionary
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        currentNode = self.root

        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]

        currentNode.isEndOfWord = True

    def search(self, word: str) -> bool:

        currentNode = self.root

        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]

        if currentNode.isEndOfWord == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:

        currentNode = self.root

        for char in prefix:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]

        return True


def test_trie():

    # Your Trie object will be instantiated and called as such:
    obj = Trie()
    word = "apple"
    prefix = "app"
    non_prefix = "abb"
    obj.insert(word)
    assert obj.search(word) == True
    assert obj.startsWith(prefix) == True
    assert obj.startsWith(non_prefix) == False


test_trie()
print("All tests passed!")
