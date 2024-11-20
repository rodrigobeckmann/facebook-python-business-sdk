# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.api import FacebookAdsApi

access_token = '<ACCESS_TOKEN>'
app_secret = '<APP_SECRET>'
app_id = '<APP_ID>'
id = '<AD_ACCOUNT_ID>'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My Test Website Custom Audience',
  'rule': {'inclusions':{'operator':'or','rules':[{'event_sources':[{'id':'<pixelID>','type':'pixel'}],'retention_seconds':8400,'filter':{'operator':'and','filters':[{'field':'url','operator':'i_contains','value':'shoes'}]}}]}},
  'prefill': '1',
}
print AdAccount(id).create_custom_audience(
  fields=fields,
  params=params,
)