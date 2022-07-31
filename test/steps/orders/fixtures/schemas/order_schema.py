get_orders_response_schema = \
    {
        "_embedded":
            {'type': 'dict', 'schema':
                {
                    "customerOrders":
                        {'type': 'list', 'schema':
                            {'type': 'string'}
                         }
                }
             },
        "_links": {'type': 'dict', 'schema':
            {
                "self":
                    {'type': 'dict', 'schema':
                        {
                            "href": {'type': 'string'}
                        }
                     },
                "profile":
                    {'type': 'dict', 'schema':
                        {
                            "href": {'type': 'string'}
                        }
                     },
                "search":
                    {'type': 'dict', 'schema':
                        {
                            "href": {'type': 'string'}
                        }
                     }
            }
                   },
        "page":
            {'type': 'dict', 'schema':
                {
                    "size": {'type': 'integer'},
                    "totalElements": {'type': 'integer'},
                    "totalPages": {'type': 'integer'},
                    "number": {'type': 'integer'}
                }
             }
    }
post_orders_response_schema = \
    {
        "id": {'type': 'string'},
        "customerId": {'type': 'string'},
        "customer":
            {'type': 'dict', 'schema':
                {
                    "firstName": {'type': 'string'},
                    "lastName": {'type': 'string'},
                    "username": {'type': 'string'},
                    "addresses":
                        {'type': 'list', 'schema':
                            {'type': 'dict', 'schema':
                                {
                                    "id": {'type': 'string'},
                                    "number": {'type': 'string'},
                                    "street": {'type': 'string'},
                                    "city": {'type': 'string'},
                                    "postcode": {'type': 'string'},
                                    "country": {'type': 'string'}
                                }
                             }
                         },
                    "cards":
                        {'type': 'list', 'schema':
                            {'type': 'dict', 'schema':
                                {
                                    "id": {'type': 'string'},
                                    "longNum": {'type': 'string'},
                                    "expires": {'type': 'string'},
                                    "ccv": {'type': 'string'}
                                }

                             }
                         }
                }
             },
        "address":
            {'type': 'dict', 'schema':
                {
                    "number": {'type': 'string'},
                    "street": {'type': 'string'},
                    "city": {'type': 'string'},
                    "postcode": {'type': 'string'},
                    "country": {'type': 'string'}
                }
             },
        "card":
            {'type': 'dict', 'schema':
                {
                    "longNum": {'type': 'string'},
                    "expires": {'type': 'string'},
                    "ccv": {'type': 'string'}
                }
             },
        "items":
            {'type': 'list', 'schema':

                {'type': 'dict', 'schema':
                    {
                        "id": {'type': 'string'},
                        "itemId": {'type': 'string'},
                        "quantity": 0,
                        "unitPrice": 0
                    }
                 }

             },
        "shipment":
            {'type': 'dict', 'schema':
                {
                    "id": {'type': 'string'},
                    "name": {'type': 'string'}
                }
             },
        "date": {'type': 'string'},
        "total": {'type': 'integer'}
    }
