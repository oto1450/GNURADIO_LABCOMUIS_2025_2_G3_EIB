import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """Bloque para calcular media y desviación estándar de la amplitud"""

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name="Estadísticas de Amplitud",
            in_sig=[(np.complex64, 512)],  # entrada: vector complejo (longitud configurable)
            out_sig=[np.float32, np.float32]  # salidas: media y desviación estándar
        )

    def work(self, input_items, output_items):
        in0 = input_items[0]  # forma: (N, 1024)
        mean_out = output_items[0]
        std_out = output_items[1]

        for i, vec in enumerate(in0):
            # Calcular magnitudes
            magnitudes = np.abs(vec)

            # Media de amplitud
            mean_amp = np.mean(magnitudes)

            # Desviación estándar de amplitud
            std_amp = np.std(magnitudes)

            # Asignar resultados a las salidas
            mean_out[i] = mean_amp
            std_out[i] = std_amp

        # Retornar el número de elementos producidos
        return len(mean_out)