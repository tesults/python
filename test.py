import tesults

def main():
    data = {
        'target': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjQ0MWZjYmNiLTA0MjAtNGYzMS05ZGMwLTUwY2JmYmFhOWNmNS0xNDc3MDA4NjUyMjQ0IiwiZXhwIjo0MTAyNDQ0ODAwMDAwLCJ2ZXIiOiIwIiwic2VzIjoiNmI3OGI2Y2YtOTkwYy00YjYyLThmOTQtNDZkMjE1ZjA1ZWRlIiwidHlwZSI6InQifQ.XCsjYNzhEgY1AHmyQP0q7GiirpRH5dgxYxKBfO1IFwE',
        'results': {
            'cases': [
                {'name': 'Test 1', 
                 'desc':'Test 1 desc',
                 'suite': 'Suite A',
                 'result': 'pass'
                },
                {'name': 'Test 2', 
                 'desc':'Test 2 desc',
                 'suite': 'Suite A',
                 'result': 'pass'
                },
                {'name': 'Test 3', 
                 'desc':'Test 3 desc',
                 'suite': 'Suite A',
                 'result': 'pass'
                }
            ]
        }
    }
    
    print(tesults.results(data))

main()