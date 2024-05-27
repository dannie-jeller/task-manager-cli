import unittest
import os
import json
from task_manager import task_manager

TASKS_FILE = 'tasks.json'

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        if os.path.exists(TASKS_FILE):
            os.remove(TASKS_FILE)

    def tearDown(self):
        if os.path.exists(TASKS_FILE):
            os.remove(TASKS_FILE)

    def test_add_task(self):
        task_manager.add_task("Test task")
        tasks = task_manager.load_tasks()
        self.assertEqual(tasks[-1]["description"], "Test task")
        self.assertFalse(tasks[-1]["completed"])

    def test_list_tasks(self):
        task_manager.add_task("Test task")
        tasks = task_manager.load_tasks()
        self.assertGreater(len(tasks), 0)

    def test_complete_task(self):
        task_manager.add_task("Test task")
        tasks = task_manager.load_tasks()
        task_manager.complete_task(0)
        tasks = task_manager.load_tasks()
        self.assertTrue(tasks[0]["completed"])

    def test_remove_task(self):
        task_manager.add_task("Test task")
        tasks = task_manager.load_tasks()
        task_manager.remove_task(0)
        tasks = task_manager.load_tasks()
        self.assertEqual(len(tasks), 0)

if __name__ == '__main__':
    unittest.main()
