"""Stream type classes for tap-woocommerce."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

import requests
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_woocommerce.client import WooCommerceStream


class ProductsStream(WooCommerceStream):
    """Define custom stream."""
    name = "products"
    path = "products"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("sku", th.StringType),
        th.Property("name", th.StringType),
        th.Property("price", th.IntegerType),
        th.Property("options", th.ArrayType(th.ObjectType(
            th.Property("title", th.StringType),
            th.Property("values", th.ArrayType(th.StringType))
        ))),
        th.Property("media_gallery_entries", th.ArrayType(th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("file", th.ArrayType(th.StringType)),
            th.Property("label", th.ArrayType(th.StringType))
        ))),
        th.Property("created_at", th.StringType),
    ).to_dict()

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        print(response.json())
        # def preprocess_input(data):
        #     data_convert = []
        #     for item in data['products']:
        #         raw_data = {
        #             "id": item['id'],
        #             "name": item['title'],
        #             "sku": item['handle'],
        #             "created_at": item['created_at'],
        #             "updated_at": item['updated_at'],
        #             "options": [],
        #             "media_gallery_entries": [],
        #             "source": "shopify"
        #         }
        #         for variant in item['variants']:
        #             raw_data['options'].append({
        #                 "product_sku": variant['sku'],
        #                 "title": variant['title'],
        #                 "price": variant['price'],
        #                 "sku": variant['sku'],
        #                 "created_at": variant['created_at'],
        #                 "updated_at": variant['updated_at'],
        #             })
        #         for image in item['images']:
        #             raw_data['media_gallery_entries'].append({
        #                 "id": image['id'],
        #                 "position": image['position'],
        #                 "file": image['src'],
        #                 "created_at": image['created_at'],
        #                 "updated_at": image['updated_at'],
        #             })
        #         data_convert.append(raw_data)
        #     return data_convert
        # processed_data = response.json()
        # res = preprocess_input(processed_data)
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())


class CategoriesStream(WooCommerceStream):
    """Define custom stream."""
    name = "categories"
    path = "products/categories"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("slug", th.StringType),
        th.Property("parent", th.IntegerType),
        th.Property("description", th.StringType),
        th.Property("display", th.StringType),
        th.Property("image", th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("date_created", th.DateTimeType),
            th.Property("date_created_gmt", th.DateTimeType),
            th.Property("date_modified", th.DateTimeType),
            th.Property("date_modified_gmt", th.DateTimeType),
            th.Property("src", th.StringType),
            th.Property("name", th.StringType),
            th.Property("alt", th.StringType)
        )),
        th.Property("menu_order", th.IntegerType),
        th.Property("count", th.IntegerType),
        th.Property("_links", th.ObjectType(
            th.Property("self", th.ArrayType(th.ObjectType(
                th.Property("href", th.StringType),
            ))),
            th.Property("collection", th.ArrayType(th.ObjectType(
                th.Property("href", th.StringType),
            ))),
        ))
    ).to_dict()


class ProductsAttributeStream(WooCommerceStream):
    """Define custom stream."""
    name = "products_attribute"
    path = "products/attributes"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("slug", th.StringType),
        th.Property("type", th.StringType),
        th.Property("order_by", th.StringType),
        th.Property("has_archives", th.BooleanType),
        th.Property("_links", th.ObjectType(
            th.Property("self", th.ArrayType(th.ObjectType(
                th.Property("href", th.StringType),
            ))),
            th.Property("collection", th.ArrayType(th.ObjectType(
                th.Property("href", th.StringType),
            ))),
        ))
    ).to_dict()
