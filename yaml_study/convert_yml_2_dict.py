import yaml

with open("./sample_eg.yml") as f:
    dct = yaml.load(f)

print(dct)

a = {
    'key': {
        'child-key': 'value',
        'child-key2': 'value2'
    },
    'companies': [
        {'id': 1, 'name': 'company1', 'price': '200W'},
        {'id': 2, 'name': 'company2', 'price': '400W'}
    ],
    'languages': ['Ruby', 'Perl', 'Python'],
    'websites': {
        'YAML': 'yaml.org',
        'Ruby': 'ruby-lang.org',
        'Python': 'python.org',
        'Perl': 'use.perl.org'
    }
}

"""
key:
  child-key: value
  child-key2: value2

companies:
  -
    id: 1
    name: company1
    price: 200W
  -
    id: 2
    name: company2
    price: 400W

languages:
  - Ruby
  - Perl
  - Python
websites:
  YAML: yaml.org
  Ruby: ruby-lang.org
  Python: python.org
  Perl: use.perl.org
"""
