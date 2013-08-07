from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'zora'}

@view_config(route_name='admin', renderer='admin.mako')
def admin_view(request):
     return {'project': 'zora v'}
