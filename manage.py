import os
import sys

#funcion principal para la ejecución de la app a través de Django.
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dtalent_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you " # error en caso de que Django no esté instalado o ubicado en el camino correspondiente
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

#llamamos a main para su ejecución
if __name__ == '__main__':
    main()
