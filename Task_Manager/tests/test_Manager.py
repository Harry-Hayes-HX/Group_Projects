import pytest
from unittest.mock import patch
from io import StringIO
from ..Task_Manager import TaskManager

class TestTaskManager:
    def test_menu_options(self):
        # Prepare the expected output
        expected_output = """-----MENU-----
1: Add_tasks
2: List_tasks
3: Modify_tasks
4: Complete_tasks
5: Delete_tasks
6: QUIT"""

        # Create a TaskManager instance
        task_manager = TaskManager()

        # Redirect stdout to a StringIO object to capture the output
        output = StringIO()
        with patch('sys.stdout', new=output):
            # Call the method to display the menu options
            task_manager.display_menu()

        # Check if the output matches the expected output (stripping whitespaces)
        assert output.getvalue().strip() == expected_output.strip()

    def test_add_tasks(self):
        # Create a TaskManager instance
        task_manager = TaskManager()

        # Mock user input to add a task
        with patch('builtins.input', side_effect=['task1', 'Task 1 description', '3', 'no', 'no']):
            task_manager.Add_tasks()

        # Check if the task was added as expected
        assert 'task1' in task_manager.Tasks
        assert task_manager.Tasks['task1']['description'] == 'Task 1 description'
        assert task_manager.Tasks['task1']['importance'] == 3
        assert task_manager.Tasks['task1']['completion'] == 'no'

    def test_add_existing_task(self):
        # Create a TaskManager instance
        task_manager = TaskManager()

        # Add a task with name 'task1'
        task_manager.Tasks = {
            'task1': {'description': 'Task 1 description', 'importance': 3, 'completion': 'no'},
        }

        # Mock user input to add the same task again
        with patch('builtins.input', side_effect=['task1', 'Task 1 description', '3', 'no', 'no']):
            # Redirect stdout to a StringIO object to capture the output
            output = StringIO()
            with patch('sys.stdout', new=output):
                task_manager.Add_tasks()

        # Check if the task was not added again
        assert 'task1' in task_manager.Tasks
        assert len(task_manager.Tasks) == 1  # Make sure there's only one task in the TaskManager

        # Check if the expected message was printed
        assert "The task already exists." in output.getvalue().strip()

    def test_list_tasks(self):
        # Create a TaskManager instance
        task_manager = TaskManager()

        # Add some tasks to the TaskManager
        task_manager.Tasks = {
            'task1': {'description': 'Task 1 description', 'importance': 3, 'completion': 'no'},
            'task2': {'description': 'Task 2 description', 'importance': 2, 'completion': 'no'},
            'task3': {'description': 'Task 3 description', 'importance': 4, 'completion': 'yes'},
        }

        # Mock user input to list all tasks
        with patch('builtins.input', return_value='yes'):
            # Redirect stdout to a StringIO object to capture the output
            output = StringIO()
            with patch('sys.stdout', new=output):
                task_manager.List_tasks()

            # Check if the output contains the correct tasks
            assert 'task1 -- Task 1 description, 3 (3), no' in output.getvalue().strip()
            assert 'task2 -- Task 2 description, 2 (4), no' in output.getvalue().strip()
            assert 'task3 -- Task 3 description, 4 (2), yes' in output.getvalue().strip()

        # Mock user input to list only non-completed tasks
        with patch('builtins.input', return_value='no'):
            # Redirect stdout to a StringIO object to capture the output
            output = StringIO()
            with patch('sys.stdout', new=output):
                task_manager.List_tasks()

            # Check if the output contains only non-completed tasks
            assert 'task1 -- Task 1 description, 3 (3), no' in output.getvalue().strip()
            assert 'task2 -- Task 2 description, 2 (4), no' in output.getvalue().strip()
            assert 'task3' not in output.getvalue().strip()

    def test_list_tasks_no_tasks(self):
        # Create a TaskManager instance
        task_manager = TaskManager()

        # Mock user input to display all tasks
        with patch('builtins.input', return_value='yes'):
            # Redirect stdout to a StringIO object to capture the output
            output = StringIO()
            with patch('sys.stdout', new=output):
                task_manager.List_tasks()

        # Check if the output contains the correct message
        assert "No tasks found." in output.getvalue().strip()

    def test_modify_task(self):
        # Create a TaskManager instance
        task_manager = TaskManager()

        # Add a task to the TaskManager
        task_manager.Tasks = {
            'task1': {'description': 'Task 1 description', 'importance': 3, 'completion': 'no'},
        }

        # Mock user input to modify the task
        with patch('builtins.input', side_effect=['new description']):
            result = task_manager.Modify('task1', 'new description')

        # Check if the task was modified as expected
        assert result == "Task 'task1' has been modified with the new description: 'new description'."
        assert task_manager.Tasks['task1']['description'] == 'new description'

        # Test modifying a completed task
        task_manager.Tasks['task2'] = {'description': 'Task 2 description', 'importance': 2, 'completion': 'yes'}
        result = task_manager.Modify('task2', 'modified description')
        assert result == "You cannot edit completed task 'task2'."
        assert task_manager.Tasks['task2']['description'] == 'Task 2 description'

    def test_modify_completed_task(self):
        # Create a TaskManager instance
        task_manager = TaskManager()

        # Add a completed task to the TaskManager
        task_manager.Tasks = {
            'task1': {'description': 'Task 1 description', 'importance': 3, 'completion': 'yes'},
        }

        # Mock user input to modify the task
        with patch('builtins.input', side_effect=['new description']):
            result = task_manager.Modify('task1', 'new description')

        # Check if the task was not modified
        assert result == "You cannot edit completed task 'task1'."
        assert task_manager.Tasks['task1']['description'] == 'Task 1 description'

if __name__ == '__main__':
    # Run the pytest
    pytest.main()
