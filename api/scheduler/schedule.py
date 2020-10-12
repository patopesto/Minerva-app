import logging

#from app import get_scheduler as scheduler

from ..minerva.minerva import minerva_task
from .notifier import notify

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore

from ..mongodb.client import get_mongo_client

logger = logging.getLogger(__name__)


class Scheduler:
	def __init__(self):
		jobstore = MongoDBJobStore(database='minerva', collection='apscheduler_jobs', client=get_mongo_client())

		self.scheduler = BackgroundScheduler()
		self.scheduler.add_jobstore(jobstore)
		self.scheduler.start()

		self.scheduler_rate = 1

	def create_task(self, body, task_id):
		try:
			#minerva_task(course['course'])
			job = self.scheduler.add_job(task, "interval", args=[body], minutes=self.scheduler_rate, id=task_id)
			return True
		except:
			logger.error("Error trying to create scheduler job for {}".format(body['course']["dept"]+body['course']["code"]))
			return False

	def get_task(self, task_id):
		job = self.scheduler.get_job(job_id=task_id)
		if job:
			return True
		else:
			return False


	def delete_task(self, task_id):
		job = self.scheduler.get_job(job_id=task_id)
		if job:
			self.scheduler.remove_job(job_id=task_id)


	def delete_tasks(self):
		deleted = 0
		for job in self.scheduler.get_jobs():
			job.remove()
			deleted += 1
		return deleted


def task(body):
	course = body['course']
	spaces = minerva_task(course)
	spaces += 1
	if spaces > 0:
		course_text = "{}-{}".format(course['dept'],course['dept'])
		notify(course_text, course['crn'], spaces, body['email'])


