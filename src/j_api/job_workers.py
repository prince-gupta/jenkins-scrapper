from jenkinsapi.jenkins import Jenkins, Jobs


class JobWorkers:

    def __init__(self, server: Jenkins, job_name: object) -> object:
        """
        Constructor to initialize JobWorkers
        :param server: Object of jenkinsapi.jenkins.Jenkins, having valid session
        :param job_name: name of job, str
        """
        self.jenkins_server = server
        self.job_name = job_name

    def get_job_object(self, ):
        """Get a job object
               :return: Job obj
        """
        return self.jenkins_server.get_job(self.job_name)

    def __was_last_build_passes(self):
        return self.jenkins_server.get_job(self.job_name).get_last_build().get_status() == "SUCCESS"

    def should_raise_alarm(self):
        """
        Checks if last build was failed , if so then return True to raise alarm otherwise False
        :return: Boolean
        """
        return not self.__was_last_build_passes()

    def to_string(self):
        """
        Converts Job object to String to show metadata of Job
        :return: string
        """
        job = self.get_job_object()
        string = """ Job Name : %s \n Job Description: %s \n Is Job running: %s \n Is Job enabled: %s""" \
                 % (job.name, job.get_description(), job.is_running(), job.is_enabled())
        return string
