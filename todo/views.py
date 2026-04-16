from rest_framework.decorators import api_view
from .serializers import TodoItemSerializer
from .models import TodoItem
from rest_framework.response import Response

@api_view(["GET","POST"])
def handle_todos(request):
    if request.method == "GET":
        todos = TodoItem.objects.all()
        serialized = TodoItemSerializer(todos, many=True)
        return Response(serialized.data)

    elif request.method == "POST":
        serializer = TodoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)