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

@api_view(["DELETE", "PATCH", "PUT"])
def handle_todos_by_id(request, pk):
    try:
        todo = TodoItem.objects.get(id=pk)
    except TodoItem.DoesNotExist:
        return Response({"message": f"Can't find TodoItem with id {pk}!"})
    
    if request.method == "DELETE":
        todo.delete()
        return Response({"message": f"TodoItem with id {pk} deleted!"})
    
    elif request.method == "PATCH":
        serializer = TodoItemSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serialzer.errors)
    elif request.method == "PUT":
        serializer = TodoItemSerializer(todo, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)