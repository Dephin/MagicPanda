configs = {

    'db': {
        'host':'121.41.164.58',
        'user':'sd89ynd0922bs',
        'passwd':'rM93fr40O3pl1',
        'db':'efast'
        }  

}


sql = {
    
    'hello': 
        """
        SELECT a.return_sn,a.deal_code,cast(a.confirm_time as CHAR),
        CASE WHEN b.wms_order_time=0 THEN ''
        ELSE FROM_UNIXTIME(b.wms_order_time) end
        from order_return a
        LEFT JOIN api_wms_trade b on a.return_sn=b.order_sn
        WHERE a.sd_id='40' and a.return_order_status<>3 and a.confirm_time is not null
            and FROM_UNIXTIME(a.add_time)>='{start_date}' and FROM_UNIXTIME(a.add_time)<='{end_date}';
        """
}