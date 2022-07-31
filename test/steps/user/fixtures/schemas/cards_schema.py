get_cards_response_schema = {
    "_embedded":
        {'type': 'dict', 'schema':
            {
                "card":
                    {'type': 'list', 'schema':

                        {'type': 'dict', 'schema':
                            {
                                "longNum": {'type': 'string'},
                                "expires": {'type': 'string'},
                                "ccv": {'type': 'string'},
                                "_links":
                                    {'type': 'dict', 'schema':
                                        {
                                            "self":
                                                {'type': 'dict', 'schema':

                                                    {
                                                        "href": {'type': 'string'}
                                                    }
                                                 },
                                            "card":
                                                {'type': 'dict', 'schema':
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
         },
    "_links": {'type': 'dict'},
    "page": {'type': 'dict'}
}

post_cards_response_schema = {
    "id": {'type': 'string'}
}
delete_cards_response_schema = {
    "status": {'type': 'boolean'}
}

get_cards_by_id_response_schema = \
    {
        "longNum": {'type': 'string'},
        "expires": {'type': 'string'},
        "ccv": {'type': 'string'},
        "_links":
            {'type': 'dict', 'schema':
                {
                    "self":
                        {'type': 'dict', 'schema':

                            {
                                "href": {'type': 'string'}
                            }
                         },
                    "card":
                        {'type': 'dict', 'schema':
                            {
                                "href": {'type': 'string'}
                            }
                         }
                }
             }
    }
