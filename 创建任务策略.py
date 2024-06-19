# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import json
import os
import sys

from typing import List

from alibabacloud_outboundbot20191226.client import Client as OutboundBot20191226Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_outboundbot20191226 import models as outbound_bot_20191226_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> OutboundBot20191226Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            # access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            access_key_id='',
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            # access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
            access_key_secret=''
        )
        # Endpoint 请参考 https://api.aliyun.com/product/OutboundBot
        config.endpoint = f'outboundbot.cn-shanghai.aliyuncs.com'
        return OutboundBot20191226Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_job_group_request = outbound_bot_20191226_models.CreateJobGroupRequest(
            instance_id='3f4c4489-ff70-46cf-acf0-ead5d2545dfe',
            job_group_name='sdk创建任务组策略',
            job_group_description='测试sdk创建任务组策略',
            scenario_id='',
            script_id='d9f1d96f-674e-45ab-aa07-a253f9db19a3',
            strategy_json='''{
                                "maxAttemptsPerDay": 1,
                                "minAttemptInterval": 1,
                                "RepeatBy": "once",
                                "RepeatDays": "",
                                "workingTime": "",
                                "name": "策略名字",
                                "startTime": "",
                                "endTime": ""
                            }''',
            recall_strategy_json='''{
                                        "emptyNumberIgnore": true,
                                        "inArrearsIgnore": true,
                                        "outOfServiceIgnore": true
                                }''',
            calling_number=[
                '20240524'
            ],
            ringing_duration=15,
            priority='Daily',
            min_concurrency=3,
            # flash_sms_extras=''
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            res = client.create_job_group_with_options(create_job_group_request, runtime)
            res = eval(str(res))
            JobGroupId = res['body']['JobGroup']['JobGroupId']
            # print(JobGroupId)
            return JobGroupId

        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_job_group_request = outbound_bot_20191226_models.CreateJobGroupRequest(
            instance_id='3f4c4489-ff70-46cf-acf0-ead5d2545dfe',
            job_group_name='sdk创建任务组策略',
            job_group_description='测试sdk创建任务组策略',
            scenario_id='',
            script_id='d9f1d96f-674e-45ab-aa07-a253f9db19a3',
            strategy_json='''{
                                "maxAttemptsPerDay": 1,
                                "minAttemptInterval": 1,
                                "RepeatBy": "once",
                                "RepeatDays": "",
                                "workingTime": "",
                                "name": "策略名字",
                                "startTime": "",
                                "endTime": ""
                            }''',
            recall_strategy_json='''{
                                        "emptyNumberIgnore": true,
                                        "inArrearsIgnore": true,
                                        "outOfServiceIgnore": true
                                }''',
            calling_number=[
                '20240524'
            ],
            ringing_duration=15,
            priority='Daily',
            min_concurrency=3,
            # flash_sms_extras=''
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.create_job_group_with_options_async(create_job_group_request, runtime)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    # Sample.main(sys.argv[1:])
    group_id = Sample.main(sys.argv[1:])
    print(group_id)