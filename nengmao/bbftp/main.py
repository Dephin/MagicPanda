#!/usr/local/bin/python3
# coding=utf-8

from core import *
from config import *


downfile(*down_sftp_cfg, **down_ordership_path)
downfile(*down_sftp_cfg, **down_returnship_path)
downfile(*down_sftp_cfg, **down_cancelship_path)


uploadfile(*upload_sftp_cfg, **upload_order_path)
uploadfile(*upload_sftp_cfg, **upload_return_path)
uploadfile(*upload_sftp_cfg, **upload_cancel_path)