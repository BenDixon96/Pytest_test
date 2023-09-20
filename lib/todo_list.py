
# File: lib/todo_list.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        self.task = task
        self.is_complete = False
        
        

    def mark_complete(self):
        self.is_complete = True
        
        
       




class TodoList:
    def __init__(self):
        self.todo_list = []


    def add(self, todo):
        self.todo_list.append(todo)
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
    
      
    def incomplete(self):
        res = []
        for i in self.todo_list:
            if i.is_complete == False:
                res.append(i.task)
        return res
            
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        

    def complete(self):
        res = []
        for i in self.todo_list:
            if i.is_complete == True:
                res.append(i.task)
        return res
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        

    def give_up(self):
        for i in self.todo_list:
            i.mark_complete()
        


# File: lib/todo.py
