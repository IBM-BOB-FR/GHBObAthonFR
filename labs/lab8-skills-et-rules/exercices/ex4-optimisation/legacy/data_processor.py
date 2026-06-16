import json

def process_data(data, format):
    if format == 'json':
        return json.dumps(data)
    elif format == 'xml':
        result = '<data>'
        for key in data:
            result += '<' + key + '>' + str(data[key]) + '</' + key + '>'
        result += '</data>'
        return result
    elif format == 'csv':
        result = ''
        for key in data:
            result += key + ','
        result = result[:-1] + '\n'
        for key in data:
            result += str(data[key]) + ','
        result = result[:-1]
        return result
    else:
        return str(data)

def validate_email(email):
    if '@' in email and '.' in email:
        return True
    return False

def validate_phone(phone):
    if len(phone) >= 10:
        for char in phone:
            if not char.isdigit():
                return False
        return True
    return False

def validate_age(age):
    try:
        age_int = int(age)
        if age_int >= 0 and age_int <= 150:
            return True
        return False
    except:
        return False

def calculate_stats(data):
    total = 0
    count = 0
    for item in data:
        total += item
        count += 1
    avg = total / count
    
    max_val = data[0]
    for item in data:
        if item > max_val:
            max_val = item
    
    min_val = data[0]
    for item in data:
        if item < min_val:
            min_val = item
    
    return {'average': avg, 'max': max_val, 'min': min_val, 'total': total}

# Made with Bob
