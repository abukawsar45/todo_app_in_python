def show_menu():
  print('\nTodo App Menu')
  print('1. Add Task')
  print('2. View Task')
  print('3. Mark Task As Complete')
  print('4. Delete Task')
  print('5. Exit')

def add_task(tasks, task):
  tasks.append(task)
  print(f'Task {task} added successfully!')

def view_task(tasks):
  print('\nTasks: ')
  for index, task in enumerate(tasks, start=1):
    print(f'{index}, {task} ')

def mark_complete(tasks, index):
  if 1<= index <=len(tasks):
    print(f"Task '{tasks[index-1]}' marked as completed! ")
    tasks[index-1] = f'[completed] {tasks[index-1]}'
  else:
    print('Invalid Task Index!')

def delete_task(tasks, index):
  if 1<= index <= len(tasks):
      remove_task = tasks.pop(index-1)
      print(f'Task "{remove_task}" marked as completed!! ')
  else:
    print('Invalid Task Index!')

def main():
  tasks = []


  while True:
    show_menu()
    choice= input("Enter your choice (1-5): ")

    if choice == '1':
      task = input("Enter your Task: ")
      add_task( tasks, task)

    elif choice == '2':
      view_task( tasks)

    elif choice == '3':
      index = int(input("Enter the task task index to mark complete: "))
      mark_complete(tasks, int(index))

    elif choice == '4':
       index = int(input('Enter task index to delete: '))
       delete_task(tasks, index)

    elif choice == '5':
      print('Exiting from Todo App. Bye||')
      break




if __name__ == '__main__':
  main()