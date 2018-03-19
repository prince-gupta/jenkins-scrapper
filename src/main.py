from src.j_api.jenkins_server import JenkinsServer
from src.j_api.job_workers import JobWorkers
from time import sleep
from src.properties_util import PropertyUtil

jenkins = JenkinsServer().get_server()
job = JobWorkers(jenkins, 'python-practice')

while True:
    print(job.should_raise_alarm())
    sleep(PropertyUtil().get('core', 'refresh_rate'))
