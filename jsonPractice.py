import json

task = '''{
  "id": 3,
  "todo": "Watch a classic movie",
  "completed": false,
  "userId": 4,
  "tags": ["personal", "entertainment"]
}'''

parsedTask = json.loads(task)
print(task)
print(parsedTask)
print(type(task))
print(type(parsedTask))
print(parsedTask["completed"])
print(type(parsedTask["completed"]))

parsedTask["id"] = 5
print(parsedTask)

#dumpedTask = json.dumps(parsedTask, indent=4, sort_keys=True, separators=("_","*"))
dumpedTask = json.dumps(parsedTask, indent=4)
print(dumpedTask)
print(type(dumpedTask))

