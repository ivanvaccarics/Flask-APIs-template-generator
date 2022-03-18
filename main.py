import json

path = input("Path of the file (add .json): ")

print("Opening the json file")
config = json.load(open(path))

var_import = """from flask import Flask, jsonify
app = Flask(__name__)
"""
list_func = []

print("Creating the Flask APIs template")

for elem in config['api']:
    parameters = []
    
    for k,v in elem['func_input_parameters'].items(): 
        parameters.append(f'{k}={v}')

    var_func = f"""@app.route('{elem['route']}', methods = {elem['method']})
def {elem['func_name']}({','.join(parameters)}):
    return jsonify(200)    
    """
    list_func.append(var_func)

var_exec = f"""if __name__ == '__main__':
    app.run(host='{config['address']}', port={config['port']})
"""

print("Writing on disk")

with open(config['file']+'.py', 'w') as f:
    f.write(var_import + '\n')
    for x in list_func:
        f.write(x + '\n') 
    f.write(var_exec + '\n') 
f.close()