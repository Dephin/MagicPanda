#!/usr/local/bin/python3
# coding=utf-8


mail_cfg = (
    'lee_daily_report@nengmao.net',
    'Yqaz2WSX','huanglin@nengmao.net',
    'smtp.exmail.qq.com',
    'bbsftp'
)

down_sftp_cfg = (
    # Source username,password,host
    "bbmagicpanda", "BBMagPan0214", "ftp.cargofe.com", 
    # Target username,password,host
    "ecargo", "446jvq1", "121.41.172.108", 
    # Log name,filepath
    "bbsftp", "F:/Dephin/nengmao/bbftp/logbbsftp.log"
)

upload_sftp_cfg = (
    # Source username,password,host
    "ecargo", "446jvq1", "121.41.172.108", 
    # Target username,password,host
    "bbmagicpanda", "BBMagPan0214", "ftp.cargofe.com", 
    # Log name,filepath
    "bbsftp", "/data/cron_sftp/log/bbsftp.log"
)


down_ordership_path = {
    's_path': "/PRO/outgoing/Shipment Confirmation/",
    't_path': "/in/OrderShip/",
    't_backpath': "/in/OrderShipBack/",
    'm_path': "/data/cron_sftp/backup/ordership/"
}

down_returnship_path = {
    's_path': "/PRO/outgoing/Return GRN/",
    't_path': "/in/ReturnShip/",
    't_backpath': "/in/ReturnShipBack/",
    'm_path': "/data/cron_sftp/backup/returnship/"
}

down_cancelship_path = {
    's_path': "/PRO/outgoing/Cancellation Response/",
    't_path': "/in/CancalShip/",
    't_backpath': "/in/CancalShipBack/",
    'm_path': "/data/cron_sftp/backup/cancelship/"
}

upload_order_path = {
    's_path': "/out/Order/",
    's_backpath': "/out/OrderBack/",
    't_path': "/PRO/incoming/Sales Order/",
    'm_path': "/data/cron_sftp/backup/order/"
}

upload_return_path = {
    's_path': "/out/Return/",
    's_backpath': "/out/ReturnBack/",
    't_path': "/PRO/incoming/Return Order/",
    'm_path': "/data/cron_sftp/backup/return/"
}

upload_cancel_path = {
    's_path': "/out/Cancal/",
    's_backpath': "/out/CancalBack/",
    't_path': "/PRO/incoming/Order Cancellation/",
    'm_path': "/data/cron_sftp/backup/cancel/"
}

down_inventory_path = {
    's_path': "/PRO/outgoing/Cancellation Response/",
    't_path': "/in/Inventory/",
    't_backpath': "/in/InventoryBack/",
    'm_path': "/data/cron_sftp/backup/inventory/"
}