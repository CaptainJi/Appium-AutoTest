import logging, random
from common.desiredCaps import appium_desired
from common.commonFun import Common, By, NoSuchElementException
# 封装注册业务逻辑类


class RegisterView(Common):
    # 开始注册按钮
    register_text = (By.ID, 'com.tal.kaoyan:id/login_register_text')

    # 头像设置元素
    user_header = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    item_image = (By.ID, 'com.tal.kaoyan:id/item_image')
    save = (By.ID, 'com.tal.kaoyan:id/save')

    # 用户名、密码、邮箱元素
    register_username_edittext = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    register_password_edittext = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email_edittext = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    register_btn = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')

    # 完善资料元素
    school_name = (By.ID, 'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
    perfectinfomation_major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
    perfectinfomation_goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

    # 院校元素
    forum_title = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
    university = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')

    # 专业元素
    major_subject_title = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    major_group_title = (By.ID, 'com.tal.kaoyan:id/major_group_title')
    major_search_item_name = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')

    # 用户中心元素
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    usercenter_username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')

    def register_action(self, register_username, register_password, register_email):
        self.check_cancel_btn()
        self.check_skipBtn()

        logging.info('开始注册')
        self.driver.find_element(*self.register_text).click()

        logging.info('设置用户头像')
        self.driver.find_element(*self.user_header).click()
        self.driver.find_elements(*self.item_image)[1].click()
        self.driver.find_element(*self.save).click()

        logging.info('用户名为：%s' % register_username)
        self.driver.find_element(*self.register_username_edittext).send_keys(register_username)

        logging.info('密码为：%s' % register_password)
        self.driver.find_element(*self.register_password_edittext).click()
        self.driver.find_element(*self.register_password_edittext).send_keys(register_password)

        logging.info('邮箱为：%s' % register_email)
        self.driver.find_element(*self.register_email_edittext).click()
        self.driver.find_element(*self.register_email_edittext).send_keys(register_email)

        # 点击注册按钮
        self.driver.find_element(*self.register_btn).click()

        try:
            self.driver.find_element(*self.school_name)
        except NoSuchElementException:
            logging.info('注册失败')
            self.getScreenShot('注册失败')
            return False
        else:
            self.add_register_info()
            if self.check_register_status():
                return True
            else:
                return False

    def add_register_info(self):
        logging.info('添加注册信息')

        logging.info('选择学校')
        self.driver.find_element(*self.school_name).click()
        self.find_elements(*self.forum_title)[1].click()
        self.find_elements(*self.university)[1].click()

        logging.info('选择专业')
        self.driver.find_element(*self.perfectinfomation_major).click()
        self.find_elements(*self.major_subject_title)[1].click()
        self.find_elements(*self.major_group_title)[2].click()
        self.find_elements(*self.major_search_item_name)[1].click()

        logging.info('点击进入考研帮按钮')
        self.find_element(*self.perfectinfomation_goBtn).click()

    def check_register_status(self):
        logging.info('检查注册状态')
        self.check_market_ad()
        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.usercenter_username)
        except NoSuchElementException:
            logging.error('注册失败')
            self.getScreenShot('注册失败')
            return False
        else:
            logging.info('注册成功')
            return True


if __name__ == '__main__':
    driver = appium_desired()
    register = RegisterView(driver)

    username = 'Klieg' + str(random.randint(1000, 9000))
    password = 'SIegII' + str(random.randint(1000, 9000))
    email = 'kliegSIeg' + str(random.randint(1000, 9000)) + '@163.com'
    print(username)
    print(password)
    print(email)
    register.register_action(username, password, email)
