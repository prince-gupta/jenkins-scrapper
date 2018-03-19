from src.j_api.jenkins_server import JenkinsServer
from src.j_api.job_workers import JobWorkers
from src.properties_util import PropertyUtil
if PropertyUtil().get('core', 'enable_gpio') is True:
    from src.gpio_api.led_status import LEDStatus

from time import sleep


class MainWorker:
    __jenkins_server__: JenkinsServer
    __job_worker__: JobWorkers

    def __init__(self):
        MainWorker.__jenkins_server__ = JenkinsServer().get_server()
        MainWorker.__job_worker__ = JobWorkers(MainWorker.__jenkins_server__, PropertyUtil().get('core', 'job'))

    def start(self):
        while True:
            status = MainWorker.__job_worker__.should_raise_alarm()
            if PropertyUtil().get('core', 'enable_gpio') is True:
                if status is True:
                    LEDStatus().mark_fail()
                else:
                    LEDStatus().mark_success()

        sleep(PropertyUtil().get('core', 'refresh_rate'))
