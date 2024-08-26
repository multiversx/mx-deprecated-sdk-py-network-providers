import warnings

from multiversx_sdk_network_providers.api_network_provider import \
    ApiNetworkProvider
from multiversx_sdk_network_providers.errors import GenericError
from multiversx_sdk_network_providers.proxy_network_provider import \
    ProxyNetworkProvider
from multiversx_sdk_network_providers.resources import GenericResponse

warnings.warn('This package is deprecated and will no longer be maintained. Instead, please use "multiversx-sdk".')

__all__ = ["GenericError", "GenericResponse", "ApiNetworkProvider", "ProxyNetworkProvider"]
