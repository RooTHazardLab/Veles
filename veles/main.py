"""
Veles bot
For now nothing interesting
"""

import os
import asyncio

import uvicorn
import fastapi

import config

veles_api = fastapi.FastAPI()

@veles_api.get("/")
async def notification(req: fastapi.Request):
    """
    Under development
    """

    print(req.headers)

    return {"message": "kek"}


async def main():
    """
    Veles bot for now just start serving
    """

    veles_config = config.VelesConfig(os.environ["SERVICE_CONFIG_DIR"])

    notificaton_config = uvicorn.Config(
        "main:veles_api",
        host="0.0.0.0",
        port=veles_config.cfg.port
    )

    notification_server = uvicorn.Server(notificaton_config)
    await asyncio.create_task(notification_server.serve())


if __name__ == "__main__":
    asyncio.run(main())
