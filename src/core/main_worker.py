from src.j_api.jenkins_server import JenkinsServer
from src.j_api.job_workers import JobWorkers
from src.properties_util import PropertyUtil
from src.gpio_api.led_status import LEDStatus

from time import sleep


class MainWorker:
    __jenkins_server__: JenkinsServer
    __job_worker__: JobWorkers

    def __setup_jenkins_server__(self):
        MainWorker.__jenkins_server__ = JenkinsServer().get_server()

    def __setup_job_worker(self):
        MainWorker.__job_worker__ = JobWorkers(MainWorker.__jenkins_server__, PropertyUtil().get('core', 'job'))

    def start(self):
        while True:
            status = MainWorker.__job_worker__.should_raise_alarm()
            if status is True:
                LEDStatus().mark_fail()
            else:
                LEDStatus().mark_success()

        sleep(PropertyUtil().get('core', 'refresh_rate'))
