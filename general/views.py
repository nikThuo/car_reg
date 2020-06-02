from django.shortcuts import render
from users.models import Users
from vehicle_registration.models import Vehicles, Owner
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import json


# Create your views here.
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def participants(request):
    authority = Users.objects.filter(user_type=1).values()
    agent = Users.objects.filter(user_type=2).values()
    owner = Users.objects.filter(user_type=3).values()

    # parts = {'peer1_Authority': authority,
    #          'peer2_Agent': agent,
    #          'peer3_Owner': owner
    #          }
    parts = {'peer1_Authority': 'Authority',
             'peer2_Agent': 'Agent',
             'peer3_Owner': 'Owner'
             }

    return Response(parts)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def assets(request):
    asset = Vehicles.objects.all().values()
    return Response(asset)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def transactions(request):
    trxs = Owner.objects.filter(vehicle_status='owned').values()
    print('Transactions------>', trxs)
    owner = []
    for trx in trxs:
        print('Trx------>', trx['reg_id'])
        p_owns = Owner.objects.filter(reg_id=trx['reg_id'], vehicle_status='transferred').values()
        pr_owner = []
        for p in p_owns:
            p_own = {'transaction_id': p['transaction_id'], 'owner_name': p['fullname'], 'owner_id': p['national_id'], 'owner_phone': p['mobile'],
                     'owner_email': p['email'], 'vehicle_status': p['vehicle_status']}
            pr_owner.append(p_own)
            print('Tr------>', pr_owner)
            # return pr_owner
        own = {'transaction_id': trx['transaction_id'], 'vehicle_reg_no': trx['reg_id'], 'vehicle_make': trx['make'], 'vehicle_model': trx['vehicle_model'],
               'vehicle_type': trx['vehicle_type'], 'year_of_manufacture': trx['year_of_manufacture'], 'owner_name': trx['fullname'],
               'owner_id': trx['national_id'], 'owner_phone': trx['mobile'], 'owner_email': trx['email'], 'owner_pin': trx['pin'],
               'vehicle_status': trx['vehicle_status'], 'hash': trx['hash'], 'previous_hash': trx['previous_hash'], 'timestamp': trx['timestamp'],
               'previous_owner': pr_owner}
        # print('Owner------->', own)
        owner.append(own)
        print('Owner------->', owner)
    return Response(owner)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def ledger(request):
    ledgers = []
    ledge = {'assets': '/assets',
             'participants': '/participants',
             'transactions': '/transactions'
             }
    ledgers.append(ledge)
    return Response(ledgers)

@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def user_vehicles(request):
    vechs = Owner.objects.filter(national_id=request.data['id'], vehicle_status='owned').values()
    vehicles = []

    if vechs:
        for vech in vechs:
            vehicle = {'vehicle_make': vech['make'], 'vehicle_type': vech['vehicle_type'], 'vehicle_model': vech['vehicle_model'],
                       'vehicle_no': vech['reg_id']}
            vehicles.append(vehicle)

        return Response(vehicles)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def user_vehicle_history(request):
    vechs = Owner.objects.filter(reg_id=request.data['reg_no'], vehicle_status='transferred').values()
    vehicles = []

    if vechs:
        for vech in vechs:
            vehicle = {'previous_owner_name': vech['fullname'], 'previous_owner_mobile': vech['mobile'],
                       'previous_owner_email': vech['email']}
            vehicles.append(vehicle)

        return Response(vehicles)
    return Response(status=status.HTTP_400_BAD_REQUEST)