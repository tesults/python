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
                 'files' : ['/Users/admin/Desktop/img1.png', '/Users/admin/Desktop/img2.png']

                },
                {'name': 'Test 2',
                 'desc':'Test 2 desc',
                 'suite': 'Suite A',
                 'result': 'pass',
                 'files' : ['/Users/admin/Desktop/img3.png', '/Users/admin/Desktop/img4.png']
                },
                {'name': 'Test 3',
                 'desc':'Test 3 desc',
                 'suite': 'Suite A',
                 'result': 'pass',
                 'files' : ['/Users/admin/Desktop/img4.png']
                }
            ]
        }
    }
    
    response = tesults.results(data)
    print ('success: ' + str(response.get('success')))
    print ('message: ' + response.get('message'))
    print ('warnings: ' + str(len(response.get('warnings'))))
    print ('errors: ' + str(len(response.get('errors'))))

main()