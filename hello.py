def app (environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    response_hello =['\r\n'.join(environ['QUERY_STRING'].split('&'))]
    start_response (status, headers)
    return response_hello
