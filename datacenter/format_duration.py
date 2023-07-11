def format_duration(duration):
    hours = f'{int(duration // 3600)}'
    minutes = f'{int((duration % 3600) // 60)}'
    if int(minutes) < 10:
        minutes = f'0{minutes}'
    if int(hours) < 10:
        hours = f'0{hours}'
    return f'{hours}:{minutes}'
