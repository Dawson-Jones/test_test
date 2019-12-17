import yaml

with open("./docker-compose.yaml") as f:
    dct = yaml.load(f)


"""
{
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

"""
{
    'version': '3',
    'services': {
        'db': {
            'image': 'mongo:3.6.9',
            'volumes': ['./data:/data/db'],
            'ports': ['27027:27017'],
            'command': 'mongod --config /data/db/mongod.yml'
        },
        'db2': {
            'image': 'mongo:3.6.9',
            'volumes': ['./data2:/data/db'],
            'ports': ['27028:27017'],
            'command': 'mongod --config /data/db/mongod.yml'
        },
        'db3': {
            'image': 'mongo:3.6.9',
            'volumes': ['./data3:/data/db'],
            'ports': ['27029:27017'],
            'command': 'mongod --config /data/db/mongod.yml'
        },
        'DB_inter': {
            'image': 'ubuntu-flask2:latest',
            'network_mode': 'host',
            'restart': 'unless-stopped',
            'ports': ['5000:5000'],
            'volumes': ['./:/home', '/etc/localtime:/etc/localtime:ro', '/etc/timezone:/etc/timezone:ro'],
            'command': ['/bin/sh', '-c', 'cd /home\npython3 ./main.py\n']
        }
    }
}
"""
