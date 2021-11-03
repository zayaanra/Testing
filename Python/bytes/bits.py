import json

ex = json.loads('{"first":"Clark","last":"Kent"}')
exAsJson = json.dumps(ex, separators=(",", ":"))
print(exAsJson)
# exAsStr = str(ex)
# exStrToBytes = exAsStr.encode()

# print(ex)
# print(exAsStr)
# print(exStrToBytes)