from starlette.endpoints import HTTPEndpoint
from starlette.responses import HTMLResponse


class HomeEndpoint(HTTPEndpoint):
    async def get(request):
        return HTMLResponse("<p>Movies</p>")
