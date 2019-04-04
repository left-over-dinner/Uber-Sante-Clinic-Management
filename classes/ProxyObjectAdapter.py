from datetime import datetime
class ProxyObjectAdapter:
    def toArray(proxyObject, customFormat):
        keys = proxyObject.keys()
        data = []
        for row in proxyObject:
            rowObj = {}
            for key in keys:
                rowObj[key] = customFormat.ifChangesRequired(key, row[key])
            data.append(rowObj)
        return data

class customDateFormat:
    def ifChangesRequired(key, data):
        if key == "date":
            print
            return data.strftime('%Y-%m-%d')
        else: 
            return data