import time


def wait_until(predicate, message_on_fail=None, timeout=10, poll_frequency=0):
    start = time.time()
    while True:
        try:
            return_val = predicate()
            if return_val:
                return return_val
        except:
            time.sleep(0.1)
        if time.time() - start > timeout:
            raise AssertionError(f"Timeout occurred: {message_on_fail}")
        time.sleep(poll_frequency)
