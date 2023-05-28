import logging

log = logging.getLogger(__name__)
log.setLevel('DEBUG')

formatter = logging.Formatter(fmt='{asctime}:{levelname}:{name}:{message}', style='{')
file_handler = logging.FileHandler('src/log/log.log', mode='a', encoding='utf-8')
file_handler.setLevel('DEBUG')
file_handler.setFormatter(formatter)

log.addHandler(file_handler)