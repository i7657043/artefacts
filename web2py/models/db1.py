# -*- coding: utf-8 -*-

dba = DAL('mysql://dev:uni123@localhost/devicemanager')

dba.define_table('tbl_device', Field('device_name', 'string'),  Field('first_online', 'datetime'), Field('last_online', 'datetime'), Field('owner', 'string'), Field('device_temp', 'string'), Field('ambient_temp', 'string'), Field('internal_temp', 'string'), Field('lumens', 'string'), Field('decibels', 'string'), Field('status', 'string'), Field('battery', 'string'), Field('owner','reference auth_user'), migrate=False)

dba.define_table('tbl_readings', Field('device_temp', 'string'), Field('ambient_temp', 'string'), Field('internal_temp', 'string'), Field('lumens', 'string'), Field('decibels', 'string'), Field('status', 'string'), Field('battery', 'string'), Field('timestamp', 'datetime', requires=IS_NOT_EMPTY()), Field('device_id','bigint'), migrate=False)
