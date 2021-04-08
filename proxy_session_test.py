from proxy_session import ProxySession
from proxy_session import ProxySessionTimeout

if __name__ == '__main__':
    with ProxySession() as ps:
        response, proxy_addr = ps.make_request('https://httpbin.org/ip', timeout=ProxySessionTimeout.LONG_TIMEOUT, log=True)
        if response.status_code == 200:
            print(f'Response Content:\n{response.text}')
            print(f'Proxy URL: {proxy_addr}')
        