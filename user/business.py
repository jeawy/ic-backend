import json
import traceback
import logging
from django.http import JsonResponse
from .models import User

logger = logging.getLogger(__name__)

def error(message):
    return JsonResponse({'error': message}, status=400)

def get_all_request():
    user = list(User.objects.values())
    return user

def get_request(pk):
    try:
        user = User.objects.get(pk=pk)
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'department': user.department,
            'role': user.role,
        }
    except User.DoesNotExist:
        return {'error': 'user not found'}
    except Exception as e:
        logger.error(traceback.format_exc())
        return error(message=str(e))


def post_request(request_body):
    try:
        data = json.loads(request_body)
        # Create a new user using the valid company instance
        user = User.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            department=data.get('department'),
            role = data.get('role')
        )

        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'department': user.department,
            'role': user.role,
        }
    except Exception as e:
        logger.error(traceback.format_exc())
        return error(message=str(e))

def put_request(pk, request_body):
    try:
        data = json.loads(request_body)

        user = User.objects.get(pk=pk)
        user.name = data.get('name'),
        user.email = data.get('email'),
        user.phone = data.get('phone'),
        user.department = data.get('department'),
        user.role = data.get('role')
        user.save()

        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'department': user.department,
            'role': user.role,
        }
    except User.DoesNotExist:
        return {'error': 'user not found'}
    except Exception as e:
        logger.error(traceback.format_exc())
        return error(message=str(e))

def patch_request(pk, request_body):
    try:
        user = User.objects.get(pk=pk)
        data = json.loads(request_body)
        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email= data['email']
        if 'phone' in data:
            user.phone = data['phone']
        if 'department' in data:
            user.department = data['department']
        if 'role' in data:
            user.role = data['role']
        user.save()
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'department': user.department,
            'role': user.role,
        }
    except User.DoesNotExist:
        return {'error': 'user not found'}
    except Exception as e:
        logger.error(traceback.format_exc())
        return error(message=str(e))

def delete_request(pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return {'message': 'user deleted successfully'}
    except User.DoesNotExist:
        return {'error': 'user not found'}
    except Exception as e:
        logger.error(traceback.format_exc())
        return error(message=str(e))