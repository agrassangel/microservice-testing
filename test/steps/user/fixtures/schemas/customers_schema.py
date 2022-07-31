customer_response_schema = {
    "_embedded":
        {
            'type': 'dict', 'schema':
            {
                "customer":
                    {'type': 'list', 'schema':
                        {
                            'type': 'dict', 'schema':
                            {
                                "firstName": {'type': 'string'},
                                "lastName": {'type': 'string'},
                                "username": {'type': 'string'},
                                "id": {'type': 'string'},
                                "_links":
                                    {
                                        'type': 'dict', 'schema':
                                        {
                                            "addresses":
                                                {
                                                    'type': 'dict', 'schema':
                                                    {
                                                        "href": {'type': 'string'}
                                                    }
                                                }
                                            ,
                                            "cards":
                                                {
                                                    'type': 'dict', 'schema':
                                                    {
                                                        "href": {'type': 'string'}
                                                    }
                                                }
                                            ,
                                            "customer":
                                                {
                                                    'type': 'dict', 'schema':
                                                    {
                                                        "href": {'type': 'string'}
                                                    }
                                                }
                                            ,
                                            "self":
                                                {
                                                    'type': 'dict', 'schema':
                                                    {
                                                        "href": {'type': 'string'}
                                                    }
                                                }
                                        }
                                    }
                            }
                        }
                     }
            }
        }
}

delete_customer_by_id_response_schema = \
    {
        "status": {'type': 'boolean'}
    }

get_customer_by_id_response_schema = \
    {
        "firstName": {'type': 'string'},
        "lastName": {'type': 'string'},
        "username": {'type': 'string'},
        "_links":
            {'type': 'dict', 'schema':
                {
                    "self":
                        {
                            "href": {'type': 'string'}
                        },
                    "customer":
                        {
                            'type': 'dict', 'schema':
                            {
                                "href": {'type': 'string'}
                            }
                        },
                    "addresses":
                        {
                            'type': 'dict', 'schema':
                            {
                                "href": {'type': 'string'}
                            }
                        },
                    "cards":
                        {
                            'type': 'dict', 'schema':
                            {
                                "href": {'type': 'string'}
                            }
                        }

                }
             },
        "_links": {'type': 'dict'},
        "page": {'type': 'dict'}
    }

get_customer_by_id_card_response_schema = \
    {
        "_embedded":
            {'type': 'dict', 'schema':
                {
                    "card":
                        {'type': 'list', 'schema':
                            {
                                'type': 'dict', 'schema':
                                {
                                    "longNum": {'type': 'string'},
                                    "expires": {'type': 'string'},
                                    "ccv": {'type': 'string'},
                                    "_links":
                                        {
                                            'type': 'dict', 'schema':
                                            {
                                                "self":
                                                    {
                                                        'type': 'dict', 'schema':
                                                        {
                                                            "href": {'type': 'string'}
                                                        }
                                                    }
                                            },
                                            "card":
                                                {
                                                    'type': 'dict', 'schema':
                                                    {
                                                        "href": {'type': 'string'}
                                                    }
                                                }
                                        }
                                }
                            }
                         }
                }
             },
        "_links": {'type': 'dict'},
        "page": {'type': 'dict'}
    }

get_customer_by_id_address_response_schema = \
    {
        "_embedded": {
            "address":
                {'type': 'list', 'schema':
                    {
                        'type': 'dict', 'schema':
                        {
                            "number": {'type': 'string'},
                            "street": {'type': 'string'},
                            "city": {'type': 'string'},
                            "postcode": {'type': 'string'},
                            "country": {'type': 'string'},
                            "_links": {
                                "self":
                                    {
                                        'type': 'dict', 'schema':
                                        {
                                            "href": {'type': 'string'}
                                        }
                                    },
                                "address":
                                    {
                                        'type': 'dict', 'schema':
                                        {
                                            "href": {'type': 'string'}
                                        }
                                    }
                            }
                        }
                    }
                 }
        },
        "_links": {'type': 'dict'},
        "page": {'type': 'dict'}
    }
