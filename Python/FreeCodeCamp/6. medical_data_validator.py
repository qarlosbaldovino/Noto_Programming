import re

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    constraints = {
        'patient_id': isinstance(patient_id, str) 
        and re.fullmatch(r'p\d+', patient_id, re.IGNORECASE), #String y empezar con una (p o P) y despues numeros.
        'age': isinstance(age, int) and age >= 18, #Entero y mayor igual a 18
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'), #String y el genero (pasado a minuscula) male o female
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None, #String o None
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]), #Array y todos los valores dentro deben ser string
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE) #String y empezar con V y numeros
    }

    return [key for key, value in constraints.items() if not value] #Devuelve la clave de los items que no cumplen

def validate(data):
    is_sequence = isinstance(data, (list, tuple)) #Verifica si pasamos una lista o tupla
    is_invalid = False

    if not is_sequence: #Si no es lista o tupla...
        print('Invalid format: expected a list or tuple.')
        return False

    key_set = set( #Seteamos con las claves de lo que se espera como diccionario
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )

    for index, dictionary in enumerate(data): #Iteramos la data extrayendo el índice y su contenido

        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True

        if set(dictionary.keys()) != key_set: #Chequeamos si las claves son iguales al set que hicimos con la data que pasamos como parametro
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True

        invalid_records = find_invalid_records(**dictionary) #Guardamos en una lista las keys con errores

        for key in invalid_records: #Si encuentra error, mostramos la lista y el valor donde se equivoca y su respectiva posicion
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            is_invalid = True
        

    if is_invalid:
        return False
    
    print('Valid format.')
    return True

validate(medical_records)