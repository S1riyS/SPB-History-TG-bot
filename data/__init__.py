import typing as t

from data.routes.test_route import route as first_route

if t.TYPE_CHECKING:
    from src.libs.route import Route

ROUTES: t.Dict[int, "Route"] = {
    0: first_route,
}
