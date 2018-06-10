
import math
import time

name = 'when_will_it_end'

round_2 = lambda x: round(x, -int(math.floor(math.log10(x))) + 1)

def format_time(epoch_time, seconds_left = 100):
    time_local = time.localtime(epoch_time)
    if seconds_left < 600:
        return time.strftime('%H:%M:%S', time_local)
    elif seconds_left < 6000:
        return time.strftime('%H:%M', time_local)
    elif seconds_left < 60000:
        return time.strftime('%d %H', time_local)
    else:
        return time.strftime('%m-%d %H', time_local)

def format_time_difference(seconds):
    h = round_2(seconds/3600)
    m = round_2(seconds/60)
    s = round_2(seconds)
    if seconds < 60:
        return str(s) + ' seconds'
    elif seconds < 3600:
        return str(m) + ' minutes'
    else:
        return str(h) + ' hours'

class LoopProgressMonitor(object):
    def __init__(self, n,
                 rel_tol_time_left = 0.1,
                 rel_tol_time_total=0.1,
                 patience_seconds = 5,
                 verbose = True):
        '''
        :param n: The expected total number of steps in the loop
        :param rel_tol_time_left (float): Don't bother to issue an update if the
        most recent report was within this fraction of the estimated time remaining
        :param patience_rel_time_total (float): Don't bother to issue an update if the most
        recent report was within this fraction of the current total estimated time
        :param patience_seconds (float): Don't bother to issue an update less than this long
        after the previous update
        '''
        self.n = n
        self.k = 0
        self.rel_tol_time_left = rel_tol_time_left
        self.rel_tol_time_total = rel_tol_time_total
        self.patience_seconds = patience_seconds
        self.user_expected_seconds_left = 1e10
        self.last_update = -1e10
        self.verbose = verbose
        self.t0 = time.time()

    def describe_time_left(self):
        end = time.time() + self.user_expected_seconds_left # - tol_seconds
        total_str = format_time_difference(end - self.t0)
        str_seconds_per_iter =round_2(self.seconds_per_iteration)
        print('Est. total ' + total_str +
              ', finish ' + format_time(end, self.user_expected_seconds_left) +
              ' after ' + str(self.n - self.k) +
              ' iters at ' + str(str_seconds_per_iter) +
              ' sec/iter')

    def __call__(self):
        if not self.verbose:
            return
        if self.k == 0:
            print('Starting first of ' + str(self.n) + ' iterations ...')
        else:
            now = time.time()
            total_seconds = now - self.t0
            self.seconds_per_iteration = total_seconds/self.k
            expected_seconds_left = (self.n - self.k)*self.seconds_per_iteration
            self.user_expected_seconds_left -= self.seconds_per_iteration
            total_time_left = expected_seconds_left + total_seconds
            error_seconds = abs(self.user_expected_seconds_left - expected_seconds_left)
            error_over_time_left = error_seconds/self.user_expected_seconds_left
            error_over_time_total = error_seconds/total_time_left
            silence = now - self.last_update
            if ((error_over_time_left  > self.rel_tol_time_left)
                    and (error_over_time_total > self.rel_tol_time_total)
                    and (silence > self.patience_seconds)):
                self.user_expected_seconds_left = expected_seconds_left
                self.describe_time_left()
                self.last_update = now
        self.k += 1
