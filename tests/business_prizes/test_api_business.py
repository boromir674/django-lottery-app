import pytest
from rest_framework.reverse import reverse
# from django.shortcuts import reverse


#    model = Business
#         fields = ('id', 'name', 'description', 'email', 'address', 'website')
#
#
# # API
# class BusinessViewset(BaseModelViewSet):
#     serializer_class = BusinessSerializer
#
#     def __get_permissions(self):
#         if self.action in ('list', 'retrieve'):
#             return [AllowAny]
#         if self.action in ('update', 'partial_update', 'create', 'destroy'):
#             return [IsAuthenticated, IsAdminUser]
#
#     def get_queryset(self):
#         if get_user_model().is_staff:  # can access the admin site
#             return Business.objects.all()
#         return Business.objects.get(user=self.request.user)

# @pytest.mark.parametrize('client, method, status_code, data', [
#     ('anonymous', 'get', 401)
# ])
# def test_authorization(clients):
#     pass
#
# def test_public_endpoints20(client_obj):
#     client_obj.get(reverse('auth'))
#
#
# def test_public_endpoints23(client_obj):
#     client_obj.get(reverse('businesses_business'))
#
# def test_public_endpoints(client_obj):
#     client_obj.get(reverse('businesses_businesses'))
#
# def test_public_endpoints0(client_obj):
#     client_obj.get(reverse('business_business'))
#
# def test_public_endpoints1(client_obj):
#     client_obj.get(reverse('business_businesses'))
#
# def test_public_endpoints3(client_obj):
#     client_obj.get(reverse('business_prizes_business'))
#
# def test_public_endpoints2(client_obj):
#     client_obj.get(reverse('business_prizes_businesses'))


@pytest.mark.skip
def test_business_functionality(business_client):

    user = create_user(username=username, password='strong-password')
    client.login()
    client.post(reverse(''))
    # test that a logged in business account can create (POST), edit (PUT), retrieve and list the business resource

    # test that a logged in business account cannot delete (DELETE)

    # test that an anonymous account can retrieve and list the business resource GET

    # test that an anonymous account cannot DELETE, update PUT, create POST,

    # test that an admin can do anything on the resource
