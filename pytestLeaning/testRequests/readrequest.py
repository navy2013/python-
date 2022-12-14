import csv


class ReadCsv():
    def read_cvs(self):
        item = []
        with open("requests.csv", "r", encoding="utf-8") as f:
            reader = csv.reader(f)  # [['http://apis.juhe.cn/mobile/get', '{"phone":18434897968,"key":ac527a2b4613d115a0f7362c1994d7c}', 'post'], ['http://v.juhe.cn/toutiao/index', '{"type":"top","key":"50c7dff49882c3bb72900a7799004a8c"}', 'get']]
            # reader = csv.DictReader(f)  # [{'url': 'http://apis.juhe.cn/mobile/get', 'params': '{"phone":18434897968,"key":ac527a2b4613d115a0f7362c1994d7c}', 'method': 'post'}, {'url': 'http://v.juhe.cn/toutiao/index', 'params': '{"type":"top","key":"50c7dff49882c3bb72900a7799004a8c"}', 'method': 'get'}]
            for csv_i in reader:
                item.append(csv_i)
            item = item[1:]
        return item


r = ReadCsv()
a = r.read_cvs()
print(a)
