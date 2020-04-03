from selenium.webdriver.support.wait import WebDriverWait
from capability import driver, NoSuchElementException
from log import log
from login import login
from time import sleep


# 获取屏幕尺寸
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


# 滑动
def swipe(x, y, x0, y0):
    x = x
    y = y
    x0 = x0
    y0 = y0
    l = getSize()
    x1 = int(l[0] * x)
    y1 = int(l[1] * y)
    x2 = int(l[0] * x0)
    y2 = int(l[1] * y0)
    driver.swipe(x1, y1, x2, y2, 500)


def openAntFroest():
    log.logger.info('进入蚂蚁森林')
    try:
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@text=\'蚂蚁森林\']').click()
        driver.implicitly_wait(10)
    except NoSuchElementException:
        log.logger.info('蚂蚁森林打开失败')


def openFriendsList():
    log.logger.info('查找好友列表')
    sleep(3)
    swipe(0.5, 0.9, 0.5, 0.1)
    sleep(0.5)
    swipe(0.5, 0.9, 0.5, 0.1)
    try:
        # swipe(0.5, 0.9, 0.5, 0.5)
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@text=\'查看更多好友\']').click()
        driver.implicitly_wait(10)
        friendsLists = driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                     '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                     '.RelativeLayout/android.widget.RelativeLayout['
                                                     '2]/android.widget.RelativeLayout/android.widget.RelativeLayout'
                                                     '/android.widget.FrameLayout/com.uc.webview.export.WebView/com'
                                                     '.uc.webkit.ax/android.webkit.WebView/android.view.View/android'
                                                     '.view.View/android.view.View[2]/android.view.View')

        friendsNum = friendsLists
    except NoSuchElementException:
        log.logger.info('没找到好友')
    else:
        log.logger.info('好友共有%s人' % len(friendsNum))
        return friendsNum


def clickFriendsPage(num):
    driver.implicitly_wait(10)
    friendsLists = driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                 '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                 '.RelativeLayout/android.widget.RelativeLayout['
                                                 '2]/android.widget.RelativeLayout/android.widget.RelativeLayout'
                                                 '/android.widget.FrameLayout/com.uc.webview.export.WebView/com'
                                                 '.uc.webkit.ax/android.webkit.WebView/android.view.View/android'
                                                 '.view.View/android.view.View[2]/android.view.View')
    driver.implicitly_wait(10)
    name = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                                        '.RelativeLayout['
                                        '2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android'
                                        '.widget.FrameLayout/com.uc.webview.export.WebView/com.uc.webkit.ax/android'
                                        '.webkit.WebView/android.view.View/android.view.View/android.view.View['
                                        '1]/android.view.View/android.view.View['
                                        '3]/android.view.View/android.view.View').text

    driver.implicitly_wait(10)
    add = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android' \
          '.widget.RelativeLayout/android.widget.RelativeLayout[' \
          '2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/com.uc.webview' \
          '.export.WebView/com.uc.webkit.ax/android.webkit.WebView/android.view.View/android.view.View/android.view' \
          '.View[2]/android.view.View[' + str(num + 1) + ']/android.view.View[3]/android.view.View[' \
                                                         '1]/android.view.View '

    friendName = driver.find_element_by_xpath(add).text
    log.logger.info('进入第%s个好友%s的森林' % (num + 1, friendName))

    driver.implicitly_wait(10)
    if name == friendName:
        log.logger.info('第%s为自己的森林,跳过' % (num + 1))
        return False
    else:
        friendsLists[num].click()
        return True


def back():
    log.logger.info('返回')
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.alipay.mobile.nebula:id/h5_tv_nav_back').click()
    sleep(2)


def stealEnergy():
    log.logger.info('判断是否有能量')
    driver.implicitly_wait(10)

    items = driver.find_elements_by_class_name('android.widget.Button')
    if len(items) > 5:
        for i in items:
            if '能量' in i.text:
                log.logger.info('收取{1}'.format(i.text.replace('收集', '')))
                i.click()
        back()
    else:
        back()


if __name__ == '__main__':
    login('', '')
    openAntFroest()
    lists = openFriendsList()
    driver.implicitly_wait(10)

    for num in range(len(lists)):
        reName=clickFriendsPage(num)
        if not reName:
            pass
        else:
            stealEnergy()
        sleep(1)
        # back()
        swipe(0.5, 0.5, 0.5, 0.4)
    log.logger.info('收取完成')