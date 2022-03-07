from flask import jsonify, make_response
from api.anthill import blueprint
from api import limiter
from api.generators import (
    generate_cnpj,
    generate_cpf,
    generate_rg,
    generate_name,
    generate_person_address,
    generate_birthday_date
)

default_all_values = {
    'cpf_mode': 'points', 
    'cnpj_mode': 'points', 
    'gen_cnpj': True, 
    'rg_mode': 'points', 
    'gender_name': 'R'
}

default_rg_mode = {
    'cpf_mode': '', 
    'cnpj_mode': '', 
    'gen_cnpj': False, 
    'rg_mode': 'points', 
    'gender_name': 'R'
}

default_cpf_mode = {
    'cpf_mode': 'points', 
    'cnpj_mode': '', 
    'gen_cnpj': False, 
    'rg_mode': '', 
    'gender_name': 'R'
}

default_cnpj_without_points_mode = {
    'cpf_mode': '', 
    'cnpj_mode': '', 
    'gen_cnpj': True, 
    'rg_mode': '', 
    'gender_name': 'R'
}
default_cnpj_points_mode = {
    'cpf_mode': '', 
    'cnpj_mode': 'points', 
    'gen_cnpj': True, 
    'rg_mode': '', 
    'gender_name': 'R'
}

default_gender_name = {
    'cpf_mode': '', 
    'cnpj_mode': '', 
    'gen_cnpj': True, 
    'rg_mode': '', 
}


@blueprint.route('/full', defaults=default_all_values, methods=["GET"])
@blueprint.route('/custom/rg', defaults=default_rg_mode, methods=["GET"])
@blueprint.route('/custom/cpf', defaults=default_cpf_mode, methods=["GET"])
@blueprint.route('/custom/cnpj/null', defaults=default_cnpj_without_points_mode, methods=["GET"])
@blueprint.route('/custom/cnpj/points', defaults=default_cnpj_points_mode, methods=["GET"])
@blueprint.route('/custom/gender/<gender_name>', defaults=default_gender_name, methods=["GET"])
@blueprint.route('/custom/all/<cpf_mode>/<cnpj_mode>/<gen_cnpj>/<rg_mode>/<gender_name>', methods=["GET"])
@limiter.limit("60/minute")
def generate_a_custom_person(cpf_mode, cnpj_mode, gen_cnpj, rg_mode, gender_name):

    if type(gen_cnpj) is not bool:
        gen_cnpj = convert_arg_to_boolean_value(gen_cnpj)
        
    ( 
        name, 
        age, 
        birthday, 
        cpf, 
        rg, 
        cnpj, 
        address, 
        state, 
        state_abbreviation,
        city, 
        bairro, 
        logradouro
    ) = get_data(cpf_mode=cpf_mode, cnpj_mode=cnpj_mode, gen_cnpj=bool(gen_cnpj), rg_mode=rg_mode, gender_name=gender_name)

    person_data = {
        "name": name,
        "age": age,
        "birthday": birthday,
        "cpf": cpf,
        "rg": rg,
        "cnpj": cnpj,
        "address": address,
        "state": state,
        "state_abbreviation": state_abbreviation,
        "city": city,
        "bairro": bairro,
        "logradouro": logradouro
    }
    return jsonify(person_data)


@blueprint.route('/', methods=["GET"])
@limiter.limit("60/minute")
def default_person_generation():
    ( 
        name, 
        age, 
        birthday, 
        cpf, 
        rg, 
        cnpj, 
        address, 
        state, 
        state_abbreviation,
        city, 
        bairro, 
        logradouro
    ) = get_data()

    person_data = {
        "name": name,
        "age": age,
        "birthday": birthday,
        "cpf": cpf,
        "rg": rg,
        "cnpj": cnpj,
        "address": address,
        "state": state,
        "state_abbreviation": state_abbreviation,
        "city": city,
        "bairro": bairro,
        "logradouro": logradouro
    }
    return jsonify(person_data)



def convert_arg_to_boolean_value(arg):
    return arg.lower() in ("true", "1", "yes", "sim", "si", "s", "ss", "ja")


def get_data(cpf_mode='', cnpj_mode='', gen_cnpj=False, rg_mode='', gender_name='R') -> tuple:

    rg = generate_rg(
        output_mode=rg_mode
    )

    cpf = generate_cpf(
        output_mode=cpf_mode
    )

    if gen_cnpj:
        cnpj = generate_cnpj(
            output_mode=cnpj_mode)
    else:
        cnpj = ""

    birthday, age  = generate_birthday_date()        
    name = generate_name(gender_name=gender_name)
    location_data = generate_person_address()
    
    address = location_data['address']
    logradouro = location_data['logradouro']
    state = location_data['state']
    state_abbreviation = location_data['state_abbreviation']
    city = location_data['city']
    bairro = location_data['bairro']

    return  name, age, birthday, cpf, rg, cnpj, address, state, state_abbreviation, city, bairro, logradouro

