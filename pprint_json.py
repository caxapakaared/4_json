import json
import sys

def load_data(filepath):
    with open(filepath, "r", encoding='windows-1251') as json_content:
        return json.load(json_content)


def pretty_print_json(data):
    print(json.dumps(data, indent = 4, sort_keys = True, ensure_ascii=False))

if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
    except IndexError:
        print('Отсутствует путь к файлу. Программа будет завершена')
        sys.exit()
    json_content = load_data(filepath)
    pretty_print_json(json_content)
