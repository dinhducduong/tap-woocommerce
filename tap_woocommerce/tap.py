"""WooCommerce tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_woocommerce.streams import (
    WooCommerceStream,
    ProductsStream,
    CategoriesStream,
    ProductsAttributeStream
)

STREAM_TYPES = [
    ProductsStream,
    CategoriesStream,
    ProductsAttributeStream
]


class TapWooCommerce(Tap):
    """WooCommerce tap class."""
    name = "tap-woocommerce"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property("consumer_key", th.StringType, required=True),
        th.Property("consumer_secret", th.StringType, required=True),
        th.Property("site_url", th.StringType, required=True),
        th.Property("start_date", th.DateTimeType)
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
