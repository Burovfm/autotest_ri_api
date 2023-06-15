schema_request_create_application = {
    "type": "object",
    "default": {},
    "title": "Root Schema",
    "required": [
        "success"
    ],
    "properties": {
        "success": {
            "type": "boolean",
            "default": "false",
            "title": "The success Schema",
            "examples": [
                "true"
            ]
        }
    },
    "examples": [{
        "success": "true"
    }]
}

schema_response_error = {
    "type": "object",
    "required": [
        "error"
    ],
    "properties": {
        "error": {
            "type": "string",
        }
    }
}