from jenkinsapi.jenkins import Jenkins
from src.properties_util import PropertyUtil


class JenkinsServer:
    jenkins_server = None

    def __connect__(self):
        if JenkinsServer.jenkins_server is None:
            JenkinsServer.jenkins_server = Jenkins(baseurl=PropertyUtil().get('jenkins_config', 'jenkins.url'),
                                                   username=PropertyUtil().get('jenkins_config', 'jenkins.username'),
                                                   password=PropertyUtil().get('jenkins_config','jenkins.api.token'))
        return JenkinsServer.jenkins_server

    def get_server(self):
        return self.__connect__()
