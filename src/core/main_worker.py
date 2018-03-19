from src.j_api.jenkins_server import JenkinsServer
from src.j_api.job_workers import JobWorkers
from src.properties_util import PropertyUtil
if PropertyUtil().get('core', 'enable_gpio') is True:
    from src.gpio_api.led_status import LEDStatus

from time import sleep


class MainWorker:
    jenkins_server = JenkinsServer
    job_worker =  JobWorkers

    def __init__(self):
        MainWorker.jenkins_server = JenkinsServer().get_server()
        MainWorker.job_worker = JobWorkers(MainWorker.jenkins_server, PropertyUtil().get('core', 'job'))

    def start(self):
        while True:
            status = MainWorker.job_worker.should_raise_alarm()
            if PropertyUtil().get('core', 'enable_gpio') is True:
                if status is True:
                    LEDStatus().mark_fail()
                else:
                    LEDStatus().mark_success()

        sleep(PropertyUtil().get('core', 'refresh_rate'))
