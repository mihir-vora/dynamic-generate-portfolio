from rest_framework import serializers
from blog.models import Questions



class QuestionSerializers(serializers.ModelSerializer):
	class Meta:
		model = Questions
		fields = '__all__'