from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password


# Create your views here.

class ProvinceView(APIView):
    provinces = Province.objects.all()
    serializer_class = ProvinceSerializer

    def get(self, request, **kwargs):
        provinces = Province.objects.all()
        serializer = ProvinceSerializer(provinces, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        province_name = request.POST.get('province_name')
        code_province = request.POST.get('code_province')
        Province.objects.create(province_name=province_name, code_province=code_province)
        return Response({'message': 'Province cree avec success.'}, status=status.HTTP_201_CREATED)


class DepartmentView(APIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self, request, **kwargs):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        department_name = request.POST.get('department_name')
        province = request.POST.get('province')
        Department.objects.create(department_name=department_name, province_id=province)
        return Response({'message': 'Departement cree avec success.'}, status=status.HTTP_201_CREATED)


class MunicipalityView(APIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, **kwargs):
        municipalities = Municipality.objects.all()
        serializer = MunicipalitySerializer(municipalities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        municipality_name = request.POST.get('municipality_name')
        department = request.POST.get('department')
        Municipality.objects.create(municipality_name=municipality_name, department_id=department)
        return Response({'message': 'Commune cree avec success.'}, status=status.HTTP_201_CREATED)


class ShopView(APIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, **kwargs):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        shop_name = request.POST.get('shop_name')
        shop_description = request.POST.get('shop_description')
        municipality = request.POST.get('municipality')
        shop_address = request.POST.get('shop_address')
        shop_location = request.POST.get('shop_location')
        shop_logo = request.FILES.get('shop_logo')
        shop_backdrop = request.FILES.get('shop_backdrop')
        Shop.objects.create(shop_name=shop_name, shop_description=shop_description, shop_address=shop_address,
                            shop_location=shop_location, shop_logo=shop_logo, shop_backdrop=shop_backdrop,
                            municipality_id=municipality)
        return Response({'message': 'Magasin cree avec success.'}, status=status.HTTP_201_CREATED)


class ShopByIdView(APIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, **kwargs):
        shops = Shop.objects.filter(pk=kwargs['pk']).first()
        serializer = ShopSerializer(shops)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        shop_name = request.POST.get('shop_name')
        shop_description = request.POST.get('shop_description')
        municipality = request.POST.get('municipality')
        shop_address = request.POST.get('shop_address')
        shop_location = request.POST.get('shop_location')
        shop_logo = request.FILES.get('shop_logo')
        shop_backdrop = request.FILES.get('shop_backdrop')
        Shop.objects.create(shop_name=shop_name, shop_description=shop_description, shop_address=shop_address,
                            shop_location=shop_location, shop_logo=shop_logo, shop_backdrop=shop_backdrop,
                            municipality_id=municipality)
        return Response({'message': 'Magasin cree avec success.'}, status=status.HTTP_201_CREATED)


class ShelveView(APIView):
    queryset = Shelve.objects.all()
    serializer_class = ShelveSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, **kwargs):
        shelves = Shelve.objects.all()
        serializer = ShelveSerializer(shelves, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        shelve_name = request.POST.get('shelve_name')
        shelve_description = request.POST.get('shelve_description')
        Shelve.objects.create(shelve_name=shelve_name, shelve_description=shelve_description)
        return Response({'message': 'Rayon crée avec success.'}, status=status.HTTP_201_CREATED)


class ProductView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_image = request.FILES.get('product_image')
        product_promotion_price = request.POST.get('product_promotion_price')
        Product.objects.create(product_name=product_name, product_description=product_description,
                               product_image=product_image)
        return Response({'message': 'Produit crée avec success.'}, status=status.HTTP_201_CREATED)


class ShopShelveView(APIView):
    queryset = ShopShelve.objects.all()
    serializer_class = ShopShelveSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, **kwargs):
        shop_shelves = ShopShelve.objects.all()
        serializer = ShopShelveSerializer(shop_shelves, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        shop = request.POST.get('shop')
        shelve = request.POST.get('shelve')
        ShopShelve.objects.create(shop_id=shop, shelve_id=shelve)
        return Response({'message': 'Rayon atribué crée avec success.'}, status=status.HTTP_201_CREATED)


class ShelvesByShopView(APIView):
    queryset = ShopShelve.objects.all()
    serializer_class = ShopShelveSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, **kwargs):
        shop_shelves = ShopShelve.objects.filter(shop_id=kwargs['shop_id']).all()
        serializer = ShopShelveSerializer(shop_shelves, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        shop = request.POST.get('shop')
        shelve = request.POST.get('shelve')
        ShopShelve.objects.create(shop_id=shop, shelve_id=shelve)
        return Response({'message': 'Rayon atribué crée avec success.'}, status=status.HTTP_201_CREATED)


class ShelveProductView(APIView):
    queryset = ShelveProduct.objects.all()
    serializer_class = ShelveProductSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, **kwargs):
        shelve_products = ShelveProduct.objects.all()
        serializer = ShelveProductSerializer(shelve_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        product = request.POST.get('product')
        shop_shelve = request.POST.get('shop_shelve')
        product_price = request.POST.get('product_price')
        ShelveProduct.objects.create(product_id=product, shop_shelve_id=shop_shelve, product_price=product_price)
        return Response({'message': 'Produit atribué crée avec success.'}, status=status.HTTP_201_CREATED)


class ShelveProductByShopView(APIView):
    queryset = ShelveProduct.objects.all()
    serializer_class = ShelveProductSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, **kwargs):
        shelve_products = ShelveProduct.objects.filter(shop_shelve_id=kwargs['id']).all()
        serializer = ShelveProductSerializer(shelve_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        product = request.POST.get('product')
        shop_shelve = request.POST.get('shop_shelve')
        product_price = request.POST.get('product_price')
        ShelveProduct.objects.create(product_id=product, shop_shelve_id=shop_shelve, product_price=product_price)
        return Response({'message': 'Produit atribué crée avec success.'}, status=status.HTTP_201_CREATED)


class RoleView(APIView):
    queryset = UserRole.objects.all()
    serializer_class = RoleSerializer

    def get(self, request, **kwargs):
        clients = UserRole.objects.all()
        serializer = RoleSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.POST)
        role_value = request.POST.get('role_value')
        UserRole.objects.create(role_value=role_value)
        return Response({'message': 'Compte client crée avec success.'}, status=status.HTTP_201_CREATED)


class ClientView(APIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.POST)
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        municipality = request.POST.get('municipality')
        quarter = request.POST.get('quarter')
        address = request.POST.get('address')
        user_account = AppUser.objects.create_user(email=email, password=password, username=name, role_id=2,
                                                   is_staff=True, is_active=True, phone=phone)
        Client.objects.create(name=name, surname=surname, email=email, phone=phone, municipality_id=municipality,
                              quarter=quarter, address=address, user=user_account)
        return Response({'message': 'Compte client crée avec success.'}, status=status.HTTP_201_CREATED)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)

    # authentication_classes = (TokenAuthentication,)

    ##
    def post(self, request):
        data = request.data
        print(data)
        # assert validate_email(data)
        # assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                new_serializer = UserSerializer(user)
                print(new_serializer.data)
                response = {"user": new_serializer.data, "token": token.key, "status": status.HTTP_200_OK}
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response({"status": status.HTTP_205_RESET_CONTENT}, status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response({"status": status.HTTP_303_SEE_OTHER}, status=status.HTTP_303_SEE_OTHER)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
