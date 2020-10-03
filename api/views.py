from django.shortcuts import render

# Create your views here.
import json, math
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializers, KitSerializers
from .models import Product, Kit, KitProducts
from rest_framework import viewsets

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsAuthenticated]


class KitsViewSet(viewsets.ModelViewSet):

    queryset = Kit.objects.all()
    serializer_class = KitSerializers
    permission_classes = [IsAuthenticated]

    def create(self, request):

        kit_json = json.loads(request.body)
        products_json = kit_json.pop('products', None)
        products = []

        try:
            if len(products_json) > 2:
                for product in products_json:
                    products.append(KitProducts.objects.create(
                        sku           =  product["sku"],
                        quantity      =  product["quantity"],
                        discount      =  product["discount"],
                    ))
            else:
                return JsonResponse({'message': "O kit precisa de 2 ou mais produtos para o cadastro"}, status=status.HTTP_200_OK)


            kit = Kit.objects.create(
                kit_name=   kit_json["kit_name"],
                kit_sku=    kit_json["kit_sku"],
            )

            kit.products.set(products)
            serializer = KitSerializers(kit)

            return JsonResponse({'kit': serializer.data}, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': "Cannot possible create this kit"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk):

        kit_json = json.loads(request.body)
        products = kit_json.pop('products', None)

        try:
            kit = Kit.objects.filter(id=pk)
            kit.update(**kit_json)

            if products is not None:
                for product in products:
                    if product.get('id'):
                        kit_products = KitProducts.objects.get(pk=product['id'], kit=kit[0])
                        kit_products.sku      = product['sku']
                        kit_products.quantity = product['quantity']
                        kit_products.discount = product['discount']
                        kit_products.save()
                    else:
                        KitProducts.objects.create(kit=kit[0], **product)

            kit = Kit.objects.get(pk=pk)
            serializer = KitSerializers(kit)

            return JsonResponse({'kit': serializer.data}, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': "Cannot possible create this kit"}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['get'], url_path='kits-calculation')
    def kits_calculation(self, request, pk):
        kit_calculation = {}
        kits_products = []
        kits = Kit.objects.filter(pk=pk)
        kit_stock = list()
        kit_cost  = 0
        kit_price = 0


        for kit in kits:
            kit_calculation['kit_name'] = kit.kit_name
            kit_calculation['sku'] = kit.kit_sku

            for product in kit.products.all():

                prod = Product.objects.get(sku=product.sku)
                kit_stock.append(math.floor(prod.stock / product.quantity if product.quantity > 0 else 1))
                kit_cost += prod.cost
                kit_price += prod.discount_price(product.discount)

        kit_stock = min(kit_stock)

        kit_calculation.update({
            'price': kit_price,
            'cost': kit_cost,
            'stock': kit_stock,
        })
        return JsonResponse({'kit_calculation': kit_calculation}, status=status.HTTP_201_CREATED)
