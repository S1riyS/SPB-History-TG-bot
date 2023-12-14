import typing as t

from data.routes.test_route import route as first_route
from data.routes.route2 import route as second_route
from data.routes.route1 import route as third_route

if t.TYPE_CHECKING:
    from src.libs.route import Route

ROUTES: t.Dict[int, "Route"] = {
    0: first_route,
    1: second_route,
    2: third_route,
}
