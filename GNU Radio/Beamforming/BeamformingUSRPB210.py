#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: BeamformingUSRPB210
# Author: Juan Mateo Alban Mendez
# GNU Radio version: v3.8.2.0-57-gd71cd177

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
import epy_block_0_0
import epy_block_0_1_0
import epy_block_0_1_0_0
import epy_block_1
import epy_block_1_1

from gnuradio import qtgui

class BeamformingUSRPB210(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BeamformingUSRPB210")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BeamformingUSRPB210")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "BeamformingUSRPB210")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 500e3
        self.phaseUSRP = phaseUSRP = 0
        self.RF_Gain2 = RF_Gain2 = 20
        self.RF_Gain = RF_Gain = 70
        self.Frequency = Frequency = 2.45e9

        ##################################################
        # Blocks
        ##################################################
        self._phaseUSRP_range = Range(-3.2, 3.2, 0.01, 0, 200)
        self._phaseUSRP_win = RangeWidget(self._phaseUSRP_range, self.set_phaseUSRP, 'phaseUSRP', "counter_slider", float)
        self.top_grid_layout.addWidget(self._phaseUSRP_win)
        self._RF_Gain2_range = Range(0, 90, 1, 20, 200)
        self._RF_Gain2_win = RangeWidget(self._RF_Gain2_range, self.set_RF_Gain2, 'RF_Gain2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._RF_Gain2_win)
        self._RF_Gain_range = Range(0, 90, 1, 70, 200)
        self._RF_Gain_win = RangeWidget(self._RF_Gain_range, self.set_RF_Gain, 'RF_Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._RF_Gain_win)
        self._Frequency_range = Range(600e6, 2.50e9, 1000, 2.45e9, 200)
        self._Frequency_win = RangeWidget(self._Frequency_range, self.set_Frequency, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Frequency_win)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
            ",".join(("serial=30ECBB4", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
        )
        self.uhd_usrp_source_0_0.set_time_source('external', 0)
        self.uhd_usrp_source_0_0.set_clock_source('external', 0)
        self.uhd_usrp_source_0_0.set_center_freq(2e9, 0)
        self.uhd_usrp_source_0_0.set_rx_agc(False, 0)
        self.uhd_usrp_source_0_0.set_gain(RF_Gain2, 0)
        self.uhd_usrp_source_0_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0_0.set_bandwidth(200e3, 0)
        self.uhd_usrp_source_0_0.set_center_freq(2e9, 1)
        self.uhd_usrp_source_0_0.set_gain(20, 1)
        self.uhd_usrp_source_0_0.set_antenna('RX2', 1)
        self.uhd_usrp_source_0_0.set_bandwidth(1e3, 1)
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("serial=30ECB92", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
        )
        self.uhd_usrp_source_0.set_time_source('external', 0)
        self.uhd_usrp_source_0.set_clock_source('external', 0)
        self.uhd_usrp_source_0.set_center_freq(2e9, 0)
        self.uhd_usrp_source_0.set_rx_agc(False, 0)
        self.uhd_usrp_source_0.set_gain(RF_Gain2, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_bandwidth(200e3, 0)
        self.uhd_usrp_source_0.set_center_freq(2e9, 1)
        self.uhd_usrp_source_0.set_gain(20, 1)
        self.uhd_usrp_source_0.set_antenna('RX2', 1)
        self.uhd_usrp_source_0.set_bandwidth(1e3, 1)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
            ",".join(("serial=30ECBB4", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
            '',
        )
        self.uhd_usrp_sink_0_0.set_time_source('external', 0)
        self.uhd_usrp_sink_0_0.set_clock_source('external', 0)
        self.uhd_usrp_sink_0_0.set_center_freq(2.45e9, 0)
        self.uhd_usrp_sink_0_0.set_gain(RF_Gain, 0)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0_0.set_bandwidth(200e3, 0)
        self.uhd_usrp_sink_0_0.set_center_freq(Frequency, 1)
        self.uhd_usrp_sink_0_0.set_gain(RF_Gain, 1)
        self.uhd_usrp_sink_0_0.set_antenna('TX/RX', 1)
        self.uhd_usrp_sink_0_0.set_bandwidth(200e3, 1)
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("serial=30ECB92", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
            '',
        )
        self.uhd_usrp_sink_0.set_time_source('external', 0)
        self.uhd_usrp_sink_0.set_clock_source('external', 0)
        self.uhd_usrp_sink_0.set_center_freq(2.45e9, 0)
        self.uhd_usrp_sink_0.set_gain(RF_Gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_bandwidth(200e3, 0)
        self.uhd_usrp_sink_0.set_center_freq(Frequency, 1)
        self.uhd_usrp_sink_0.set_gain(RF_Gain, 1)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 1)
        self.uhd_usrp_sink_0.set_bandwidth(200e3, 1)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec())
        self.high_pass_filter_0_0 = filter.fir_filter_ccf(
            1,
            firdes.high_pass(
                1,
                samp_rate,
                40e3,
                10e3,
                firdes.WIN_HAMMING,
                6.76))
        self.high_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.high_pass(
                1,
                samp_rate,
                40e3,
                10e3,
                firdes.WIN_HAMMING,
                6.76))
        self.epy_block_1_1 = epy_block_1_1.blk()
        self.epy_block_1 = epy_block_1.blk()
        self.epy_block_0_1_0_0 = epy_block_0_1_0_0.blk(phase_correction=4.83)
        self.epy_block_0_1_0 = epy_block_0_1_0.blk(phase_correction=5)
        self.epy_block_0_0 = epy_block_0_0.blk(numeroAntenas=4, direccionMaximo=60.0, tipoArreglo=False, frecuencia=2450e6, phase_correctionUSRP=phaseUSRP)
        self.blocks_null_sink_4 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_3_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_cc(30)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(10)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_cc(100e-3)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_cc(100e-3)
        self.blocks_add_const_vxx_0_1 = blocks.add_const_cc(300e-3)
        self.blocks_add_const_vxx_0_0_0 = blocks.add_const_cc(300e-3)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 50e3, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.epy_block_1, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.epy_block_1_1, 0))
        self.connect((self.blocks_add_const_vxx_0_0_0, 0), (self.epy_block_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_1, 0), (self.epy_block_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_add_const_vxx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_const_vxx_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.epy_block_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.epy_block_1_1, 1))
        self.connect((self.epy_block_0_0, 3), (self.epy_block_0_1_0, 0))
        self.connect((self.epy_block_0_0, 1), (self.epy_block_0_1_0_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.epy_block_0_0, 2), (self.uhd_usrp_sink_0_0, 0))
        self.connect((self.epy_block_0_1_0, 0), (self.uhd_usrp_sink_0_0, 1))
        self.connect((self.epy_block_0_1_0_0, 0), (self.uhd_usrp_sink_0, 1))
        self.connect((self.epy_block_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.epy_block_1_1, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.high_pass_filter_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.uhd_usrp_source_0, 1), (self.blocks_null_sink_4, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.high_pass_filter_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 1), (self.blocks_null_sink_3_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.high_pass_filter_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "BeamformingUSRPB210")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, 40e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.high_pass_filter_0_0.set_taps(firdes.high_pass(1, self.samp_rate, 40e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)

    def get_phaseUSRP(self):
        return self.phaseUSRP

    def set_phaseUSRP(self, phaseUSRP):
        self.phaseUSRP = phaseUSRP
        self.epy_block_0_0.phase_correctionUSRP = self.phaseUSRP

    def get_RF_Gain2(self):
        return self.RF_Gain2

    def set_RF_Gain2(self, RF_Gain2):
        self.RF_Gain2 = RF_Gain2
        self.uhd_usrp_source_0.set_gain(self.RF_Gain2, 0)
        self.uhd_usrp_source_0_0.set_gain(self.RF_Gain2, 0)

    def get_RF_Gain(self):
        return self.RF_Gain

    def set_RF_Gain(self, RF_Gain):
        self.RF_Gain = RF_Gain
        self.uhd_usrp_sink_0.set_gain(self.RF_Gain, 0)
        self.uhd_usrp_sink_0.set_gain(self.RF_Gain, 1)
        self.uhd_usrp_sink_0.set_gain(self.RF_Gain, 2)
        self.uhd_usrp_sink_0.set_gain(self.RF_Gain, 3)
        self.uhd_usrp_sink_0_0.set_gain(self.RF_Gain, 0)
        self.uhd_usrp_sink_0_0.set_gain(self.RF_Gain, 1)
        self.uhd_usrp_sink_0_0.set_gain(self.RF_Gain, 2)
        self.uhd_usrp_sink_0_0.set_gain(self.RF_Gain, 3)

    def get_Frequency(self):
        return self.Frequency

    def set_Frequency(self, Frequency):
        self.Frequency = Frequency
        self.uhd_usrp_sink_0.set_center_freq(self.Frequency, 1)
        self.uhd_usrp_sink_0_0.set_center_freq(self.Frequency, 1)





def main(top_block_cls=BeamformingUSRPB210, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
