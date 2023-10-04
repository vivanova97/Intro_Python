import json

__all__ = ['text_file_to_json']

def text_file_to_json(input_file, output_file):
    
    '''Serializes to json a txt file in the following format: key|value'''
    
    with(
        open(input_file, 'r', encoding='utf-8') as txt_f,
        open(output_file, 'w+', encoding='utf-8') as json_f
    ):
        dictionary = {}
        
        for line in txt_f:
            line_list = line.strip().split('|')
            dictionary[line_list[0]] = float(line_list[1])
        
        json.dump(dictionary, json_f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    text_file_to_json('text.txt', 'json_file.json')
