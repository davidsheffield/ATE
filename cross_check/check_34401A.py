import time

import numpy as np
import pandas as pd
import pyvisa


def check_34401A():
    """
    Check Agilent 34401A with four-wire short.
    """

    rm = pyvisa.ResourceManager()
    dmm = rm.open_resource('ASRL2::INSTR',
                           baud_rate=9600,
                           data_bits=7,
                           parity=pyvisa.constants.Parity.even,
                           stop_bits=pyvisa.constants.StopBits.two,
                           timeout=5000)
    if dmm.query('*idn?') != 'HEWLETT-PACKARD,34401A,0,11-5-2\r\n':
        raise RuntimeError('Did not find Agilent 34401A')
    dmm.write('system:remote')
    time.sleep(1)

    values = []
    for i in range(10):
        result = dmm.query('measure:voltage:dc? min,min')
        print(result, float(result))
        values.append(float(result))

    dmm.write('system:local')
    breakpoint()
    print('')


if __name__ == '__main__':
    check_34401A()
