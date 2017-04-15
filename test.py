import tesults

def main():
    data = {
        'target': 'token',
        'results': {
            'cases': [
                {'name': 'Test 1', 
                 'desc':'Test 1 desc',
                 'suite': 'Suite A',
                 'result': 'pass',
                 'files' : ['/Users/admin/Desktop/TestFiles/log0.txt', '/Users/admin/Desktop/TestFiles/log1.txt']

                },
                {'name': 'Test 2',
                 'desc':'Test 2 desc',
                 'suite': 'Suite A',
                 'result': 'pass',
                 'files' : ['/Users/admin/Desktop/TestFiles/capture0.png', '/Users/admin/Desktop/TestFiles/capture2.png']
                },
                {'name': 'Test 3',
                 'desc':'Test 3 desc',
                 'suite': 'Suite A',
                 'result': 'pass',
                 'files' : ['/Users/admin/Desktop/TestFiles/capture3.png']
                }
            ]
        }
    }
    
    response = tesults.results(data)
    print 'success: ' + str(response.get('success'))
    print 'message: ' + response.get('message')
    print 'warnings: ' + str(len(response.get('warnings')))
    print 'errors: ' + str(len(response.get('errors')))

main()