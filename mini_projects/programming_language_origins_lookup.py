tech = input('Name a programming language or a framework: ')

# Making use of "match" statement instead of verbose if-elif-statements.

match tech:
    case 'Python':
        print('.')
    case 'Java':
        print('')
    case 'C#' | 'Blazor' | 'Bicep':
        print('Microsoft')
    case 'Kubernetes' | 'Golang' | 'Flutter' | 'Dart':
        print(f'Google is the company behind "{tech}" ')
    case _:
        print('Hey, never heard of that one before!')

