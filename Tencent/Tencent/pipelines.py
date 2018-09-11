# -*- coding: utf-8 -*-
import json


class TencentPipeline(object):

#   功能：保存item数据

    def __init__(self):
        self.filename = open("tencent.json", "w")

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
        self.filename.write(text.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.filename.close()