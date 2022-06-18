from django.http import JsonResponse
from blog.models import Questions
from .serializers import QuestionSerializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['get',])
def votingData(request):
	questions = Questions.objects.all()
	frontend = Questions.objects.filter(answer='frontend').count()
	print(frontend)
	backend = Questions.objects.filter(answer='backend').count()
	print(backend)
	fullstack = Questions.objects.filter(answer='fullstack').count()
	print(fullstack)
	# serializers  = QuestionSerializers(questions, many=True)
	return Response({
				'frontend':frontend,
				'backend' : backend,
				'fullstack':fullstack,
			})