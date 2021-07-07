import webbrowser

#  Variables

sa = True
oi = True
sec = True
ww = True
fin = True

web_list = [sa, oi, sec, ww, fin]  # Boolean array to track if to open or not to open website
web_links = ['https://seekingalpha.com/symbol/', 'http://openinsider.com/search?q=',
             'https://www.sec.gov/edgar/search/#/entityName=', 'https://whalewisdom.com/stock/',
             'https://finra-markets.morningstar.com/BondCenter/Default.jsp?part=3']


#  Functions

def open_websites(bool_list, stock_ticker):  # inputs are 2 lists, one list containing booleans, other to contain ticker
    for i in range(0, len(web_links)):  # runs loop for all vars in web_links
        if bool_list[i] is True:  # if the boolean says True, to open website, then run code
            webbrowser.open(str(web_links[i]) + str(stock_ticker[0]))  # opens website + ticker name at end


def open_test_website():
    webbrowser.open("https://seekingalpha.com/symbol/appl")


def web_links_len():
    len1 = len(web_links)
    return len1


def sa_is_true():
    return web_list[0]


def oi_is_true():
    return web_list[1]


def sec_is_true():
    return web_list[2]


def ww_is_true():
    return web_list[3]


def fin_is_true():
    return web_list[4]


def website_is_true_update(sa1, oi1, sec1, ww1, fin1):  # updates true/false booleans
    if (sa1 is True) or (sa1 is False):  # if inputs are booleans then no change
        web_list[0] = sa1
        web_list[1] = oi1
        web_list[2] = sec1
        web_list[3] = ww1
        web_list[4] = fin1

    elif sa1 == 1 or sa1 == 0:  # Converts 1 into true, 0 into false if it's not a boolean already
        if sa1 == 1:
            web_list[0] = True
        else:
            web_list[0] = False
        if sa1 == 1:
            web_list[1] = True
        else:
            web_list[1] = False
        if sa1 == 1:
            web_list[2] = True
        else:
            web_list[2] = False
        if sa1 == 1:
            web_list[3] = True
        else:
            web_list[3] = False
        if sa1 == 1:
            web_list[4] = True
        else:
            web_list[4] = False
