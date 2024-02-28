import logging
import wyrm

# logging.config.fileConfig('./wyrm_logging_example.ini')
# wyrm = wyrm.core._base.Wyrm(debug=True)
# y = wyrm.pulse(x=2)

logger = logging.getLogger('wyrm_logging_example')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('wyrm_logging_example.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
wyrm = wyrm.Wyrm()

logger.info('calling wyrm.pulse')
y = wyrm.pulse(2)
print(y)

# # logger.info('creating an instance of wyrm.core._base.Wyrm')
# wyrm = wyrm.core._base.Wyrm(max_pulse_size=2, debug=True)
# logger.info('created an instance of wyrm.core._base.Wyrm')

# logger.info('calling Wyrm.pulse')
# y = wyrm.pulse(x=2)
# print(f'pulse returned y = {y}')
# logger.info('finished Wyrm.pulse')