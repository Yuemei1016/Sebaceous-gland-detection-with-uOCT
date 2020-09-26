import os
import logging
import time

def create_logger(curr_path, cfg_file, cfg):
    # set up logger
    root_output_path = os.path.join(curr_path, 'output')
    if not os.path.exists(root_output_path):
        os.makedirs(root_output_path)
    assert os.path.exists(root_output_path), '{} does not exist'.format(root_output_path)

    cfg_name = os.path.basename(cfg_file).split('.')[0]
    config_output_path = os.path.join(root_output_path, '{}'.format(cfg_name))
    if not os.path.exists(config_output_path):
        os.makedirs(config_output_path)

    image_sets = [iset for iset in cfg.image_sets.split('+')]
    final_output_path = os.path.join(config_output_path, '{}'.format('_'.join(image_sets)))
    if not os.path.exists(final_output_path):
        os.makedirs(final_output_path)

    log_file = '{}_{}.log'.format(cfg_name, time.strftime('%Y-%m-%d-%H-%M'))
    head = '%(asctime)-15s %(message)s'
    logging.basicConfig(filename=os.path.join(final_output_path, log_file), format=head)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    return logger, final_output_path