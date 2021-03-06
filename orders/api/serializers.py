from rest_framework import serializers
from orders.models import Order, OrderItem, Table


class TableSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_table_detail')

    class Meta:
        model = Table
        fields = ['title', 'id', 'is_using', 'user_using', 'ordering', 'url', 'last_active_table']
    

class OrderSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_order_detail')
    
    class Meta:
        model = Order
        fields = ['title', 'timestamp', 'user_created', 'user_edited',
                  'active', 'is_paid', 'table_related', 'value', 'paid_value',
                  'id',
                  'tag_value', 'tag_paid_value', 'tag_table_related',
                  'tag_is_paid', 'remain_value', 'tag_remain_value',
                  'url', 'tag_timestamp'
                ]


class OrderItemSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_order_item_detail')

    class Meta:
        model = OrderItem
        fields= ['url',
                 'id', 'product_related', 'order_related',
                 'value', 'paid_value', 'is_paid', 'qty',
                 'tag_product_related', 'tag_value', 'tag_paid_value', 'tag_remain',
                 'tag_total_value',
                ]