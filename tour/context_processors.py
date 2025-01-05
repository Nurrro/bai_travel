from django.conf import settings

def canonical_url_processor(request):
    return {'canonical_url': request.build_absolute_uri()}
