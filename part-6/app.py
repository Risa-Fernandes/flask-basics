"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# ------------------------------------------------------------------
# In-memory task data
# ------------------------------------------------------------------
TASKS = [
    {
        'id': 1,
        'title': 'Learn Flask',
        'status': 'Completed',
        'priority': 'High',
        'due_date': '2026-01-10'
    },
    {
        'id': 2,
        'title': 'Build To-Do App',
        'status': 'In Progress',
        'priority': 'Medium',
        'due_date': '2026-01-15'
    },
    {
        'id': 3,
        'title': 'Push to GitHub',
        'status': 'Pending',
        'priority': 'Low',
        'due_date': '2026-01-20'
    }
]

# ------------------------------------------------------------------
# HOME – List all tasks
# ------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html', tasks=TASKS)


# ------------------------------------------------------------------
# ADD TASK
# ------------------------------------------------------------------
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_task = {
            'id': len(TASKS) + 1,
            'title': request.form['title'],
            'status': request.form['status'],
            'priority': request.form['priority'],
            'due_date': request.form['due_date']
        }
        TASKS.append(new_task)
        return redirect(url_for('index'))

    return render_template('add.html')


# ------------------------------------------------------------------
# VIEW SINGLE TASK
# ------------------------------------------------------------------
@app.route('/task/<int:id>')
def task_detail(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    if not task:
        return "Task not found", 404
    return render_template('task.html', task=task)



# ------------------------------------------------------------------
# EDIT TASK
# ------------------------------------------------------------------
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    if not task:
        abort(404)

    if request.method == 'POST':
        task['title'] = request.form['title']
        task['status'] = request.form['status']
        task['priority'] = request.form['priority']
        task['due_date'] = request.form['due_date']
        return redirect(url_for('task_detail', id=id))

    return render_template('edit.html', task=task)


# ------------------------------------------------------------------
# DELETE TASK
# ------------------------------------------------------------------
@app.route('/delete/<int:id>')
def delete_task(id):
    global TASKS
    TASKS = [t for t in TASKS if t['id'] != id]
    return redirect(url_for('index'))


# ------------------------------------------------------------------
# FILTER BY PRIORITY
# ------------------------------------------------------------------
@app.route('/priority/<name>')
def tasks_by_priority(name):
    filtered_tasks = [
        t for t in TASKS if t['priority'].lower() == name.lower()
    ]
    return render_template(
        'priority.html',
        tasks=filtered_tasks,
        priority=name.capitalize()
    )


# ------------------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------------------
@app.route('/dashboard')
def dashboard():
    total = len(TASKS)
    completed = len([t for t in TASKS if t['status'] == 'Completed'])
    pending = len([t for t in TASKS if t['status'] == 'Pending'])
    in_progress = len([t for t in TASKS if t['status'] == 'In Progress'])

    return render_template(
        'dashboard.html',
        total=total,
        completed=completed,
        pending=pending,
        in_progress=in_progress
    )


# ------------------------------------------------------------------
# ABOUT PAGE
# ------------------------------------------------------------------
@app.route('/about')
def about():
    return render_template('about.html')


# ------------------------------------------------------------------
# RUN SERVER
# ------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
