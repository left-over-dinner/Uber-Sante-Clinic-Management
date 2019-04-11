from datetime import datetime
import json
class ProxyObjectAdapter:
    def toArray(proxyObject, customFormats):
        keys = proxyObject.keys()
        data = []
        for row in proxyObject:
            rowObj = {}
            for key in keys:
                for formatQ in customFormats:
                    adaptedFormat = formatQ.ifChangesRequired(key, row[key])
                    if adaptedFormat is not None:
                        rowObj[key] = adaptedFormat
                        break
            data.append(rowObj)
        return data

class customDateFormat:
    def ifChangesRequired(key, data):
        if key == "date" and data is not None:
            return data.strftime('%Y-%m-%d')
        else:
            return None
    pass

class customSlotsFormat:
    def ifChangesRequired(key, data):
        if key == "slots":
            return json.loads(data)
        else: 
            return data
    pass