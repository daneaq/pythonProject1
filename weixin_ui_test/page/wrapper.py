import time

from selenium import webdriver


#处理弹窗
def handle_black(func):
    def wrapper(*args,**kwargs):
        black_list = [("id","menu_contacts")]
        max_err =0
        try:
            return func(*args,**kwargs)
            err_num = 0
        except Exception as e:
            instance: webdriver = args[0]
            if err_num >= max_err:
                raise e
            for loc in black_list:
                black_elements = instance.finds(loc)
                length = len(black_elements)
                if length > 0:
                    black_elements[0].click()
            err_num +=1
            time.sleep(5)
            return func (*args,**kwargs)
    return wrapper