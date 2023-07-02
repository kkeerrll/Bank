from function import *

operations = json.loads(json.dumps(open_operation()).replace("from", "fromCard"), object_hook=lambda d: SimpleNamespace(**d))

for operation in sorted(operations, key=lambda operation: datetime.datetime.strptime(operation.date, '%Y-%m-%dT%H:%M:%S.%f'))[-5:]:
    print(operation_description(operation) + '\n')