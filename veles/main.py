"""
Veles bot
For now nothing interesting
"""

import os
import json
import asyncio
import logging.config

import uvicorn
import fastapi

import config

logger = logging.getLogger("veles")
veles_api = fastapi.FastAPI()

@veles_api.get("/")
async def root(req: fastapi.Request):
    """
    Under development
    """

    logger.info(req.headers)

    return {"message": "kek"}



async def veles():
    """
    Veles bot for now just start serving
    """

    veles_config = config.VelesConfig(
        f'{os.environ["SERVICE_CONFIG_DIR"]}/config.yaml'
    )

    notificaton_config = uvicorn.Config(
        "main:veles_api",
        host=veles_config.cfg.server.host,
        port=veles_config.cfg.server.port
    )

    notification_server = uvicorn.Server(notificaton_config)
    await asyncio.create_task(notification_server.serve())


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
