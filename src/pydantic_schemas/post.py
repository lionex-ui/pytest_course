from typing import Any

from pydantic import BaseModel, field_validator, Field


class Post(BaseModel):
    version: str = Field(alias="server_version")
    chain_id: str
    head_block_num: int
    last_irreversible_block_num: int
    last_irreversible_block_id: str
    head_block_id: str
    head_block_time: str
    head_block_producer: str
    virtual_block_cpu_limit: int
    virtual_block_net_limit: int
    block_cpu_limit: int
    block_net_limit: int
    server_version_string: str
    fork_db_head_block_num: int
    fork_db_head_block_id: str
    server_full_version_string: str
    total_cpu_weight: str
    total_net_weight: str
    earliest_available_block_num: int
    last_irreversible_block_time: str

    @field_validator("version")
    def version_content(cls, v: Any):
        if v != "04774eb7":
            raise ValueError("server_version is not equals 04774eb7")
        else:
            return v

    @field_validator("server_full_version_string")
    def server_full_version_string_content(cls, v: Any):
        if v != "v5.0.0-04774eb7726ae95a6cb795b493fcf0f25021bc5f":
            raise ValueError("server_version_string is not equals v5.0.0-04774eb7726ae95a6cb795b493fcf0f25021bc5f")
        else:
            return v

    @field_validator("server_version_string")
    def server_version_string_content(cls, v: Any):
        if v != "v5.0.0":
            raise ValueError("server_version_string is not equals v5.0.0")
        else:
            return v
