import re
import sys


def separate_words(text):
    """
    Separates a text into words
    :param text: text to separate into words
    :return: list with all words
    """
    if text:
        splitter = re.compile('[^a-zA-Z0-9_\\+\\-]')
        return [word.strip().lower() for word in splitter.split(text) if len(word)]
    return []


def count_words(words):
    """
    Count words provided in a list
    :param words: list of words to count
    :return: dict of words and word count
    """
    words_count = {}
    if words:
        for word in words:
            words_count[word] = words_count[word]+1 if word in words_count else 1
    return words_count


def process_text(text):
    """
    Process a test file by counting words
    :param text: input test string
    :return: dict of words and word count
    """

    # Separate words
    words = separate_words(text)

    # Count words
    words_count = count_words(words)
    for word, count in words_count.iteritems():
        print count, word
    return words_count


if __name__ == "__main__":

    if len(sys.argv) == 2:
        if sys.argv[1] == '--help':
            print "Usage: python words.py <file path>"
        else:
            try:
                with open(sys.argv[1], 'r+') as f:
                    process_text(f.read())
            except Exception, e:
                print e.message
    else:
        print "Invalid file name entered!"
