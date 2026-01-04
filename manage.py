#!/usr/bin/env python
import os, sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
    if src not in sys.path:
        sys.path.insert(0, src)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
