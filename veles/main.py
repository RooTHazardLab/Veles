"""
Veles bot
"""

import os
import json
import asyncio
import logging.config

import uvicorn
import fastapi
import fastapi.middleware.cors as cors_middleware

import config

import funds.routes

logger = logging.getLogger("veles")
veles_api = fastapi.FastAPI()

veles_api.include_router(funds.routes.router)

origins = [
    "*",
]

veles_api.add_middleware(
    cors_middleware.CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def veles():
    """
    Veles bot for now just start serving
    """

    veles_config = config.VelesConfig(
        f'{os.environ["SERVICE_CONFIG_DIR"]}/config.yaml'
    )

    veles_api_config = uvicorn.Config(
        "main:veles_api",
        host=veles_config.cfg.server.host,
        port=veles_config.cfg.server.port
    )

    veles_api_server = uvicorn.Server(veles_api_config)
    await asyncio.create_task(veles_api_server.serve())


def main():
    """Run async veles service"""

    with open(
        "veles/logging_config.json",
        encoding="utf-8"
    ) as logging_cgf_fd:
        logging_cfg = json.load(logging_cgf_fd)

    logging.config.dictConfig(logging_cfg)

    coroutine = veles()

    asyncio.run(coroutine)


if __name__ == "__main__":
    main()
