import json
import traceback
from django.http import JsonResponse
from .models import Broker
from company.models import Company

def get_all_request():
    broker = list(Broker.objects.values())
    return broker

def get_request(pk):
    try:
        broker = Broker.objects.get(pk=pk)
        return {
            'id': broker.id,
            'first_name': broker.first_name,
            'last_name': broker.last_name,
            'email': broker.email,
            'phone': broker.phone,
            'address': broker.address,
            'company': broker.company.id,
            'license_no': broker.license_no,
            'license_issued_date': str(broker.license_issued_date),
            'status': broker.status
        }
    except Broker.DoesNotExist:
        return {'error': 'Broker not found'}
    except Exception:
        return {'error': traceback.format_exc()}


def post_request(request_body):
    try:
        data = json.loads(request_body)

        # Validate that company_id is provided
        company_id = data.get('company_id')
        if not company_id:
            return {'error': 'company_id is required'}

        # Ensure the company with the provided ID exists
        try:
            company = Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            return {'error': 'Company not found'}

        # Create a new broker using the valid company instance
        broker = Broker.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            phone=data.get('phone'),
            address=data.get('address'),
            company=company,  # Assign the company instance
            license_no=data.get('license_no'),
            license_issued_date=data.get('license_issued_date'),
            status = data.get('status')
        )

        return {
            'id': broker.id,
            'first_name': broker.first_name,
            'last_name': broker.last_name,
            'email': broker.email,
            'phone': broker.phone,
            'address': broker.address,
            'company': broker.company.id,
            'license_no': broker.license_no,
            'license_issued_date': str(broker.license_issued_date),
            'status': broker.status
        }
    except Exception:
        return {'error': traceback.format_exc()}

def put_request(pk, request_body):
    try:
        data = json.loads(request_body)
        company_id = data.get('company_id')
        if not company_id:
            return {'error': 'company_id is required'}

        # Ensure the company with the provided ID exists
        try:
            company = Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            return {'error': 'Company not found'}

        broker = Broker.objects.get(pk=pk)
        broker.first_name = data.get('first_name')
        broker.last_name = data.get('last_name')
        broker.email = data.get('email')
        broker.phone = data.get('phone')
        broker.address = data.get('address')
        broker.company = company
        broker.license_no = data.get('license_no')
        broker.license_issued_date = data.get('license_issued_date')
        broker.status = data.get('status')
        broker.save()

        return {
            'id': broker.id,
            'first_name': broker.first_name,
            'last_name': broker.last_name,
            'email': broker.email,
            'phone': broker.phone,
            'address': broker.address,
            'company': broker.company.id,
            'license_no': broker.license_no,
            'license_issued_date': str(broker.license_issued_date),
            'status': broker.status
        }
    except Broker.DoesNotExist:
        return {'error': 'Broker not found'}
    except Exception:
        return {'error': traceback.format_exc()}

def patch_request(pk, request_body):
    try:
        broker = Broker.objects.get(pk=pk)
        data = json.loads(request_body)
        if 'first_name' in data:
            broker.first_name = data['first_name']
        if 'last_name' in data:
            broker.last_name = data['last_name']
        if 'email' in data:
            broker.email = data['email']
        if 'phone' in data:
            broker.phone = data['phone']
        if 'address' in data:
            broker.address = data['address']
        if 'company_id' in data:
            broker.company_id = data['company_id']
        if 'license_no' in data:
            broker.license_no = data['license_no']
        if 'license_issued_date' in data:
            broker.license_issued_date = data['license_issued_date']
        if 'status' in data:
            broker.status = data['status']
        broker.save()
        return {
            'id': broker.id,
            'first_name': broker.first_name,
            'last_name': broker.last_name,
            'email': broker.email,
            'phone': broker.phone,
            'address': broker.address,
            'company': broker.company.id,
            'license_no': broker.license_no,
            'license_issued_date': str(broker.license_issued_date),
            'status': broker.status
        }
    except Broker.DoesNotExist:
        return {'error': 'Broker not found'}
    except Exception:
        return {'error': traceback.format_exc()}

def delete_request(pk):
    try:
        broker = Broker.objects.get(pk=pk)
        broker.delete()
        return {'message': 'Broker deleted successfully'}
    except Broker.DoesNotExist:
        return {'error': 'Broker not found'}
    except Exception:
        return {'error': traceback.format_exc()}