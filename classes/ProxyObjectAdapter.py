from datetime import datetime
import json
class ProxyObjectAdapter:
    def toArray(proxyObject, customFormats):
        keys = proxyObject.keys()
        data = []
        for row in proxyObject:
            rowObj = {}
            for key in keys:
                for format in customFormats:
                    rowObj[key] = format.ifChangesRequired(key, row[key])
            data.append(rowObj)
        return data

class customDateFormat:
    def ifChangesRequired(key, data):
        if key == "date":
            return data.strftime('%Y-%m-%d')
        else: 
            return data

class customSlotsFormat:
    def ifChangesRequired(key, data):
        if key == "slots":
            return json.loads(data)
        else: 
            return data