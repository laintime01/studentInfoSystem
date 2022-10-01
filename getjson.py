import json


class GetJsonData:
    def json_data(self, *json_file):
        with open('todo.json', 'r', encoding='utf-8') as jf:
            jd = json.load(jf)
            return jd

    def json_update(self, dict_new, *json_file):
        json_data = self.json_data()
        json_data.update(dict_new)
        with open('todo.json', mode='w', encoding='utf-8') as jf:
            json.dump(json_data, jf, indent=2, sort_keys=False, ensure_ascii=False)

    def json_del(self, key, *json_file):
        json_dict = self.json_data('todo.json')
        json_data = json_dict.pop(key)
        print(json_data, 'delete success')
        with open('todo.json', mode='w', encoding='utf-8') as jf:
            json.dump(json_dict, jf, indent=2, sort_keys=False, ensure_ascii=False)