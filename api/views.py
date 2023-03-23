from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    developer = {'name':'Gabriel Costa Soares', 'age': 34, 'course' : 'Backend Python', 'country':'Germany', 'school' : 'EBAC Sao Paulo'}
    return Response(developer)