import json


def task() -> float:
    with open("input.json") as f:
        json_ = json.load(f)

    sum_ = sum([item["score"] * item["weight"] for item in json_])
    return round(sum_, 3)


print(task())
