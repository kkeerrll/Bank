import json
import datetime
from types import SimpleNamespace

def open_operation():
    file = open("operations.json")
    return json.load(file)
def operation_description(operation):
    date = datetime.datetime.strptime(operation.date, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    firstLine = date + " " + operation.description + "\n"
    secondLine = card_description(operation.to) + "\n"
    thirdLine = operation.operationAmount.amount + " " + operation.operationAmount.currency.name

    if "fromCard" in operation.__dict__.keys():
        secondLine = card_description(operation.fromCard) + " -> " + secondLine

    return firstLine + secondLine + thirdLine

def card_description(card_operation):
    card_operations_components = card_operation.split()

    if card_operations_components[0] == "Счет":
        return "Счет **" + card_operations_components[1][-4:]
    else:
        l = card_operations_components[-1]
        return (f'{" ".join(card_operations_components[:-1])} {l[:4]} {l[4:6]}** **** {l[12:]}')