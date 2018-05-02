#!/usr/local/bin/python3
# coding=utf-8

from core import *
from config import *


uploadfile(*upload_sftp_cfg, **upload_order_path)
uploadfile(*upload_sftp_cfg, **upload_return_path)
uploadfile(*upload_sftp_cfg, **upload_cancel_path)