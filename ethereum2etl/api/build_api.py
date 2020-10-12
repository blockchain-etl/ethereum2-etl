from blockchainetl_common.thread_local_proxy import ThreadLocalProxy

from ethereum2etl.api.ethereum2_teku_api import Ethereum2TekuApi
from ethereum2etl.api.rate_limiting_proxy import RateLimitingProxy


def build_api(provider_uri, rate_limit):
    api = ThreadLocalProxy(lambda: Ethereum2TekuApi(provider_uri))
    if rate_limit is not None and rate_limit > 0:
        api = RateLimitingProxy(api, max_per_second=rate_limit)
    return api