import shlex
import subprocess
import os

# execute shell command
def exec_cmd(cmd):
    tokens = shlex.split(cmd)
    subprocess.run(tokens)

# using for return command from command
# delete new line
def get_cmd_stdout(cmd):
    tokens = shlex.split(cmd)
    tokens = subprocess.run(tokens, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return tokens.stdout.decode("utf8").replace('\n','')

# get repository name
REPO_APP = 'aws ecr describe-repositories --repository-names app --output text --query "repositories[0].repositoryUri"'
REPO_APP = get_cmd_stdout(REPO_APP)
REPO_WEB = 'aws ecr describe-repositories --repository-names web --output text --query "repositories[0].repositoryUri"'
REPO_WEB = get_cmd_stdout(REPO_WEB)

if __name__ == "__main__":
    # build flask,uwsgi and python that is Dockerfile
    build_app = 'docker build -t {}:latest ./dockerfiles/app/'.format(REPO_APP)
    exec_cmd(build_app)

    # nginx that is Dockerfile
    build_web = 'docker build -t {}:latest ./dockerfiles/nginx/'.format(REPO_WEB)
    exec_cmd(build_web)

    # pushing image to ecr
    for repo in [REPO_APP, REPO_WEB]:
        push_image = 'docker push {}:latest'.format(repo)
        exec_cmd(push_image)
