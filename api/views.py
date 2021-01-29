from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from service.models import Order
from .serializers import OrderSerializer


class OrderView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({"orders": serializer.data})


    def post(self, request):
        order = request.data.get('order')

        serializer = OrderSerializer(data=order)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Order created! "})

    def delete(self, request, pk):
        # Get object with this pk
        order = get_object_or_404(Order.objects.all(), pk=pk)
        order.delete()
        return Response({
            "message": "order with id `{}` has been deleted.".format(pk)
        }, status=204)


    # def order_to_json(self, order):
    #     return {
    #         'service_type': order.service_type,
    #         'room_count':order.order.room_count,
    #         'address':order.address,
    #         'order_date':order.order_date,
    #         'date_created':order.date_created,
    #         'user':order.user.id
    #     }
