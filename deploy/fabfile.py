import os
import tempfile
import subprocess
from os.path import join
from fabric import task, Connection

server = "root@49.13.174.94"
deploy = os.path.dirname(os.path.abspath(__file__))


def get_connection():
    return Connection(host=server)


@task
def update_config(c):
    conn = get_connection()
    deploy_path = join(deploy, "supervisord.conf")
    conn.put(deploy_path, "/etc/supervisor/conf.d/", sudo=True)
    conn.sudo("supervisorctl reread")
    conn.sudo("supervisorctl update")


@task
def release(c):
    conn = get_connection()
    remote_folder = "/home/service-gudauri-bot"

    with conn.cd(remote_folder):
        conn.run("git pull")
        conn.run("supervisorctl restart sbot")


@task
def restart(c):
    conn = get_connection()
    conn.run("supervisorctl restart sbot")


@task
def stop(c):
    conn = get_connection()
    conn.run("supervisorctl stop sbot")


@task
def ssh(c):
    subprocess.call(['ssh', server.split(':')[0]])
