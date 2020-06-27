import requests
import json

def getCreds() :
    creds = dict()
    creds['access_token'] = 'EAApVTGkUJwcBANlq7weQBtmkZBQcqrDn6NFhBaGAlxaVAIYxd4t4bmMpMrKJhZA22ZBRi0YPMmjszEKpuRXZCDLynes5kGSVxxqvVD8vsv5ZCPoYDTSFBVv0diEzOHIoxTheOmapXrJXYyNo9M2njNUCCIQnOZC0bcZBGJCAprBZCQZDZD'
    creds['client_id'] = '2908536435910407'
    creds['client_secret'] = '4a782190da7189362492060d608f721f'
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v7.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'

    return creds

def makeApiCall( url, endpointParams, debug = 'no' ) :
    data = requests.get( url, endpointParams )
    
    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 )
    response['json_data'] = json.loads( data.content )
    response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 )

    if ( 'yes' == debug) :
        displayApiCallData( response )

    return response

def displayApiCallData( response ) :
    print("\nURL: ")
    print(response['url'])
    print("\nEndpoint Params: ")
    print(response['endpoint_params_pretty'])
    print("\nResponse: ")
    print(response['json_data_pretty'])