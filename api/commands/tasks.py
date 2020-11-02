import falcon
import json
import copy
import uuid

from ..mongodb import client
from pymongo import ReturnDocument
from ..scheduler.schedule import Scheduler
from bson.json_util import dumps
from bson.objectid import ObjectId

class Tasks(object):
	def __init__(self):
		self.tasksDB = client.get_mongo_collection("courses")
		self.scheduler = Scheduler()
		#print(self.tasksDB)
		#schedule.delete_tasks()
		
	def on_get(self, req, resp):
		tasks = list(self.tasksDB.find(filter={}, projection={'_id':False}))
		#tasks = list(self.tasksDB.find(filter={}))
		for task in tasks:
			active = self.scheduler.get_task(task['task_id'])
			task['active'] = active

		resp.status = falcon.HTTP_200
		resp.media = tasks

	def on_post(self, req, resp):
		#task_ID = 'test001'
		body = copy.deepcopy(req.media)
		task_id = str(ObjectId())
		data = {'task_id': task_id, 'course': req.media['course'], 'email': req.media['email']}
		r = self.tasksDB.insert_one(data)

		task_active = self.scheduler.create_task(body, task_id)

		data = {'task_id': task_id, 'course': body['course'], 'email': body['email'], 'active': task_active, 'status': r.acknowledged}
		resp.status = falcon.HTTP_200
		resp.media = data


	def on_delete(self, req, resp):
		r = self.tasksDB.delete_many({})
		deleted_jobs = self.scheduler.delete_tasks()

		resp.status = falcon.HTTP_200
		data = {'status': r.acknowledged, 'deleted_documents': r.deleted_count, 'deleted_jobs': deleted_jobs}
		resp.media = data


	def on_get_single(self, req, resp, task_id):
		task = self.tasksDB.find_one(filter={'task_id': task_id}, projection={'_id':False})

		if task:
			task_active = self.scheduler.get_task(task_id)
			task['active'] = task_active

			resp.status = falcon.HTTP_200
			resp.media = task
		else:
			resp.status = falcon.HTTP_404

	def on_put_single(self, req, resp, task_id):
		body = copy.deepcopy(req.media)
		update_operator = {}
		for key, item in body.items():
			if key == 'email':
				update_operator['email'] = body['email']
			else:
				op = "course." + key
				update_operator[op] = item

		task = self.tasksDB.find_one_and_update(filter={'task_id': task_id}, update={'$set': update_operator}, projection={'_id':False}, return_document=ReturnDocument.AFTER)

		resp.media = task

	def on_delete_single(self, req, resp, task_id):
		r = self.tasksDB.find_one_and_delete(filter={'task_id': task_id})

		if r:
			self.scheduler.delete_task(task_id)

			resp.status = falcon.HTTP_200
		else:
			resp.status = falcon.HTTP_404

