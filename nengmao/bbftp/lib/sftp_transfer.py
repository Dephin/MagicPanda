#!/usr/local/bin/python3
# coding=utf-8


from paramiko import Transport, SFTPClient


class SftpTransfer(Transport):
    def __new__(
        cls,
        username = "",
        password = "",
        host = "",
        port = 22 
    ):  
        """
        :function .put(local, remote):
        :function .get(local, remote):
        :function .open(remote, 'wx'):
            Return a file instance.
        :function .rmdir(remote):
        :function .chdir(path=None):
            Change the "current directory".
        :function .listdir(path="."):
        :function .getcwd():
        """
        transport = super(SftpTransfer, cls).__new__(cls)
        transport.__init__( (host, port) )
        transport.connect(\
            username=username, password=password)
        sftp = SFTPClient.from_transport(transport)
        return sftp

    def __del__(sftp):
        sftp.close()