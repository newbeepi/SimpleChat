from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Message, Thread
from .serializers import MessageSerializer, ThreadSerializer

User = get_user_model()


class ThreadList(APIView):
    def post(self, request):
        user1_username = request.data.get('user1')
        user2_username = request.data.get('user2')
        user1 = User.objects.get(username=user1_username)
        user2 = User.objects.get(username=user2_username)
        thread = Thread.objects.filter(participants=user1).filter(participants=user2).first()
        if not thread:
            thread = Thread.objects.create()
            thread.participants.set([user1, user2])
            thread.save()
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)


class ThreadDetail(APIView):
    def delete(self, request, pk):
        thread = Thread.objects.get(pk=pk)
        thread.delete()
        return Response("Thread successfully deleted!")


class UserThreadDetail(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        threads = Thread.objects.filter(participants=user)
        serializer = ThreadSerializer(threads, many=True)
        return Response(serializer.data)


def save_message(message, thread):
    message["thread"] = thread.pk
    serializer = MessageSerializer(data=message)
    serializer.is_valid()
    serializer.save()
    return serializer.data


class MessageThreadList(APIView):
    def get(self, request, pk):
        thread = Thread.objects.get(pk=pk)
        serializer = MessageSerializer(thread.messages, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        thread = Thread.objects.get(pk=pk)
        messages = request.data.get("messages")
        res = []
        for message in messages:
            res.append(save_message(message, thread))
        return Response(res)


class MessageDetail(APIView):
    def post(self, request):
        messages_ids = request.data.get("messages_ids")
        print(messages_ids)
        messages = Message.objects.filter(Q(id__in=messages_ids))
        for message in messages:
            message.is_read = True
            message.save()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


class UserMessageList(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        count = user.messages.filter(is_read=False).count()
        return Response({"unread messages count": count})
