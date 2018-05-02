#!/usr/local/bin/python3
# coding=utf-8

from lib.sftp_transfer import SftpTransfer
from lib.logger import Logger
from lib.sendmail import send
from config import mail_cfg


def downfile(
    s_username,
    s_password,
    s_host,
    t_username,
    t_password,
    t_host,
    logger_name,
    logger_path,
    s_path=".",
    t_path=".",
    t_backpath=".",
    m_path="."
):
    logger = Logger(logger_name, logger_path)

    try:
        s_sftp = SftpTransfer(
            s_username,
            s_password,
            s_host,
        )
        logger.debug('connect %s@%s source:%s' % (s_username, s_host, s_path))

        t_sftp = SftpTransfer(
            t_username,
            t_password,
            t_host,
        )
        logger.debug('connect %s@%s target:%s backup:%s' % (t_username, t_host, t_path, t_backpath))


        files = s_sftp.listdir(s_path)
        if files:
            logger.debug(",".join(files))
            for file in files:
                s_sftp.get(s_path+file, m_path+file)
                logger.info("download %s" % file)
                t_sftp.put(m_path+file, t_path+file)
                logger.info("move %s" % file)
                s_sftp.remove(s_path+file)
                logger.info("remove %s" % file)
        else:
            logger.info("source:%s has none files" % s_path)

    except Exception as e:   
        logger.error(e)
        send(*mail_cfg, text=unicode(str(e), "utf-8"))


def uploadfile(
    s_username,
    s_password,
    s_host,
    t_username,
    t_password,
    t_host,
    logger_name,
    logger_path,
    s_path=".",
    s_backpath=".",
    t_path=".",
    m_path="."
):
    logger = Logger(logger_name, logger_path)

    try:
        s_sftp = SftpTransfer(
            s_username,
            s_password,
            s_host,
        )
        logger.debug('connect %s@%s source:%s backup:%s' % (s_username, s_host, s_path, s_backpath))

        t_sftp = SftpTransfer(
            t_username,
            t_password,
            t_host,
        )
        logger.debug('connect %s@%s target:%s' % (t_username, t_host, t_path))

        files = s_sftp.listdir(s_path)
        if files:
            logger.debug(",".join(files))
            for file in files:
                s_sftp.get(s_path+file, m_path+file)
                logger.info("upload %s" % file)
                s_sftp.put(m_path+file, s_backpath+file)
                logger.info("backup %s" % file)
                t_sftp.put(m_path+file, t_path+file)
                logger.info("move %s" % file)
                s_sftp.remove(s_path+file)
                logger.info("remove %s" % file)
        else:
            logger.info("source:%s has none files" % s_path)

    except Exception as e:   
        logger.error(e)
        send(*mail_cfg, text=unicode(str(e), "utf-8"))
