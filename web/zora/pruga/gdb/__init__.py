from django.conf import settings
if not settings.NEO4J_DATABASES:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured('You must configure a Neo4j database to use Neo4j models.')
    
print(settings.NEO4J_DATABASES) 
