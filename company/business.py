import json
import traceback

from django.http import JsonResponse
from .models import Company

def get_all_request():
    companies = list(Company.objects.values())
    return companies

def get_request(pk):
    try:
        company = Company.objects.get(pk=pk)
        return {
            'id': company.id,
            'name': company.name,
            'address': company.address,
            'phone': company.phone,
            'email': company.email,
            'status': company.status
        }
    except Company.DoesNotExist:
        return {'error': 'Company not found'}
    except Exception:
        return {'error': traceback.format_exc()}

def post_request(request_body):
    try:
        data = json.loads(request_body)
        company = Company.objects.create(
            name=data.get('name'),
            address=data.get('address'),
            phone=data.get('phone'),
            email=data.get('email'),
            status=data.get('status')
        )
        return {
            'id': company.id,
            'name': company.name,
            'address': company.address,
            'phone': company.phone,
            'email': company.email,
            'status': company.status
        }
    except Exception:
        return {'error': traceback.format_exc()}

def put_request(pk, request_body):
    try:
        company = Company.objects.get(pk=pk)
        data = json.loads(request_body)
        company.name = data.get('name', company.name)
        company.address = data.get('address', company.address)
        company.phone = data.get('phone', company.phone)
        company.email = data.get('email', company.email),
        company.status = data.get('status', company.status)
        company.save()
        return {
            'id': company.id,
            'name': company.name,
            'address': company.address,
            'phone': company.phone,
            'email': company.email,
            'status': company.status
        }
    except Company.DoesNotExist:
        return {'error': 'Company not found'}
    except Exception:
        return {'error': traceback.format_exc()}

def patch_request(pk, request_body):
    try:
        company = Company.objects.get(pk=pk)
        data = json.loads(request_body)
        # Only update the fields provided in the request
        if 'name' in data:
            company.name = data['name']
        if 'address' in data:
            company.address = data['address']
        if 'phone' in data:
            company.phone = data['phone']
        if 'email' in data:
            company.email = data['email']
        if 'status' in data:
            company.status = data['status']
        company.save()
        return {
            'id': company.id,
            'name': company.name,
            'address': company.address,
            'phone': company.phone,
            'email': company.email,
            'status': company.status
        }
    except Company.DoesNotExist:
        return {'error': 'Company not found'}
    except Exception:
        return {'error': traceback.format_exc()}

def delete_request(pk):
    try:
        company = Company.objects.get(pk=pk)
        company.delete()
        return {'message': 'Deleted successfully'}
    except Company.DoesNotExist:
        return {'error': 'Company not found'}
    except Exception:
        return {'error': traceback.format_exc()}
