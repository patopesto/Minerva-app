import smtplib
import logging

logger = logging.getLogger(__name__)



def notify(course, crn, spaces, recipients):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("bambinito.dev@gmail.com", "@RZKrkaJ238qTTef")

	msg = "The course " + course + " (" + crn + "), has " + str(spaces) + " seats remaining."
	#to_addr = ["alban.moreon@gmail.com", "bambinito.dev@gmail.com"]
	server.sendmail("bambinito.dev@gmail.com",recipients, msg)
	logger.info("Email sent to {} for course {}".format(', '.join(to_addr), course))
	server.quit()