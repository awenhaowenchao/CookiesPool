# Redis数据库地址
REDIS_HOST = 'localhost'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

# 产生器使用的浏览器
BROWSER_TYPE = 'Chrome'

# 产生器类，如扩展其他站点，请在此配置
GENERATOR_MAP = {
    #'weibo': 'WeiboCookiesGenerator',
    'videorank': 'VideoRankCookiesGenerator'
}

# 测试类，如扩展其他站点，请在此配置
TESTER_MAP = {
    'weibo': 'WeiboValidTester',
    'videorank': 'VideoRankvalidtester'
}

TEST_URL_MAP = {
    'weibo': 'https://m.weibo.cn/',
    'videorank': 'https://videorank.cn'
}

# 产生器和验证器循环周期
CYCLE = 120

# API地址和端口
API_HOST = '0.0.0.0'
API_PORT = 5000

# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = True
# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = False
# API接口服务
API_PROCESS = True

#斐斐打码
FATEADM_API_MAP = {
    'pd_id' : '110001',  # 用户中心页可以查询到pd信息
    'pd_key' : 'kiICPvBd2heVYadv7Z0qL4GEzk9KziAp',
    'app_id' : '310001',  # 开发者分成用的账号，在开发者中心可以查询到
    'app_key' : 'FSbuBR2SGWgZ6rSCqwUfQweUNB4g1Wjl'
}
