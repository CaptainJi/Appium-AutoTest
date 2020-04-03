from selenium.webdriver.support.wait import WebDriverWait
from capability import driver, NoSuchElementException
from log import log


def login(username, password):
    username = username
    password = password
    log.logger.info(' ========================开始登录========================')
    # 判断是否登陆成功
    try:
        # 隐示等待
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@text=\'蚂蚁森林\']')
        log.logger.info('登陆成功')
    except NoSuchElementException:
        # 跳过温馨提示
        try:
            log.logger.info('跳过温馨提示')
            # driver.find_element_by_xpath('//*[@text=\'温馨提示\']')
            driver.find_element_by_xpath('//*[@text=\'同意\']').click()
        except NoSuchElementException:
            log.logger.info('未找到温馨提示')
        # 显示等待“其他登录方式”元素
        WebDriverWait(driver, 5).until(
            lambda x: x.find_element_by_xpath('//*[@text=\'其他登录方式\']'))
        # 尝试使用“其他登录方式”登录
        try:

            driver.find_element_by_xpath('//*[@text=\'其他登录方式\']').click()
            log.logger.info('使用账号密码登录')
        except NoSuchElementException:
            log.logging.info('未找到其他登录方式')
        # 控制输入账号及密码
        try:
            log.logger.info('输入账号')
            usernameText = driver.find_element_by_id(
                'com.ali.user.mobile.security.ui:id/userAccountInput')
            usernameText.find_element_by_id(
                'com.ali.user.mobile.security.ui:id/content').send_keys(username)
            driver.find_element_by_id(
                'com.ali.user.mobile.security.ui:id/nextButton').click()
        except NoSuchElementException:
            log.logger.info('未找到账号输入框')
        try:
            try:
                driver.implicitly_wait(5)
                log.logger.info('输入密码')
                passwordText = driver.find_element_by_id(
                    'com.ali.user.mobile.security.ui:id/userPasswordInput')
                passwordText.find_element_by_id(
                    'com.ali.user.mobile.security.ui:id/content').send_keys(password)
                driver.find_element_by_id(
                    'com.ali.user.mobile.security.ui:id/loginButton').click()
            except NoSuchElementException:
                log.logger.info('未找到密码输入框')
        except NoSuchElementException:
            log.logger.info('更换登录方式为密码')
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath('//*[@text=\'换个方式登录\']'))
            driver.find_element_by_xpath('//*[@text=\'换个方式登录\']').click()
            driver.find_element_by_xpath('//*[@text=\'密码登录\']').click()
            driver.find_element_by_id(
                'com.ali.user.mobile.security.ui:id/content').send_keys(password)
            driver.find_element_by_id(
                'com.ali.user.mobile.security.ui:id/loginButton').click()
        # 取消升级
        try:
            log.logger.info('取消升级')
            driver.find_element_by_xpath('//*[@text=\'稍后再说\']').click()
            log.logger.info('========================登陆成功========================')
        except NoSuchElementException:
            log.logger.info('========================登陆成功========================')


if __name__ == "__main__":
    login('', '')
