import datetime


def formatter_screenshots(data):
    result = []
    if data is not None:
        for item in data:
            result.append(item[17])
    return result


def formatter_users(data):
    if data:
        return int(data.replace(',', '').replace('+', ''))
    else:
        return 0


def formatter_date(date):
    time_format = datetime.datetime.strptime(date, '%B %d, %Y')
    return datetime.datetime.strftime(time_format, '%Y-%m-%d')


def formatter_free(data):
    if data == 'FREE':
        return 1
    else:
        return 2


def formatter_related(data):
    result = []
    if data:
        for item in data:
            value = {
                "id": item[0],
                "name": item[1],
                "icon": item[3],
                "url": item[37],
                "summary": item[6],
                "category": item[9],
                "category_name": item[10],
                "score": item[12],
                "ratings": item[22],
                "users": item[23],
                "developer_name": item[2],
                "developer_website":  item[81],
                "featured":  item[89],
            }
            result.append(value)
    return result
