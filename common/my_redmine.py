from redminelib import Redmine
import warnings


def link_redmine(user, pwd, data):
    url = 'http://redmine.jiuqi.com.cn/'
    redmine = Redmine(url=url, username=user, password=pwd,
                      raise_attr_exception=False)

    issue = redmine.project.get(3)  # 获取项目
    test_iss = issue.issues.get(2443)  # 获取任务
    # print(issue,test_iss)   # 项目任务需要存在
    # 创建子任务
    test_iss.project.issues.manager.create(
        tracker_id=1,  # 类型：1错误，2功能，7提测，13任务
        subject=data['subject'],  # 主题
        description=data['description'],  # 描述
        status_id=1,  # 状态：1新建，2进行中，3已解决，4反馈，5已关闭，6已拒绝
        priority_id=2,  # 优先级：1低，2普通，3高，4紧急，5立刻
        assigned_to_id=185,  # 指派给：29唐芳萍，46范嫒嫒，49冯小伟，51曹立，55董建忠，185高祖新
        done_ratio=0,  # 完成度:0,10-100
        parent_issue_id='',  # 父任务
        fixed_version_id='V2.1',  # 版本号
        project_id='cyv2'  # 项目编号：采云：cyv2
    )


# if __name__ == '__main__':
#     warnings.simplefilter("ignore", ResourceWarning)
#     redmine_user = 'gaozuxin'
#     redmine_pwd = 'jiuqi@310235'
#     data = {
#         "subject": '自动创建问题',
#         "description": '问题描述'
#     }
#     link_redmine(redmine_user, redmine_pwd, data)
