from selenium import webdriver
import time
import config

def main():
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(firefox_options=options)
    driver.get(config.CONFIG['targetURL'])

    UN = driver.find_element_by_id('email')
    UN.send_keys(config.CONFIG['email'])

    PS = driver.find_element_by_id('pass')
    PS.send_keys(config.CONFIG['password'])

    driver.find_element_by_id('loginbutton').click()

    try:
        driver.find_element_by_xpath("//*[contains(text(), '"+config.CONFIG['TimeRange']+"')]").click()
        time.sleep(1);
        driver.find_element_by_xpath("//*[contains(text(), '簽到!')]").click()
        print('簽到成功!')
    except:
        print('簽到失敗')
    finally:
        driver.save_screenshot('ConfirmScreen.png')
        driver.quit()

if __name__ == '__main__':
    main()