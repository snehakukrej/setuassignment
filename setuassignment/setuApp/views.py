from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FetchBill
from .permission import Check_API_KEY_Auth

# Create your views here.


class fetchCustomerBill(APIView):
    permission_classes = (Check_API_KEY_Auth,)
    def get(self, request):
        phone_number = request.data.get('mobileNumber')
        try:
            object = FetchBill.objects.get(mobile = phone_number)
            result = {
                "customerName": object.customer_name,
                "dueAmount": object.due_amount,
                "dueDate": object.due_date,
                "refID": object.ref_id,
            }


        except Exception as exc:
            print(str(exc))
            result = {"message": str(exc)}
            return Response(result, status=404)
        return Response(result, status=200)


class updateCustomerBill(APIView):
    permission_classes = (Check_API_KEY_Auth,)
    def post(self, request):
        ref_id = request.data.get('refID')
        transaction_details = request.data.get('transaction')
        try:
            object = FetchBill.objects.get(ref_id= ref_id)
            object.due_amount = transaction_details.get('amountPaid')
            object.due_date = transaction_details.get('date')
            result = {
                        "status": "SUCCESS",
                        "data": {
                            "ackID": object.ref_id
                        }
                    }

        except Exception as exc:
            print(str(exc))
            result = {"message": str(exc)}
            return Response(result, status=404)
        return Response(result, status=200)






        


