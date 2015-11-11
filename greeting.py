def greeting(name, language='english'):
    if language == 'english':
        return 'Hello, {0}!'.format(name)
    elif language == 'french':
        return 'Bonjour, {0}!'.format(name)
    else:
        return 'I do not speak {0}'.format(language)

print greeting('Bob')
print greeting('Francois', language='french')
print greeting('Maria', language='spanish')

def data_taking_years(default_years=None):
    if default_years is None:
        default_years = []
    default_years += [2011, 2012]
    return default_years

print data_taking_years()
print data_taking_years()

def call_this_function(func):
    return func()

def build_greeting(salutation):
    def greeting(name):
        return '{0} {1}!'.format(salutation, name)
    return greeting

print build_greeting('Hola')('Bob')
print greeting('Dave', language='french')
