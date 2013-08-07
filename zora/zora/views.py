from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'zora'}

@view_config(route_name='admin', renderer='admin.mako')
def admin_view(request):
    return {'project': 'zora'}
    
@view_config(route_name='cql_main', renderer='cql.mako')
def cql_main_view(request):
    from pruga import dotazy
    import os
    cesta = os.path.dirname(dotazy.__file__)
    cypher_skripty = [skript for skript in os.listdir(cesta) if skript.endswith('.cql')]
    return {'project': 'zora',  'cypher_skripty': cypher_skripty}
    
@view_config(route_name='cql')
def cql_view(request):
    from pruga.dotazy import cypher
    cql_skript = request.matchdict['cql']
    cql_kód = cypher(cql_skript)
    
    from pruga.servery.medvěd import cypher as spustím_cypher
    výsledek = spustím_cypher(cql_kód)
    
    from pyramid.response import Response
    return Response('Výsledek {}'.format(výsledek) )

