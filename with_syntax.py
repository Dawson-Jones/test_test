class Sample(object):
    def __init__(self):
        print('init called')

    def __call__(self, *args, **kwargs):
        print('call called')

    def __enter__(self):
        print('enter called')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit called')


s = Sample()

s()

s.close()

