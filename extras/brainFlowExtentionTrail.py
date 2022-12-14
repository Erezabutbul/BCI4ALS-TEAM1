import time
import pandas as pd
from brainflow.board_shim import BoardShim, BrainFlowInputParams

BoardShim.enable_dev_board_logger()

params = BrainFlowInputParams()
params.ip_port = 6677
params.serial_port = "COM5"
# params.ip_address = args.ip_address
# params.ip_protocol = args.ip_protocol
# params.timeout = args.timeout
# params.file = args.file

board = BoardShim(2, params)
board.prepare_session()

# board.start_stream () # use this for default options
board.start_stream(45000)
time.sleep(10)
# data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
data = board.get_board_data()  # get all data and remove it from internal buffer
# EEGData = dict()
# EEGData["EEGNames"] = board.get_eeg_names(board.board_id)
# EEGData["EEGChannels"] = board.get_eeg_channels(board.board_id)
board.stop_stream()
board.release_session()
# df = pd.DataFrame(EEGData)
# df.to_csv("generated_data",index=True, index_label="index", encoding="utf_8_sig")
print(data)
print()