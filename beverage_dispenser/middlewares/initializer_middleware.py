import os
import uuid
from fastapi import Request
from beverage_dispenser.constants import env
from beverage_dispenser.providers.mongo import MongoDB

os.path.join(os.getcwd(), "beverage_dispenser")


class InitializerMiddleware:
    async def __call__(self, request: Request, call_next):
        self.get_origin(request)

        if "OPTIONS" in request.__dict__['scope']['method']:
            return await call_next(request)

        MongoDB()
        request.state.request_id = str(uuid.uuid4())
        return await call_next(request)

    def get_origin(self, request):
        request_origin = ''
        for header in request.__dict__['scope']['headers']:
            name = header[0].decode('utf-8')
            if name == 'origin':
                request_origin = header[1].decode('utf-8')
        request.state.origin = request_origin
