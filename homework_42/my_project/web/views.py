from django.shortcuts import render


def operation(request):
    operation = request.POST.get('operation')
    if operation == '+':
        num = float(request.POST.get('First number')) + float(request.POST.get('Second number'))
        return int(num) if int(num)==float(num) else num
    elif operation == '*':
        num = float(request.POST.get('First number')) * float(request.POST.get('Second number'))
        return int(num) if int(num)==float(num) else num
    elif operation == '-':
        num = float(request.POST.get('First number')) - float(request.POST.get('Second number'))
        return int(num) if int(num)==float(num) else num
    elif operation == '/':
        if request.POST.get('Second number') != '0':
            num = float(request.POST.get('First number')) / float(request.POST.get('Second number'))
            return int(num) if int(num)==float(num) else num
        else:
            return None
    elif not operation:
        return 'не ввели операцию'
        


def valid_nums(request):
    try:
        float(request.POST.get('First number')) + float(request.POST.get('Second number'))
        if request.POST.get('operation'):
            return True
        else:
            return 'не ввели операцию'
    except:
        return False

def ans(request):
    if valid_nums(request):
        content = {
            'oper' : str(operation(request)),
            'var_1': 'На 0 делить нельзя',
        }
        if content['oper'] == 'None':
            content['oper'] = None
        elif operation(request) == 'не ввели операцию':
            content['oper'] = 'не ввели операцию'
    else:
        content = {
            'oper' : 'не ввели число',
        }
    return render(request, 'ans.html', content) 
    



def index_view(request):
    return render(request, 'index.html')