import time, sqlite3

global count
global N
N = 1
count = 0


def keep_safe(driver, F_Login):
    try:
        F = 1
        while (F):
            if F_Login == 1:
                QR_Code = driver.find_element_by_xpath('//*[@id="container"]/h2').text
                txt = '安全校验'
            else:
                QR_Code = driver.find_element_by_xpath('/html/body/div/div[1]/div/h1/a[2]').text  # 1
                txt = '登录'
            if QR_Code == txt:
                print(txt)
                print('请在15s内扫码')
                if txt == '安全校验':
                    time.sleep(15)
                    QR_Code_2 = driver.find_element_by_xpath('//*[@id="container"]/h2').text
                    if QR_Code_2 == QR_Code:
                        F = 1
                    else:
                        F = 0
                elif txt == '登录':
                    time.sleep(15)
                    QR_Code_2 = QR_Code = driver.find_element_by_xpath('/html/body/div/div[1]/div/h1/a[2]').text
                    if QR_Code_2 == QR_Code:
                        F = 1
                    else:
                        F = 0
    except:
        pass


def getInfor(driver):
    global N
    for num in range(10):
        num = num + 1
        al_day_xpath = '//*[@id="J-item-' + str(num) + '"]/td[2]/p[1]'  # //*[@id="J-item-1"]/td[2]/p[1]    日期
        al_time_xpath = '//*[@id="J-item-' + str(num) + '"]/td[2]/p[2]'  # //*[@id="J-item-1"]/td[2]/p[2]    时刻
        al_way_xpath = '//*[@id="J-item-' + str(num) + '"]/td[3]/p[1]'  # //*[@id="J-item-1"]/td[3]/p[1]  方式
        al_payee_xpath = '//*[@id="J-item-' + str(num) + '"]/td[3]/p[2]'  # //*[@id="J-item-1"]/td[3]/p[2]/span 收款人
        al_snum_xpath = '//*[@id="J-tradeNo-' + str(num) + '"]'  # //*[@id="J-tradeNo-1"] 号#.get_attribute("title")
        al_figure_xpath = '//*[@id="J-item-' + str(num) + '"]/td[4]/span'  # //*[@id="J-item-1"]/td[4]/span 金额
        al_status_xpath = '//*[@id="J-item-' + str(num) + '"]/td[6]/p[1]'  # //*[@id="J-item-1"]/td[6]/p[1] 交易状态

        al_day = driver.find_element_by_xpath(al_day_xpath).text
        al_time = driver.find_element_by_xpath(al_time_xpath).text
        al_way = driver.find_element_by_xpath(al_way_xpath).text
        al_payee = driver.find_element_by_xpath(al_payee_xpath).text
        al_snum = driver.find_element_by_xpath(al_snum_xpath).get_attribute("title")
        al_figure = driver.find_element_by_xpath(al_figure_xpath).text
        al_status = driver.find_element_by_xpath(al_status_xpath).text

        conn = sqlite3.connect('zhifubaoDatabase.db')
        cursor = conn.cursor()

        cursor.execute(
            'create table if not exists alipayrecords(recordid INTEGER PRIMARY KEY NOT NULL,createtime text,'
            'gender char(100),ordernum int(40),expend char(50),operation char(50),output char(50))')
        selectsql = "select sum(recordid) from alipayrecords where ordernum = '" + al_way + "'"
        cursor.execute(selectsql)
        values = cursor.fetchall()
        if values[0][0] == None:
            sqlss = "insert into alipayrecords (createtime,gender,ordernum,expend,operation,output)" \
                    " values('" + al_day + "','" + al_time + "','" + al_way + "','" + al_payee + "','" + al_snum + "','" + al_figure + "')"
            cursor.execute(sqlss)
        cursor.close()
        conn.commit()
        conn.close()

        print(str(N) + '.' + '日期' + ':' + al_day + '\t时间' + ':' + al_time + '\t方式' + ':' + al_way + '\t收款人' + ':' + al_payee + '\t流水号' + ':' + al_snum + '\t金额' + ':' + al_figure + '\t交易状态' + ':' + al_status)
        N = N + 1


def isElementExist(driver, element):
    flag = True
    try:
        driver.find_element_by_xpath(element)
        return flag
    except:
        flag = False
        return flag


def searchDriver(driver):
    global count
    print("ssssssssssssssssssssssssssssssssss")
    cnt = 0
    if count > 0:
        time.sleep(60)
    count = count + 1
    for i in range(8):
        if cnt == 1:
            flag = isElementExist(driver, '//*[@id="J_home-record-container"]/div[2]/div/div[2]/div[2]/div/a[1]')
            if flag:
                elem = driver.find_element_by_xpath('//*[@id="J_home-record-container"]/div[2]/div/div[2]/div[2]/div/a[1]')
                cnt = cnt + 1
                elem.click()
            else:
                elem = driver.find_element_by_xpath('//*[@class="page fn-right"]/div[1]/a[1]')
                elem.click()
                break
        elif cnt == 0:
            cnt = cnt + 1
        else:
            print("cxcxcxcxcxcxcxcxcxcxccx")
            flag = isElementExist(driver,'//*[@id="J_home-record-container"]/div[2]/div/div[2]/div[2]/div/a[3]')
            if flag:
                elem = driver.find_element_by_xpath('//*[@id="J_home-record-container"]/div[2]/div/div[2]/div[2]/div/a[3]')
                elem.click()
            else:
                elem = driver.find_element_by_xpath('//*[@class="page fn-right"]/div[1]/a[1]')
                elem.click()
                break
        time.sleep(1)
        # keep_safe(driver)
        try:
            if driver:
                getInfor(driver)
            else:
                print('本次循环结束！')
                pass
        except:
            print('估计是没了！')
            pass
    searchDriver(driver)
