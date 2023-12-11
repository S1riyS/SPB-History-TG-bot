from src.libs.checkpoint import Checkpoint
from src.libs.checkpoints_connector import CheckpointsConnector
from src.libs.route import Route
from src.libs.typing import CheckpointDetails
from src.libs.typing import RouteDetails

__checkpoints = [
    Checkpoint(
        details=CheckpointDetails(
            name="Первая точка",
            photo_path="",
            description="Длинной описание текущего чекпоинта...",
            location="ул. Пушкина 192",
        ),
        connector=CheckpointsConnector(
            itinerary_comment="Совсем недалеко есть...", itinerary_photo_path=""
        ),
    ),
    Checkpoint(
        details=CheckpointDetails(
            name="Вторая точка",
            photo_path="",
            description="Длинной описание второго чекпоинта...",
            location="ул. Пушкина 200",
        ),
        connector=CheckpointsConnector(
            itinerary_comment="QWEQWEQWEQWE", itinerary_photo_path=""
        ),
    ),
    Checkpoint(
        details=CheckpointDetails(
            name="Треться точка",
            photo_path="",
            description="Длинной описание третьего чекпоинта...",
            location="ул. Ленина 56",
        ),
        connector=CheckpointsConnector(
            itinerary_comment="Тут рядом находится...", itinerary_photo_path=""
        ),
    ),
]

route = Route(
    details=RouteDetails(
        name="Тестовое имя",
        map_photo_path="img.png",
        brief_description="Короткое описание маршрута",
        full_description='Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. '
                         'Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века. '
                         'В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, '
                         'используя Lorem Ipsum для распечатки образцов. '
                         'Lorem Ipsum не только успешно пережил без заметных изменений пять веков, '
                         'но и перешагнул в электронный дизайн.',
    ),
    checkpoints=__checkpoints,
)
