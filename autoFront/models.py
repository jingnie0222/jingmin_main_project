from django.db import models


# Create your models here.
class Auto(models.Model):
    """
    :param baseNode: base代码Node的git分支
    :param baseNginx: base代码Nginx的svn分支
    :param testNode: test代码Node的git分支
    :param testNginx: test代码Nginx的svn分支

    :param dataIp: 新数据的机器ip地址
    :param dataUser: 新数据的机器用户
    :param dataPass: 新数据的机器密码
    :param dataPath: 新数据的路径
    :param confIp: 新配置文件的机器ip地址
    :param confUser: 新配置文件的机器用户
    :param confPass: 新配置文件的机器密码
    :param confPath: 新配置文件的路径

    :param type: 代表是给pc还是wap安装环境

    :param isPic: PIC系统图像对比，1代表是，0代表否
    :param isPagetest: Pagetest回归测试，1代表是，0代表否
    :param isInterface: 特殊结果接口比对，1代表是，0代表否
    :param isPress: 自动压力测试，1代表是，0代表否
    :param isUts: UTS交互验证测试，1代表是，0代表否

    :param create_time: 任务创建时间
    :param start_time: 任务开始时间
    :param end_time: 任务结束时间
    :param user: 用户
    :param status: 任务运行状态
    :param runningIp: 环境搭建所在机器ip
    :param tag: 备注信息
    :param log: 日志

    :param basePicResult: PIC系统图像对比-base结果
    :param testPicResult: PIC系统图像对比-test结果
    :param basePagetestResult: Pagetest回归测试-base结果
    :param testPagetestResult: Pagetest回归测试-test结果
    :param baseInterfaceResult: 特殊结果接口比对-base结果
    :param testInterfaceResult: 特殊结果接口比对-test结果
    :param basePressResult: 自动压力测试-base结果
    :param testPressResult: 自动压力测试-test结果
    :param baseUtsResult: UTS交互验证测试-base结果
    :param testUtsResult: UTS交互验证测试-test结果
    :return: None
    """

    baseNode = models.CharField(max_length=100, default='')
    baseNginx = models.TextField(default='')
    testNode = models.CharField(max_length=100, default='')
    testNginx = models.TextField(default='')

    dataIp = models.CharField(max_length=20, default='')
    dataUser = models.CharField(max_length=20, default='')
    dataPass = models.CharField(max_length=20, default='')
    dataPath = models.CharField(max_length=100, default='')
    confIp = models.CharField(max_length=20, default='')
    confUser = models.CharField(max_length=20, default='')
    confPass = models.CharField(max_length=20, default='')
    confPath = models.CharField(max_length=100, default='')

    type = models.CharField(max_length=20, default='')

    isPic = models.IntegerField(default=0)
    isPagetest = models.IntegerField(default=0)
    isInterface = models.IntegerField(default=0)
    isPress = models.IntegerField(default=0)
    isUts = models.IntegerField(default=0)

    create_time = models.CharField(max_length=50, default='')
    start_time = models.CharField(max_length=50, default='')
    end_time = models.CharField(max_length=50, default='')
    user = models.CharField(max_length=20, default='')
    status = models.IntegerField(default=0)
    runningIp = models.CharField(max_length=50, default='')
    tag = models.CharField(max_length=20, default='')
    log = models.TextField(default='')

    baseHostName = models.TextField(default='')
    testHostName = models.TextField(default='')
    basePicResult = models.TextField(default='')
    testPicResult = models.TextField(default='')
    basePagetestResult = models.TextField(default='')
    testPagetestResult = models.TextField(default='')
    baseInterfaceResult = models.TextField(default='')
    testInterfaceResult = models.TextField(default='')
    basePressResult = models.TextField(default='')
    testPressResult = models.TextField(default='')
    baseUtsResult = models.TextField(default='')
    testUtsResult = models.TextField(default='')


class front_diff_mission_result(models.Model):
    query = models.TextField(default='')
    # mission = models.ForeignKey(to=Auto, blank=True, null=True, on_delete=models.SET_NULL)
    mission_id = models.IntegerField(default=0)
    url1 = models.TextField(default='')
    url2 = models.TextField(default='')
    is_diff = models.IntegerField(default=0)
    html1 = models.TextField(default='')
    html2 = models.TextField(default='')
    status = models.IntegerField(default=0)
    comment = models.TextField(default='')
    css_selector = models.TextField(default='')

class Selftest(models.Model):
    """
    :param baseNode: base代码Node的git分支
    :param baseNginx: base代码Nginx的svn地址
    :param testNode: test代码Node的git分支
    :param testNginx: test代码Nginx的svn地址

    :param testIp: 新数据的机器ip地址
    :param testUser: 新数据的机器用户
    :param testPass: 新数据的机器密码

    :param baseIp: 新配置文件的机器ip地址
    :param baseUser: 新配置文件的机器用户
    :param basePass: 新配置文件的机器密码

    :param type: 代表是给pc还是wap安装环境

    :param isPic: PIC系统图像对比，1代表是，0代表否
    :param isPagetest: Pagetest回归测试，1代表是，0代表否
    :param isInterface: 特殊结果接口比对，1代表是，0代表否
    :param isPress: 自动压力测试，1代表是，0代表否
    :param isUts: UTS交互验证测试，1代表是，0代表否

    :param create_time: 任务创建时间
    :param start_time: 任务开始时间
    :param end_time: 任务结束时间
    :param user: 用户
    :param status: 任务运行状态
    :param runningIp: 环境搭建所在机器ip
    :param tag: 备注信息
    :param log: 日志

    :param basePicResult: PIC系统图像对比-base结果
    :param testPicResult: PIC系统图像对比-test结果
    :param basePagetestResult: Pagetest回归测试-base结果
    :param testPagetestResult: Pagetest回归测试-test结果
    :param baseInterfaceResult: 特殊结果接口比对-base结果
    :param testInterfaceResult: 特殊结果接口比对-test结果
    :param basePressResult: 自动压力测试-base结果
    :param testPressResult: 自动压力测试-test结果
    :param baseUtsResult: UTS交互验证测试-base结果
    :param testUtsResult: UTS交互验证测试-test结果
    :return: None
    """

    baseNode = models.CharField(max_length=100, default='')
    baseNginx = models.TextField(default='')
    testNode = models.CharField(max_length=100, default='')
    testNginx = models.TextField(default='')

    baseIp = models.CharField(max_length=20, default='')
    baseUser = models.CharField(max_length=20, default='')
    basePass = models.CharField(max_length=20, default='')
    testIp = models.CharField(max_length=20, default='')
    testUser = models.CharField(max_length=20, default='')
    testPass = models.CharField(max_length=20, default='')
    #1跳过，0执行
    isSkipdeploy = models.IntegerField(default=0)#是否跳过环境部署
    type = models.CharField(max_length=20, default='')

    isPic = models.IntegerField(default=0)
    isPagetest = models.IntegerField(default=0)
    isInterface = models.IntegerField(default=0)
    isPress = models.IntegerField(default=0)
    isUts = models.IntegerField(default=0)

    isJuhe=models.IntegerField(default=0)
    isStruct=models.IntegerField(default=0)
    isRealmonitor=models.IntegerField(default=0)
    isPingback=models.IntegerField(default=0)
    isSecurity=models.IntegerField(default=0)
    isDeadlink=models.IntegerField(default=0)

    create_time = models.CharField(max_length=50, default='')
    start_time = models.CharField(max_length=50, default='')
    end_time = models.CharField(max_length=50, default='')
    user = models.CharField(max_length=20, default='')
    status = models.IntegerField(default=0)
    runningIp = models.CharField(max_length=50, default='')
    tag = models.CharField(max_length=20, default='')
    log = models.TextField(default='')

    #0:待完成。1成功 -1失败
    baseStatus=models.IntegerField(default=0)#base环境 jeckins deploy情况
    testStatus=models.IntegerField(default=0)#test环境 jeckins deploy情况

    baseHostName = models.TextField(default='')
    testHostName = models.TextField(default='')
    basePicResult = models.TextField(default='')
    testPicResult = models.TextField(default='')
    basePagetestResult = models.TextField(default='')
    testPagetestResult = models.TextField(default='')
    baseInterfaceResult = models.TextField(default='')
    testInterfaceResult = models.TextField(default='')
    basePressResult = models.TextField(default='')
    testPressResult = models.TextField(default='')
    baseUtsResult = models.TextField(default='')
    testUtsResult = models.TextField(default='')

    baseJuheResult = models.TextField(default='')
    testJuheResult = models.TextField(default='')
    baseStructResult = models.TextField(default='')
    testStructResult = models.TextField(default='')
    baseRealmonitorResult = models.TextField(default='')
    testRealmonitorResult = models.TextField(default='')
    basePingbackResult = models.TextField(default='')
    testPingbackResult = models.TextField(default='')
    baseSecurityResult = models.TextField(default='')
    testSecurityResult = models.TextField(default='')
    baseDeadlinkResult = models.TextField(default='')
    testDeadlinkResult = models.TextField(default='')
    #test环境std统计和err统计结果查看路径
    testStdResult = models.TextField(default='')
    testErrResult = models.TextField(default='')