
import math
import time

round_2 = lambda x: round(x, -int(math.floor(math.log10(x))) + 1)

def format_time(epoch_time, seconds_left):
    time_local = time.localtime(epoch_time)
    if seconds_left < 600:
        return time.strftime('%H:%M:%S', time_local)
    elif seconds_left < 6000:
        return time.strftime('%H:%M', time_local)
    elif seconds_left < 60000:
        return time.strftime('%d %H', time_local)
    else:
        return time.strftime('%m-%d %H', time_local)

class LoopProgressMonitor(object):
    def __init__(self, n, tol = 0.1, patience_seconds = 5):
        '''
        :param n: The expected total number of steps in the loop
        '''
        self.n = n
        self.k = 0
        self.tol = tol
        self.patience_seconds = patience_seconds
        self.t0 = time.time()
        self.user_expected_seconds_left = 1e10
        self.last_update = -1e10

    def describe_time_left(self):
        #tol_seconds = self.tol * self.user_expected_seconds_left
        end = time.time() + self.user_expected_seconds_left # - tol_seconds
        #late_end = early_end + 2*tol_seconds
        str_seconds_per_iter =round_2(self.seconds_per_iteration)
        print('Est. finish ' + format_time(end, self.user_expected_seconds_left) +
              #' and ' + format_time(late_end, self.user_expected_seconds_left) +
              ' after ' + str(self.n - self.k) +
              ' iters at ' + str(str_seconds_per_iter) +
              ' sec/iter')

    def __call__(self):
        if self.k == 0:
            print('Starting first of ' + str(self.n) + ' iterations ...')
        else:
            now = time.time()
            total_seconds = now - self.t0
            self.seconds_per_iteration = total_seconds/self.k
            expected_seconds_left = (self.n - self.k)*self.seconds_per_iteration
            self.user_expected_seconds_left -= self.seconds_per_iteration
            error_seconds = abs(self.user_expected_seconds_left - expected_seconds_left)
            tol_fail = (error_seconds/self.user_expected_seconds_left > self.tol)
            silence = now - self.last_update
            if tol_fail and (silence > self.patience_seconds):
                self.user_expected_seconds_left = expected_seconds_left
                self.describe_time_left()
                self.last_update = now
        self.k += 1