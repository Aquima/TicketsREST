from ticket.models import Ticket

from ticket.serializer import TicketSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
class TicketListAPI(APIView):
    def get(self,request):
        ticket = Ticket.objects.all()
        serializer = TicketSerializer(ticket, many=True)
        serialized_tickets = serializer.data
        return Response(serialized_tickets)



