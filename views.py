from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatSession, Message, User
from .serializers import MessageSerializer

class ChatAPIView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        message_text = request.data.get('message')

        user = User.objects.get(id=user_id)
        session, _ = ChatSession.objects.get_or_create(user=user)

        Message.objects.create(session=session, sender='user', message=message_text)
        ai_response = "This is a dummy AI response."

        Message.objects.create(session=session, sender='ai', message=ai_response)
        return Response({"response": ai_response})
