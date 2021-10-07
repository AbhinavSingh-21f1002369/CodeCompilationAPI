import subprocess

def compile(code,input_str):
    with open("/home/pi/Desktop/CodeCompilationAPI/code.py","w") as f :
        f.write(code)
        f.close()
    
    # Start a Subprocess and run the Python Code
    p = subprocess.Popen(['python3', '/home/pi/Desktop/CodeCompilationAPI/code.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Communicate with the python and pass the input
    x = p.communicate(input_str.encode())
    #print(x[0].decode())
    #print(x[1].decode())
    result = {}
    result['output']=x[0].decode()
    result['error']=x[1].decode()
    # Check if there is any error
    if result['error'] == '':
        result['status']="Ok"
    else:
        result['status']="NotOk"
    return (result)