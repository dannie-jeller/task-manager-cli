from setuptools import setup, find_packages

setup(
    name='task-manager-cli',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'task-manager=task_manager.task_manager:main',
        ],
    },
)
