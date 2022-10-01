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
            json.dump(json_data, jf, indent=2, sort_keys=True, ensure_ascii=False)

