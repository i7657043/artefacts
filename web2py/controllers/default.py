# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import datetime
@auth.requires_login()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    id = auth.user.first_name
    response.flash = T("Our IOT App")
    return locals()

@auth.requires_login()
def view_devices():

    deviceRows = dba(dba.tbl_device.owner==auth.user.id).select()
    for row1 in deviceRows:
        if row1.last_online > datetime.datetime.now()-datetime.timedelta(seconds=10):
            row1.status = "on"
        else:
            row1.status = "off"


    #deviceRows = dba(dba.tbl_device).select()
    return locals()

@auth.requires_login()
def add_devices():
    #grid = SQLFORM.grid(dba.tbl_device, create=True, deletable=True, editable=True, user_signature = False)
    dba.tbl_device.owner.default = auth.user.id
    dba.tbl_device.owner.writable = False
    dba.tbl_device.owner.readable = False
    dba.tbl_device.last_online.writable = False
    dba.tbl_device.last_online.readable = False
    dba.tbl_device.first_online.writable = False
    dba.tbl_device.first_online.readable = False
    dba.tbl_device.device_temp.writable = False
    dba.tbl_device.device_temp.readable = False
    dba.tbl_device.ambient_temp.writable = False
    dba.tbl_device.ambient_temp.readable = False
    dba.tbl_device.internal_temp.writable = False
    dba.tbl_device.internal_temp.readable = False
    dba.tbl_device.lumens.writable = False
    dba.tbl_device.lumens.readable = False
    dba.tbl_device.decibels.writable = False
    dba.tbl_device.decibels.readable = False
    dba.tbl_device.status.writable = False
    dba.tbl_device.status.readable = False
    dba.tbl_device.battery.writable = False
    dba.tbl_device.battery.readable = False

    add_form = SQLFORM(dba.tbl_device)
    if add_form.process().accepted:
        response.flash = 'form accepted'
        redirect(URL('index'))

    elif add_form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return locals()

@auth.requires_login()
def dev_management():
    dba.tbl_device.owner.writable = False
    dba.tbl_device.owner.readable = False
    dba.tbl_device.last_online.writable = False
    dba.tbl_device.last_online.readable = True
    dba.tbl_device.first_online.writable = False
    dba.tbl_device.first_online.readable = True
    dba.tbl_device.device_temp.writable = False
    dba.tbl_device.device_temp.readable = False
    dba.tbl_device.ambient_temp.writable = False
    dba.tbl_device.ambient_temp.readable = False
    dba.tbl_device.internal_temp.writable = False
    dba.tbl_device.internal_temp.readable = False
    dba.tbl_device.lumens.writable = False
    dba.tbl_device.lumens.readable = False
    dba.tbl_device.decibels.writable = False
    dba.tbl_device.decibels.readable = False
    dba.tbl_device.status.writable = False
    dba.tbl_device.status.readable = True
    dba.tbl_device.battery.writable = False
    dba.tbl_device.battery.readable = False
    
    grid = SQLFORM.grid(auth.user.id==dba.tbl_device.owner, fields=[dba.tbl_device.device_name, dba.tbl_device.id], formstyle = 'table3cols');
    return locals()

@auth.requires_login()
def selected_device():
    selected_device = dba.tbl_device(request.args(0))

    if selected_device.last_online > datetime.datetime.now()-datetime.timedelta(seconds=10):
        selected_device.status = "on"
    else:
        selected_device.status = "off"

    dict1 = dba.executesql("SELECT device_temp FROM tbl_readings WHERE device_id="+request.args(0)+" ORDER BY timestamp DESC LIMIT 20;", as_dict = True)
    dict2 = dba.executesql("SELECT ambient_temp FROM tbl_readings WHERE device_id="+request.args(0)+" ORDER BY timestamp DESC LIMIT 20;", as_dict = True)
    dict3 = dba.executesql("SELECT internal_temp FROM tbl_readings WHERE device_id="+request.args(0)+" ORDER BY timestamp DESC LIMIT 20;", as_dict = True)
    dict4 = dba.executesql("SELECT battery FROM tbl_readings WHERE device_id="+request.args(0)+" ORDER BY timestamp DESC LIMIT 20;", as_dict = True)

    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
