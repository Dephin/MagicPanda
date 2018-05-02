#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright (c) 2018
"""


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

import smtplib

def send(
    from_addr, password, to_addr, 
    smtp_server, subject, 
    text="", from_nick="", to_nick=""
):

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'%s <%s>' % (from_nick,from_addr))
    msg['To'] = _format_addr(u'%s <%s>' % (to_nick,to_addr))
    msg['Subject'] = Header(u'%s' % subject, 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(0)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()