import os
import argparse

from src.fast5_utils import OsBp_FAST5
from src.signal_utils import get_signal_pA, detect_events


duration = (4, 1000)
min_thresh_i = 0.30
strict_thresh_i = 0.60


def start_detection(file_in, channel_query):
	'''
	:param file_in: String - location of FAST5
	:param channel_query - Iter<Int>
	:return: Void
	'''
	with OsBp_FAST5(file_in) as g:
		for channel_no in channel_query:
			print('Processing channel {}...'.format(channel_no))
			info_obj = g.get_channel_raw(channel_no)
			signal_ary = get_signal_pA(info_obj)
			detect_out = detect_events(signal_ary, t_range=duration, min_depth_range=(0.0, min_thresh_i), strict_depth=strict_thresh_i)
			open_pA = detect_out['open_current']
			if open_pA != -1.0 and open_pA >= 200.0:
				print('# Channel {}, Sampling rate: {} Hz, Io: {} pA\n'.format(channel_no, info_obj.sampling_rate, open_pA))
				for event_id, event_idx in enumerate(detect_out['event_idx'], start=1):
					start, end = event_idx
					this_event = signal_ary[start:end]
					min_pA = min(this_event)
					print('{}\t{}\t{}\t{}'.format(event_id, start, end, min_pA / open_pA))
			print('')

					
def main():
	parser = argparse.ArgumentParser(description='Detect events corresponding to short, single miRNA translocations')
	parser.add_argument('-i', required=True, help='Input FAST5')
	parser.add_argument('-r', required=False, help='Range of channels to analyse - format: {}-{}')
	parser.add_argument('-s', required=False, help='Specific channels to analyse - channel numbers separated by commas')
	parser.add_argument('-b', required=False, help='Blacklisted channels - channel numbers separated by commas')
	args = parser.parse_args()
	
	# Validate CLI
	
	search_file = os.path.abspath(args.i)
	assert os.path.exists(search_file), 'The file does not exist - please check and try again'
	
	iter_range = []
	assert not ( (args.r is not None) and (args.s is not None) ), 'You cannot use both parameters -r and -s : choose one'
	if args.r is not None:
		raw_range_split = args.r.split('-')
		assert len(raw_range_split) == 2 and all(s.isnumeric() for s in raw_range_split), 'Invalid range - see help for range format'
		start_rge, end_rge = int(raw_range_split[0]), int(raw_range_split[1])
		iter_range = [i for i in range(start_rge, end_rge)]
	if args.s is not None:
		raw_whitelst_split = args.s.split(',')
		assert all(s.isnumeric() for s in raw_whitelst_split), 'Invalid whitelist - comma-separated integers required'
		iter_range = [int(s) for s in raw_whitelst_split]
	
	channel_blklst = []
	if args.b is not None:
		raw_blklst_split = args.b.split(',')
		assert all(s.isnumeric() for s in raw_blklst_split), 'Invalid blacklist - comma-separated integers required'
		channel_blklst = [int(s) for s in raw_blklst_split]
		
	# Run pipeline
		
	start_detection(search_file, [i for i in iter_range if i not in channel_blklst])
	

if __name__ == "__main__":
	main()
	
