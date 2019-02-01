import os
from common.chrome_browser import driver
from common.my_logger import logger


def fail_run(n=2):
    def decorator(func):
        def wrapper(*args,**kw):
            for i in range(n):
                try:
                    r = func(*args,**kw)
                    return r
                except Exception as err:
                    logger.error('[{}]用例第{}次失败原因{}'.format(os.path.basename(__file__), i+1, err))
            raise Exception
        return wrapper
    return decorator


def one_browser_window():
    handles = driver.window_handles
    if len(handles) >= 1:
        for index in range(len(handles)-1, 0, -1):
            driver.switch_to.window(handles[index])
            driver.close()
        driver.switch_to.window(handles[0])
        driver.delete_all_cookies()
    else:
        pass
