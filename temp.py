import json


def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        file.close()
    return data


if __name__ == '__main__':
    ddg_data = load_data('hw1.json')
    c = 0

    for k, v in ddg_data.items():
        c += 1
        if len(v) < 10:
            print(k)
    print("all pass", c)
