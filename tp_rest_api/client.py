import requests

def main():
    response = requests.get("http://127.0.0.1:5000/todos")

    data_response = response.json()
    
    print(data_response['data'][0]['name'])

if __name__=='__main__':
    main()
