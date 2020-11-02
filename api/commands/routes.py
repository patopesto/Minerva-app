from . import (
	welcome,
	things,
	tasks
	)

def setup_routes(app):
	Welcome = welcome.Welcome()
	Things = things.Things()
	Tasks = tasks.Tasks()

	app.add_route('/', Welcome)

	app.add_route('/things', Things)

	app.add_route('/tasks', Tasks)
	app.add_route('/tasks/{task_id}', Tasks, suffix="single")

	return app