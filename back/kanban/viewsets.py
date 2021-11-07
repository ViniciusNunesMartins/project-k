from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Dashboard, Board, Card
from .serializers import DashboardSerializer, BoardSerializer, CardSerializer, UserSerializer


class DashboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Dashboard.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def boards(self, request, pk=None):
        boards = Board.objects.filter(dashboard=pk)
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)


class BoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Board.objects.filter(dashboard=self.request.user.dashboard.id)

    def perform_create(self, serializer):
        serializer.save(dashboard=self.request.user.dashboard)

    @action(detail=True, methods=['get'])
    def cards(self, request, pk=None):
        cards = Card.objects.filter(board=pk)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Card.objects.filter(board=self.request.user.board.id)

    def perform_create(self, serializer):
        serializer.save(board=self.request.user.board)

    @action(detail=True, methods=['get'])
    def users(self, request, pk=None):
        users = Card.objects.filter(card=pk)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)