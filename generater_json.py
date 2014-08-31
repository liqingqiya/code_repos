#!/usr/bin python
#-*- coding:utf-8 -*-

import ujson

str_in = [
{
    "pk":"1",
    "name":u"变形金刚1",
    "summary":u"一个猴子的故事",
    "financing_summary":u"融资概述,肯定赚钱",
    "risk_summary":u"风险概述,零风险",

    "goal":122334,
    "minimum":321,
    "intro":u"简介,一个猴子的故事",

    "plot":u"剧情摘要,一个猴子的故事",
    "info":u"项目信息",
    "news_url":"www.example.com",
    "members":u"卡司和团队",
    "filmmaking":u"制片信息",
    "scripts":u"剧本梗概",

    "invest_summary":u"投资概要",
    "proj_info":u"项目信息",
    "deficiencies":u"欠缺要素",
    "invest_detail":u"投资细节",
    "budget":u"预算&融资",
    "market":u"销售&发行",
    "financer":u"融资方介绍",
    "finance_management":u"投资管理",
    "status":"editing"
},
{
    "pk":"2",
    "name":u"变形金刚2",
    "summary":u"一个猴子的故事",
    "financing_summary":u"融资概述,肯定赚钱",
    "risk_summary":u"风险概述,零风险",

    "goal":122334,
    "minimum":321,
    "intro":u"简介,一个猴子的故事",

    "plot":u"剧情摘要,一个猴子的故事",
    "info":u"项目信息",
    "news_url":"www.example.com",
    "members":u"卡司和团队",
    "filmmaking":u"制片信息",
    "scripts":u"剧本梗概",

    "invest_summary":u"投资概要",
    "proj_info":u"项目信息",
    "deficiencies":u"欠缺要素",
    "invest_detail":u"投资细节",
    "budget":u"预算&融资",
    "market":u"销售&发行",
    "financer":u"融资方介绍",
    "finance_management":u"投资管理",
    "status":"published"
},
{
    "pk":"3",
    "name":u"变形金刚3",
    "summary":u"一个猴子的故事",
    "financing_summary":u"融资概述,肯定赚钱",
    "risk_summary":u"风险概述,零风险",

    "goal":122334,
    "minimum":321,
    "intro":u"简介,一个猴子的故事",

    "plot":u"剧情摘要,一个猴子的故事",
    "info":u"项目信息",
    "news_url":"www.example.com",
    "members":u"卡司和团队",
    "filmmaking":u"制片信息",
    "scripts":u"剧本梗概",

    "invest_summary":u"投资概要",
    "proj_info":u"项目信息",
    "deficiencies":u"欠缺要素",
    "invest_detail":u"投资细节",
    "budget":u"预算&融资",
    "market":u"销售&发行",
    "financer":u"融资方介绍",
    "finance_management":u"投资管理",
    "status":"closed"
}
]

raw_json = ujson.dumps(str_in)
with open("initial_data.json","w") as fi:
    fi.write(raw_json)
print "success"
