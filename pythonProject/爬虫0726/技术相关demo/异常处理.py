import requests


proxy = None  # 初始化代理服务器列表
proxies = [proxy1, proxy2, proxy3]  # 代理服务器列表
retries = 3  # 重试次数
backoff_factor = 0.3  # 重试等待时间因子
status_forcelist = [429, 500, 502, 503, 504]  # 需要强制重试的HTTP状态码列表
retry_strategy = Retry(total=retries, read=retries, connect=retries, backoff_factor=backoff_factor,
                       status_forcelist=status_forcelist)  # 重试策略
adapter = HTTPAdapter(max_retries=retry_strategy)  # 创建适配器
session = requests.Session()  # 创建Session对象
session.mount('http://', adapter)  # 将适配器挂载到Session对象上
session.mount('https://', adapter)  # 将适配器挂载到Session对象上
while True:  # 无限循环，直到获取到数据或退出条件满足为止
    try:
        response = session.get(url, proxies=proxies)  # 发送GET请求
        if response.status_code == 200:  # 如果请求成功（HTTP状态码为200），则退出循环
            break
    except HTTPError as e:  # 如果发生HTTPError异常（HTTP错误状态码），则进行重试或跳过当前请求（根据具体情况而定）
        if e.pageResp.status_code in status_forcelist:  # 如果HTTP状态码在需要强制重试的列表中，则进行重试（根据重试策略）
            pass  # 进行重试或跳过当前请求（根据具体情况而定