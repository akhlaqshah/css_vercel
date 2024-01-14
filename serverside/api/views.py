from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from  .models import Subject, Quiz, QuizNew, Result, AppUser


# Create your views here.

invalid_request = "Invalid request method";
user_id_not_found = "user id not found"

@api_view(['GET'])
def get_subjects(request):
    body = request.body
    print(body)
    subjects = Subject.objects.all()

    
    return JsonResponse(list(subjects.values()), safe=False)

@api_view(['GET'])
def get_all_quizes(request):
    print(request.body)
    quizzes = Quiz.objects.using('quiz_db').all()
    QuizNew.objects.bulk_create([QuizNew(**data) for data in list(quizzes.values())])
    
    """ for source_document in quizzes:
        # Create a new instance with the same data
        
        source_document_data = {key: value for key, value in source_document.__dict__.items() if key != '_state'}
        print(source_document_data)
        destination_document = Quiz(**source_document_data)
        destination_document._meta.db_table = 'quizzes'


        # Save the document to the destination collection
        destination_document.save() """

    
    return JsonResponse(list(quizzes.values()), safe=False)

@api_view(['GET'])
def get_questions(request):
    print(request.body)
    if request.method == 'GET':
        if request.GET.get('quizId') != None:
            questions = Quiz.objects.filter(quizId=request.GET.get('quizId'))
            return JsonResponse({'questions': list(questions.values()), 'error': None})
        else:
            return JsonResponse({'error': "quiz id not found", 'questions':[]})
    else:    
        return JsonResponse({'error': invalid_request, 'questions': []})

@api_view(['GET'])
def get_results(request):
    print(request.body)
    if request.method == 'GET':
        if request.GET.get('userId') != None:
            results = Result.objects.filter(quizId=request.GET.get('userId'))
            # results = Result.objects.all()
            return JsonResponse({'results': list(results.values()), 'error': None})
        else:
            return JsonResponse({'error': user_id_not_found, 'results':[]})
    else:    
        return JsonResponse({'error': invalid_request, 'results': []})

@api_view(['GET'])
def get_users(request):
    print(request.body)
    if request.method == 'GET':
        if request.GET.get('userId') != None:
            # questions = Quiz.objects.filter(quizId=request.GET.get('userId'))
            results = AppUser.objects.all()
            return JsonResponse({'users': list(results.values()), 'error': None})
        else:
            return JsonResponse({'error': user_id_not_found, 'users':[]})
    else:    
        return JsonResponse({'error': invalid_request, 'users': []})

@api_view(['POST'])
def add_new_user(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            print(data)
            print(type(data))
            if data.get('userId') != None and data.get('user_name') != None and data.get('email') != None and data.get('password') != None:
                # questions = Quiz.objects.filter(quizId=request.GET.get('userId'))
                
                AppUser.save(AppUser(**data))
                
                return JsonResponse({'user': data, 'error': None})
            else:
                return JsonResponse({'error': "invalid/missing user data", 'user':None})
        else:    
            return JsonResponse({'error': invalid_request, 'user': None})
    except Exception as ex:
        return JsonResponse({"error": str(ex), "user": None})