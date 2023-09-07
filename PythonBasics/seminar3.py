'''
Homework for seminar3
'''

def duplicate_elements(user_list):
    '''
    Returns list of duplicates from user given list
    '''
    return set(filter(lambda item: user_list.count(item) > 1, user_list))


def ten_most_common_words():
    '''
    Returns 10 most common words in the text provided 
    '''
    article = input('Enter text: ').lower()

    non_alphabet = '''( ) ` ~ ! @ # $ % ^ & * - + = | \ { } [ ] : ; " ' < > , . ? / _1234567890'''

    for nonchar in non_alphabet:
        article = article.replace(nonchar, ' ')

    article_list = article.split()

    word_count_dict = dict()

    for word in article_list:
        word_count_dict[word] = article_list.count(word)

    sorted_word_count_dict = dict(sorted(word_count_dict.items(), key=lambda item: item[1]))

    ten_most_common_words = []
    
    for _ in range(10):
        ten_most_common_words.append(sorted_word_count_dict.popitem())
        
    print(ten_most_common_words)


def backpack_variations(things_dict, backpack_capacity):
    '''
    Returns backpack variations when given backpack capacity in grams and a dictionary of things
    and their corresponding weight.
    
    Input example: 
    
    things_dict = {'pen': 10, 'book': 500, 'notebook': 1500, 'refrigerator': 30000, 'lunch': 500, \
               'chair': 10000, 'coat': 900, 'wallet': 150, 'umbrella': 300, 'medicine': 100, \
                'random_item': 3000}

    backpack_capacity = 3000
    '''
    
    backpack = 0
    all_possible_variations = []
    
    things_dict = dict(filter(lambda item: item[1] < backpack_capacity, things_dict.items()))

    for key1, value1 in things_dict.items():
        backpack = value1
        possible_variation = [key1]  
        for key2, value2 in things_dict.items():
            if backpack < backpack_capacity and key2 not in possible_variation:
                backpack += value2
                possible_variation.append(key2)
        all_possible_variations.append(possible_variation)
        backpack = 0

    for list_item in all_possible_variations:
        list_item.sort()

    i = 1
    for list_item_i in all_possible_variations[i]:
        for list_item_j in all_possible_variations[i-1]:
            if list_item_i == list_item_j:
                all_possible_variations.pop(i)

    for variation in all_possible_variations:
        print(variation)

