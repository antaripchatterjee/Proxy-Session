from sys import stderr
from proxy_session import ProxySession
from proxy_session import ProxySessionTimeout

if __name__ == '__main__':
    with ProxySession() as ps:
        error_ = ps.error
        if error_:
            print('Error Status: ', error_[0], file=stderr)
            print('Error:\n' + error_[1], file=stderr)
        response, proxy_addr = ps.make_request('https://httpbin.org/ip', timeout=ProxySessionTimeout.LONG_TIMEOUT, log=True)
        if response.status_code == 200:
            print(f'Response Content:\n{response.text}')
            print(f'Proxy URL: {proxy_addr}')
        else:
            print(f'{response}')
        