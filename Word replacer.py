def replace_word():

    str = "  What's good, I'm Samuel and hi hi hi hi  "
    word_to_replace = input("Enter the word you want to replace: ")
    word_replacement = input("Enter the word of replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()