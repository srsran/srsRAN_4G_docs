#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Intra Handover Flowgraph
# GNU Radio version: 3.9.0.0

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

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import zeromq
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import time



from gnuradio import qtgui

class s1_handover(gr.top_block, Qt.QWidget):

    def __init__(self, interval):
        gr.top_block.__init__(self, "S1 Handover Flowgraph", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("S1 Handover Flowgraph")
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

        self.settings = Qt.QSettings("GNU Radio", "s1_handover")

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
        self.samp_rate = samp_rate = 1.92e6
        self.cell_gain1 = cell_gain1 = 0
        self.cell_gain0 = cell_gain0 = 1

        ##################################################
        # Blocks
        ##################################################
        self._cell_gain1_range = Range(0, 1, 0.1, cell_gain1, 200)
        self._cell_gain1_win = RangeWidget(self._cell_gain1_range, self.set_cell_gain1, 'cell_gain1', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._cell_gain1_win)
        self._cell_gain0_range = Range(0, 1, 0.1, cell_gain0, 200)
        self._cell_gain0_win = RangeWidget(self._cell_gain0_range, self.set_cell_gain0, 'cell_gain0', "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_grid_layout.addWidget(self._cell_gain0_win)
        self.zeromq_req_source_1 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2001', 100, False, -1)
        self.zeromq_req_source_0_0 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2201', 100, False, -1)
        self.zeromq_req_source_0 = zeromq.req_source(gr.sizeof_gr_complex, 1, 'tcp://localhost:2101', 100, False, -1)
        self.zeromq_rep_sink_1_0 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2200', 100, False, -1)
        self.zeromq_rep_sink_1 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2100', 100, False, -1)
        self.zeromq_rep_sink_0 = zeromq.rep_sink(gr.sizeof_gr_complex, 1, 'tcp://*:2000', 100, False, -1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(cell_gain1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(cell_gain0)
        self.blocks_add_xx_0 = blocks.add_vcc(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.zeromq_rep_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.zeromq_rep_sink_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.zeromq_rep_sink_1_0, 0))
        self.connect((self.zeromq_req_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.zeromq_req_source_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.zeromq_req_source_1, 0), (self.blocks_throttle_0, 0))

        self.obj = Worker(interval)
        self.thread = Qt.QThread()
        self.obj.cell_gain_update.connect(self.update_cell_gain)
        self.obj.moveToThread(self.thread)
        self.thread.started.connect(self.obj.update)
        self.thread.finished.connect(self.obj.stop)
        self.thread.start()

    def update_cell_gain(self, cell, newValue):
        if (cell == 0):
            self._cell_gain0_win.d_widget.sliderChanged(newValue)
        elif (cell == 1):
            self._cell_gain1_win.d_widget.sliderChanged(newValue)


    def closeEvent(self, event):
        self.thread.quit()
        self.settings = Qt.QSettings("GNU Radio", "s1_handover")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_cell_gain1(self):
        return self.cell_gain1

    def set_cell_gain1(self, cell_gain1):
        self.cell_gain1 = cell_gain1
        self.blocks_multiply_const_vxx_0_0.set_k(self.cell_gain1)

    def get_cell_gain0(self):
        return self.cell_gain0

    def set_cell_gain0(self, cell_gain0):
        self.cell_gain0 = cell_gain0
        self.blocks_multiply_const_vxx_0.set_k(self.cell_gain0)  

  
   
class Worker(Qt.QObject):
    cell_gain_update = Qt.pyqtSignal(int, float)

    def __init__ (self, interval, active_cell = 0):
        super().__init__()
        self.active_cell = active_cell
        self.interval = interval

    def timerMethod(self):
        current_active_cell = 0
        next_active_cell = 1

        if (self.active_cell == 1):
            current_active_cell = 1
            next_active_cell = 0

        self.cell_gain_update.emit(current_active_cell, 0.500)
        
        for i in range(0, 10):
            self.cell_gain_update.emit(next_active_cell, (i + 1) * 0.100)
            time.sleep(self.interval)
        
        self.cell_gain_update.emit(current_active_cell, 0)

        self.active_cell = next_active_cell
        print("Handover made")

    @Qt.pyqtSlot()
    def update(self):
        self.timer = Qt.QTimer(self)
        self.timer.timeout.connect(self.timerMethod)

        # Add 10 seconds between each handover
        self.timer.start( ( (10 * self.interval) + 10 ) * 1000)

    @Qt.pyqtSlot()
    def stop(self):
        self.timer.stop()


def main(top_block_cls=s1_handover, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    interval = 4
    if (len(sys.argv) >= 2):
        interval = int(sys.argv[1])


    tb = top_block_cls(interval)

    tb.start()

    tb.show()

    
    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    qapp.exec_()

if __name__ == '__main__':
    main()
