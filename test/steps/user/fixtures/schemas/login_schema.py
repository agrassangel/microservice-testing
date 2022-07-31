# https://docs.python-cerberus.org/en/stable/validation-rules.html#schema-dict
loging_response_schema = \
    {
        "_embedded": {
            'type': 'dict', 'schema':
                {
                    "customer":
                        {
                            'type': 'list', 'schema':
                            {
                                'type': 'dict', 'schema':
                                {
                                    "firstName": {'type': 'string'},
                                    "lastName": {'type': 'string'},
                                    "username": {'type': 'string'},
                                    "_links":
                                        {
                                            'type': 'dict', 'schema': {
                                            "self":
                                                {
                                                    "href": {'type': 'string'}
                                                },
                                            "customer":
                                                {
                                                    'type': 'dict', 'schema': {
                                                    "href": {'type': 'string'}
                                                }
                                                },
                                            "addresses":
                                                {
                                                    'type': 'dict', 'schema': {
                                                    "href": {'type': 'string'}
                                                }
                                                },
                                            "cards":
                                                {
                                                    'type': 'dict', 'schema': {
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
