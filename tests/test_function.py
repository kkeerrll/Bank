import function
import json
from types import SimpleNamespace

operation_json = {
    "id": 464419177,
    "state": "CANCELED",
    "date": "2018-07-15T18:44:13.346362",
    "operationAmount": {
      "amount": "71024.64",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Visa Gold 9657499677062945",
    "to": "Счет 19213886662094884261"
  }

operation = json.loads(json.dumps(operation_json).replace("from", "fromCard"), object_hook=lambda d: SimpleNamespace(**d))

def test_operation_description():
    assert function.operation_description(operation) == '15.07.2018 Перевод с карты на счет\n''Visa Gold 9657 49** **** 2945 -> Счет **4261\n''71024.64 руб.'

def test_card_description():
    assert function.card_description(operation.fromCard) == "Visa Gold 9657 49** **** 2945"
    assert function.card_description(operation.to) == "Счет **4261"

