from lib.todo_list import *


my_task = Todo("walk dog")
task2 = Todo




    
def test_todoo_complete():
    
    my_task_list = TodoList()
    my_task_list.add(my_task)
    assert my_task.is_complete == False
    assert my_task_list.incomplete() == ["walk dog"]


def test_give_up():
    my_task_list = TodoList()
    my_task_list.add(my_task)
    more_task = Todo('laundry')
    other_task = Todo("cook")
    my_task_list.add(more_task)
    my_task_list.add(other_task)
    my_task_list.give_up()
    assert my_task_list.complete() == ['walk dog', 'laundry', 'cook']


