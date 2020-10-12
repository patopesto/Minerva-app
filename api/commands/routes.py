from . import (
	welcome,
	things,
	tasks
	)

def setup_routes(app):

	app.add_route('/', welcome.Welcome())

	app.add_route('/things', things.Things())

	app.add_route('/tasks', tasks.Tasks())
	app.add_route('/tasks/{task_id}', tasks.Tasks(), suffix="single")

	return app