"""Stream type classes for tap-woocommerce."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

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
        th.Property("name", th.StringType),
        th.Property("slug", th.StringType),
        th.Property("permalink", th.StringType),
        th.Property("date_created", th.DateTimeType),
        th.Property("date_created_gmt", th.DateTimeType),
        th.Property("date_modified", th.DateTimeType),
        th.Property("date_modified_gmt", th.DateTimeType),
        th.Property("type", th.StringType),
        th.Property("status", th.StringType),
        th.Property("featured", th.BooleanType),
        th.Property("catalog_visibility", th.StringType),
        th.Property("description", th.StringType),
        th.Property("short_description", th.StringType),
        th.Property("sku", th.StringType),
        th.Property("price", th.StringType),
        th.Property("regular_price", th.StringType),
        th.Property("sale_price", th.StringType),
        th.Property("date_on_sale_from", th.DateTimeType),
        th.Property("date_on_sale_from_gmt", th.DateTimeType),
        th.Property("date_on_sale_to", th.DateTimeType),
        th.Property("date_on_sale_to_gmt", th.DateTimeType),
        th.Property("price_html", th.StringType),
        th.Property("on_sale", th.BooleanType),
        th.Property("purchasable", th.BooleanType),
        th.Property("total_sales", th.IntegerType),
        th.Property("virtual", th.BooleanType),
        th.Property("downloadable", th.BooleanType),
        th.Property("downloads", th.ArrayType(th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("file", th.StringType)
        ))),
        th.Property("download_limit", th.IntegerType),
        th.Property("download_expiry", th.IntegerType),
        th.Property("external_url", th.StringType),
        th.Property("button_text", th.StringType),
        th.Property("tax_status", th.StringType),
        th.Property("tax_class", th.StringType),
        th.Property("manage_stock", th.BooleanType),
        th.Property("stock_quantity", th.IntegerType),
        th.Property("stock_status", th.StringType),
        th.Property("backorders", th.StringType),
        th.Property("backorders_allowed", th.BooleanType),
        th.Property("backordered", th.BooleanType),
        th.Property("sold_individually", th.BooleanType),
        th.Property("weight", th.StringType),
        th.Property("dimensions", th.ObjectType(
            th.Property("length", th.StringType),
            th.Property("width", th.StringType),
            th.Property("height", th.StringType)
        )),
        th.Property("shipping_required", th.BooleanType),
        th.Property("shipping_taxable", th.BooleanType),
        th.Property("shipping_class", th.StringType),
        th.Property("shipping_class_id", th.IntegerType),
        th.Property("reviews_allowed", th.BooleanType),
        th.Property("average_rating", th.StringType),
        th.Property("rating_count", th.IntegerType),
        th.Property("related_ids", th.ArrayType(th.IntegerType)),
        th.Property("upsell_ids", th.ArrayType(th.IntegerType)),
        th.Property("cross_sell_ids", th.ArrayType(th.IntegerType)),
        th.Property("parent_id", th.IntegerType),
        th.Property("purchase_note", th.StringType),
        th.Property("categories", th.ArrayType(th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("slug", th.StringType)
        ))),
        th.Property("tags", th.ArrayType(th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("slug", th.StringType)
        ))),
        th.Property("images", th.ArrayType(th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("date_created", th.DateTimeType),
            th.Property("date_modified", th.DateTimeType),
            th.Property("src", th.StringType),
            th.Property("name", th.StringType),
            th.Property("alt", th.StringType)
        ))),
        th.Property("attributes", th.ArrayType(th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("position", th.IntegerType),
            th.Property("visible", th.BooleanType),
            th.Property("variation", th.BooleanType),
            th.Property("options", th.ArrayType(th.StringType))
        ))),
        th.Property("default_attributes", th.ArrayType(th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("option", th.StringType)
        ))),
        th.Property("variations", th.ArrayType(th.IntegerType)),
        th.Property("grouped_products", th.ArrayType(th.IntegerType)),
        th.Property("menu_order", th.IntegerType),
        th.Property("meta_data", th.ArrayType(th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("key", th.StringType),
            th.Property("value", th.StringType)
        ))),
        th.Property("has_options", th.BooleanType),
        th.Property("_links", th.ObjectType(
            th.Property("self", th.ArrayType(th.ObjectType(
                th.Property("href", th.StringType),
            ))),
            th.Property("collection", th.ArrayType(th.ObjectType(
                th.Property("href", th.StringType),
            ))),
        )),
        th.Property("low_stock_amount", th.ArrayType(th.IntegerType)),
    ).to_dict()
