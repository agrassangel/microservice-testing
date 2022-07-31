catalogue_response_schema = {
    'type': 'list', 'schema':
        {
            'type': 'dict', 'schema':
            {
                "id": {'type': 'string'},
                "name": {'type': 'string'},
                "description": {'type': 'string'},
                "imageUrl": {
                    'type': 'list', 'schema':
                        {
                            'type': 'string'
                        }
                },
                "price": {'type': 'integer'},
                "count": {'type': 'integer'},
                "tag": {
                    'type': 'list', 'schema':
                        {
                            'type': 'string'
                        }
                }
            }
        }
}
catalogue_by_id_response_schema = \
    {
        "id": {'type': 'string'},
        "name": {'type': 'string'},
        "description": {'type': 'string'},
        "imageUrl": {
            'type': 'list', 'schema': {
                'type': 'string'
            }
        },
        "price": {'type': 'integer'},
        "count": {'type': 'integer'},
        "tag": {
            'type': 'list', 'schema':
                {
                    'type': 'string'
                }
        }
    }

catalogue_by_size_response_schema = \
    {
        "size": {'type': 'integer'}
    }

catalogue_tags_response_schema = {
    "tags": {
        'type': 'list', 'schema': {
            'type': 'string'
        }
    }
}
