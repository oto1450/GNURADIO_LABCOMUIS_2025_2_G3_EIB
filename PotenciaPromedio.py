import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Potencia promedio',
            in_sig=[(np.complex64, 512)],
            out_sig=[np.float32]
        )

    def work(self, input_items, output_items):
        x = input_items[0]  # x tiene forma [N, 1024]
        N = 1024

        # Potencia promedio explícita: (1/N) * sum(|x[n]|^2)
        power = (1.0 / N) * np.sum(np.abs(x)**2, axis=1)

        output_items[0][:] = power.astype(np.float32)
        return len(output_items[0])