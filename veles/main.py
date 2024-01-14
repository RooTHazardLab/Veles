"""
Veles bot
For now nothing interesting
"""

import os
import ssl
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

    print(req)

    return {"message": "kek"}


async def main():
    """
    Veles bot for now just start serving
    """

    veles_config = config.VelesConfig(os.environ["VELES_CONFIG_DIR"])

    notificaton_config = uvicorn.Config(
        "main:veles_api",
        ssl_cert_reqs=ssl.CERT_REQUIRED,
        ssl_ca_certs=veles_config.cfg.tls.ca,
        ssl_certfile=veles_config.cfg.tls.cert,
        ssl_keyfile=veles_config.cfg.tls.key,
        host="0.0.0.0",
        port=veles_config.cfg.port
    )

    notification_server = uvicorn.Server(notificaton_config)
    await asyncio.create_task(notification_server.serve())


if __name__ == "__main__":
    asyncio.run(main())
