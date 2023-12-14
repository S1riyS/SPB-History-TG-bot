from src.libs.checkpoint import Checkpoint
from src.libs.checkpoints_connector import CheckpointsConnector
from src.libs.route import Route
from src.libs.typing import CheckpointDetails
from src.libs.typing import RouteDetails

__checkpoints = [
    Checkpoint(
        details=CheckpointDetails(
            name="Петропавловский собор",
            photo_path="route2_1_1.jpg",
            description="Петропавловская крепость - историческое ядро Санкт-Петербурга, где началась история города на Неве. Она была построена в начале XVIII века во время Северной войны. Крепость является укрепительным сооружением, созданным для защиты от нападений захватчиков. Строительство началось в 1703 году на Заячьем острове. Крепость была заложена 16-27 мая и считается основанной 27 мая, что стало Днем основания Санкт-Петербурга. \n Крепость была построена по плану Петра I и французского инженера Жозефа Гаспара Ламбера де Герена. Она была названа Санкт-Питер-бурх и считается историческим центром города. В этом же году, Петр I приказал построить деревянную церковь в крепости. Церковь была названа в честь апостолов Петра и Павла. Позже она была отделана камнем и получила статус собора. Петропавловский собор является православным храмом, усыпальницей русских императоров и памятником архитектуры петровского барокко. \n Собор был самым высоким зданием в Санкт-Петербурге до 2012 года. В настоящее время он занимает третье место по высоте. У собора есть 103 колокола, включая несколько, которые датируются 1757 годом. Собор изображен на задней стороне 50-рублевой российской купюры, а его шпиль украшает 'Летящий Ангел'. Собор также известен своим карильоном - колокольным органом, способным исполнять музыку. \n Петропавловский собор обладает множеством интересных легенд и мифов, включая слухи о усыпальнице рода Романовых. Надгробие Павла I считается особенно суеверным и прикосновение к нему предполагается исполняет желания и приносит удачу.",
            location="Петропавловская крепость",
        ),
        connector=CheckpointsConnector(
            itinerary_comment="Первая точка - Исаакиевская площадь, 4. Ближайшая станция метро Горьковская",
        ),
    ),

    Checkpoint(
        details=CheckpointDetails(
            name="Исаакиевский Собор",
            photo_path="route2_2_1.jpg",
            description="Исаакиевский Собор - одна из самых известных достопримечательностей города. Он занимает четвертое место по величине среди православных соборов в мире. Высота собора - 101,5 метра, диаметр купола - 26 метров. \n Первый храм был выполнен из дерева, однако такой материал был весьма недолговечен и в 1717 году Петр дал поручение немецкому архитектору Георгу Иоганну Маттарнови заменить деревянные стены на каменные. Третья попытка возродить собор была предпринята Екатериной ІІ. Следующим, кто предпринял попытку достроить собор,стал император Павел. Работу по строительству он поручил другому итальянцу — Винченцо Бренне. \n Следующим, кто взялся за строительство собора, это император Александр І. Проект французского архитектора Огюста Монферрана поразила Александра І. Строительство собора по проекту Монферрана было начато в 1818 году и продолжалось 40 лет. Оно проходило при трех императорах Александре I, Николае I и Александре II. Возведение собора было оконченов 1848 году, но еще около десяти лет было потрачено на отделку интерьера. Освящение собора, по случаю его открытия, было проведено 11 июня 1858 года. Для убранства собора использовался мрамор различных цветов, малахит, лазурит и другие ценные породы камня. Кроме икон, его стены украшали уникальные мозаики. Алтарь был сделан в форме витража. На нем изображен 'Воскресший Христос'. Эта работа является одной из самых крупных витражных работ в Европе. Парящий под куполом голубь символизирует Святой Дух. На первый взгляд хрупкая птица являет собой посеребренную бронзовую фигуру с размахом крыльев около двух метров.",
            location="Исаакиевская площадь, 4",
        ),
        connector=CheckpointsConnector(
            itinerary_comment="Следующая точка - Казанская площадь, 2. Идти пешком 11 минут",
            itinerary_photo_path="route2_1_2.jpg"
        ),
    ),

    Checkpoint(
        details=CheckpointDetails(
            name="Казанский собор",
            photo_path="route2_3_1.jpg",
            description="Казанский соборявляется одним из крупнейших храмов Санкт-Петербурга. Он был возведён в 1801—1811 годах архитектором Андреем Воронихиным. \n Строился храм для хранения чтимого списка чудотворной иконы Божией Матери Казанской, найденной в останках сгоревшего дома в Казани в конце XVI века.После Отечественной войны 1812 года Казанский собор приобрёл значение памятника русской воинской славы. В 1813 году здесь был похоронен полководец Михаил Илларионович Кутузов. \n Собор дал название Казанской улице, Казанскому острову в дельте Невы и Казанскому мосту на пересечении Невского проспекта и канала Грибоедова. Казанский кафедральный собор — памятник российского церковного зодчества особой значимости. Именно здесь было положено начало золотой эпохи российского храмового искусства.",
            location="Казанская площадь, 2, Санкт-Петербург",
        ),
        connector=CheckpointsConnector(
            itinerary_comment="Следующая точка наб. канала Грибоедова, 2Б, лит.А. Идти пешком 7 минут",
            itinerary_photo_path="route2_2_2.jpg"
        ),
    ),

    Checkpoint(
        details=CheckpointDetails(
            name="Спас-на-Крови",
            photo_path="route2_4_1.jpg",
            description="Городская дума Санкт-Петербурга выступила инициатором возведения Часовни на месте трагически погибшего императора Александра ІІ. Это решение поддержал сын императора — Александр ІІІ, и уже 17 апреля 1881 года, в день рождения Александра ІІ, была освящена деревянная часовня. В этой часовне ежедневно служили панихиду об упокоении души императора. На этом месте часовня просуществовала до начала возведения храма — 1883 года. \n Собор был заложен 6 октября 1883 года в присутствии императора Александра ІІІ и императрицы Марии Федоровны. Первый камень был возложен самим императором. Строительство собора было растянуто почти на два с половиной десятилетия. \n Интерьер собора — это великолепное сочетание мозаичного и каменного убранства. Внутри храм выглядит как сказочная шкатулка. Мозаика чудесным образом вписывается в святые интерьеры Спаса-на-Крови. \n Мозаичные композиции Спаса-на-Крови представляют большую художественную ценность, также их масштабность поражает всякое воображение. Мозаикой снаружи выложено 400 м2 фасадов, внутри ею оформлено 7065 м2.  Профессор Покровский сравнил его с храмами византийскими, римскими, равеннскими и сицилийскими, и признал, что даже в них нет такого мозаичного богатства. \n Храм Воскресения Христова не лишен мифов и легенд. Последнее придание гласит о чудесной иконе, которая являет роковые для истории России даты: 1917, 1941, 1953. Согласно этому приданию, если внимательно присмотреться, то можно увидеть и следующие года, но их пока никто расшифровать не смог. Наверное, это и к лучшему, так как тайна должна оставаться тайной",
            location="наб. канала Грибоедова, 2Б, лит.А",
        ),
        connector=CheckpointsConnector(
            itinerary_comment="Следующая точка - площадь Растрелли, 1. Ближайшая станция метро Невский проспект",
            itinerary_photo_path="route2_3_2.jpg"
        ),
    ),

    Checkpoint(
        details=CheckpointDetails(
            name="Смольный собор",
            photo_path="route2_5_1.jpg",
            description="Смольный собор - православный храм, часть ансамбля Смольного монастыря в Санкт-Петербурге. \n Накануне своего 40-летия императрица Елизавета Петровна решила уйти от суеты и провести остаток своих дней в стенах монастыря. Она дала распоряжение о строительстве монастыря для 120 девиц из благородных семей. Для себя как будущей настоятельницы она велела построить отдельный дом. \n Строительство началось в 1744 году по проекту архитектора Франческо Бартоломео Растрелли. Основные работы были завершены в 1775 году, а окончательная отделка произошла при правлении Николая I. \n Смольный собор впечатляет своим величием и архитектурой, сочетающей барокко и классицизм. Сегодня он считается красивейшим и величественным сооружением",
            location="площадь Растрелли, 1",
        ),
        connector=CheckpointsConnector(
            itinerary_comment="Следующаая точка наб. реки Монастырки, 1Г. Ближайшая станция метро Чернышевская",
            itinerary_photo_path="route2_4_2.jpg"
        ),
    ),
    Checkpoint(
        details=CheckpointDetails(
            name="Свято-Троицкая Александро-Невская Лавра",
            photo_path="route2_6_1.jpg",
            description="Первый и наиболее крупный монастырь Санкт-Петербурга. В состав архитектурного комплекса входит несколько знаменитых некрополей В летописях часто пишут, часто пишут, что Невский монастырь заложил сам Пётр I. В июле 1710 года государь осмотрел место впадения Чёрной речки в Неву и издал указ строить здесь монастырь. Учитывая, что обитель строилась в разгар войны со Швецией на отвоёванных землях, историческая перекличка весьма показательна. \n В первой четверти XVIII века место расположения Александро-Невской Лавры выбиралось зодчим Доменико Трезини в треугольнике между реками Невой, Монастыркой и Обводным каналом отнюдь не случайно. Ранее считалось, что именно здесь в 1240 году Александр Невский со своим войском разгромил шведов. Идея строительства возникла у Петра Великого в 1704 году в период Северной войны опять-таки со шведами. Таким образом, император желал увековечить победы русской дружины над неприятелем. \n Официальной датой основания считается освящение в праздник Благовещения Пресвятой Богородицы 25 марта 1713 года деревянной Благовещенской церкви. \n В 1723 году Пётр I посетил вновь устроенный монастырь и повелел перенести мощи князя Александра из Владимирского Рождественского монастыря в новую столицу. Останки князя прибыли в Санкт-Петербург 30 августа 1724 года, в память о чём в календарь Русской церкви был введён новый праздник",
            location="наб. реки Монастырки, 1Г",
        ),
        connector=CheckpointsConnector(
            itinerary_comment="На этом завершаем нашу экскурсии. Отсюда до ближайшей станции метро Площадь Александра Невского идти 4 минуты",
            itinerary_photo_path="route2_5_2.jpg"
        ),
    ),

]

route = Route(
    details=RouteDetails(
        name="Сокральный Санкт-Петербург",
        map_photo_path="route2_0.jpg",
        brief_description="Маршрут по главным святыням Санкт-Петербург",
        full_description="Маршрут пеший, протяжённостью — 13 километра, рассчитан на длительность примерно — 4 часа. Начинаем экскурсию по святым местам с самого первого и знакового, символичного и важного, исторического и духовного. Это то место, с которого возник, вырос, создавался, строился и формировался великий Санкт-Петербург — Петропавловская крепость. Для этого нужно выйти на станции метро Горьковская, и следовать по нашему маршруту."
    ),
    checkpoints=__checkpoints,
)
