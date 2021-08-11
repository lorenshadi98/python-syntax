def print_upper_words(words, must_start_with):
    for letters in must_start_with:
        for word in words:
            if word.startswith(letters):
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})
