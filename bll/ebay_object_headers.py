


def get_headers_data_i():
    # need to define object headers
    headers = []
    headers.append('item_id')
    headers.append('item_title')
    headers.append('item_category')
    headers.append('item_condition')
    headers.append('item_condition_description')
    headers.append('item_price')
    headers.append('item_qty')
    headers.append('ship_policy')
    headers.append('packed_item_weight_lb')
    headers.append('packed_item_weight_oz')
    headers.append('packed_item_height')
    headers.append('packed_item_length')
    headers.append('packed_item_depth')
    headers.append('payment_policy')
    headers.append('return_policy')

    return headers


def get_headers_data_ii():
    headers2 = []
    headers2.append('item_id')
    headers2.append('box_name')
    headers2.append('box_category')
    headers2.append('unit_price')
    headers2.append('inv_qty')
    headers2.append('total_value')
    headers2.append('box_packing_weight_lb')
    headers2.append('box_packing_weight_oz')
    headers2.append('unit_weight_lb')
    headers2.append('unit_weight_oz')
    headers2.append('qty_weight_lb')
    headers2.append('qty_weight_oz')
    headers2.append('location')
    headers2.append('section')
    headers2.append('box_height')
    headers2.append('box_length')
    headers2.append('box_depth')
    headers2.append('box_type')
    headers2.append('box_style')
    headers2.append('box_details')
    headers2.append('pic_local_uri')
    headers2.append('pic_internet_uri')

    return headers2

def get_headers_data_iii():
    headers3 = []
    headers3.append('addressLine1')
    headers3.append('addressLine2')
    headers3.append('city')
    headers3.append('country')
    headers3.append('county')
    headers3.append('postalCode')
    headers3.append('stateOrProvince')
    headers3.append('locationAdditionalInformation')
    headers3.append('locationInstructions')
    headers3.append('locationTypes')
    headers3.append('merchantLocationStatus')
    headers3.append('name')

    return headers3


def get_headers_payment_policy():
    headers4 = []
    headers4.append('categoryTypes[i].default')
    headers4.append('categoryTypes[i].name')
    headers4.append('description')
    headers4.append('immediatePay')
    headers4.append('marketplaceId')
    headers4.append('name')
    headers4.append('paymentInstructions')
    headers4.append('paymentMethods[i][paymentMethodType]')
    headers4.append('paymentMethods[i][recipientAccountReference.referenceId]')
    headers4.append('paymentMethods[i][recipientAccountReference.referenceType]')

    return headers4


def get_headers_return_policy():
    headers = []
    headers.append('categoryTypes[i].default')
    headers.append('categoryTypes[i].name')
    headers.append('description')
    headers.append('internationalOverride.returnPeriod.unit')
    headers.append('internationalOverride.returnPeriod.value')
    headers.append('internationalOverride.returnsAccepted')
    headers.append('internationalOverride.returnShippingCostPayer')
    headers.append('marketplaceId')
    headers.append('name')
    headers.append('refundMethod')
    headers.append('returnInstructions')
    headers.append('returnPeriod.unit')
    headers.append('returnPeriod.value')
    headers.append('returnsAccepted')
    headers.append('returnShippingCostPayer')

    return headers