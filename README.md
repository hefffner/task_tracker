# task-tracker CLI
Simple command utility for tracking tasks. Runs on Python.
Project from https://roadmap.sh/projects/task-tracker

## Setup
```bash
git clone https://github.com/hefffner/task_tracker.git
cd task_tracker
chmod +x task-cli
./task-cli
OR
python3 task-cli
```
## Usage
Add a task
```bash
task-cli add "New task"
```
List tasks 
```bash
task-cli list [todo, done, in-progress]
```
Delete a task
```bash
task-cli delete [id]
```
Update a task
```bash
task-cli update [id] "New description"
```
Mark done, in progress
```bash
task-cli [mark-done, mark-in-progress] [id]
```

### All tasks stored in a JSON file
