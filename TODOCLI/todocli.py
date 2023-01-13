import json
from datetime import date 

emptyDoc = False

while True:
    with open("todoDB.json","r") as f:
        todoData = json.load
        currentDate=date.today()

    #print(todoData, type(todoData))
    #break

    if len(todoData)== 0:
        emptyDoc = True
        username =input("\n welcome enter your name\n")
        todoData["name"] = username
        todoData["date"] = str(currentDate)

        print(f"hey {username}! I hope you r good lets start day")

        cmd = input(">")

        print("\ncreat or add task write <creat task> or <add task> ")
        todoData["today"] =[]

        if cmd == "creat tast" or cmd == "add task":
            task_description =input("\nEnter yor task description")
            scheduled_time = input("\nenter scduled time for the task:")

            task = {
                "description": task_description,
                "scheduled_time":scheduled_time
            }

            todoData["today"].append(task)

            with open("todoDB.json","w") as f:
                json.dump(todoData,f,indent=4)
    elif "today" is list (todoData,keys{}):
task= todoData["today"]
username=todoData["name"]
print(f"\nhey{username},herre are the task for your day\n")

for task in tasks:
    print(f"\ntask number{tasks.index(task)+1}")
    print("\ntask description:",task["description"])
    print("\n schedule time:",task["schedule_time"])
print("\n create another task")
cmd=input(">>")
if cmd == "create task" or "add task":
      task_description = input("\nenter your task description: ")
      scheduled_time = input("\nenter schedule_time for your task:")

      task={
          "description":task_description,
          "schedule_time":scheduled_time
      }
      todoData["today"].appand(task)
      with open("todoDb.json","r") as f:
          print("task create successful")
          print("if you want add more task,type add task/create task")
          print("if you are done,please  type done")
          continue 
