import logging

def setup_logger():
    logging.basicConfig(filename='reports/attack_log.txt', level=logging.INFO,
                        format='%(asctime)s - %(message)s')
    return logging.getLogger()
