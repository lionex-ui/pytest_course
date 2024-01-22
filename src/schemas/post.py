POST_SCHEMA = {
    "type": "object",
    "properties": {
        "server_version": {
            "type": "string",
            "enum": ["04774eb7"]
        },
        "chain_id": {
            "type": "string"
        },
        "head_block_num": {
            "type": "number"
        },
        "last_irreversible_block_num": {
            "type": "number"
        },
        "last_irreversible_block_id": {
            "type": "string"
        },
        "head_block_id": {
            "type": "string"
        },
        "head_block_time": {
            "type": "string"
        },
        "head_block_producer": {
            "type": "string"
        },
        "virtual_block_cpu_limit": {
            "type": "number"
        },
        "virtual_block_net_limit": {
            "type": "number"
        },
        "block_cpu_limit": {
            "type": "number"
        },
        "block_net_limit": {
            "type": "number"
        },
        "server_version_string": {
            "type": "string",
            "enum": ["v5.0.0"]
        },
        "fork_db_head_block_num": {
            "type": "number"
        },
        "fork_db_head_block_id": {
            "type": "string"
        },
        "server_full_version_string": {
            "type": "string",
            "enum": ["v5.0.0-04774eb7726ae95a6cb795b493fcf0f25021bc5f"]
        },
        "total_cpu_weight": {
            "type": "string"
        },
        "total_net_weight": {
            "type": "string"
        },
        "earliest_available_block_num": {
            "type": "number"
        },
        "last_irreversible_block_time": {
            "type": "string"
        }
    },
    "required": ["server_version", "server_version_string"],
    "additionalProperties": False
}
