'''
1. 获取公众号id
2. 每个公众号轮询内容
3. 查询后将每个公众号都存入数据库
4. 将该任务分发给公众号爬虫，进行文本录入

'''
from datetime import timedelta
from prefect import task, flow
from agents.weread import weread
from sqlmodel import Session,engine

@task(name="获取公众号id清单")
def get_gzh_list_id():
    list = ["MP_WXS_2390204840"]
    print(list)
    return list

@task(name="获取公众号文章清单")
def get_gzh_paper(wr: weread, gzhid: str):
    list = wr.get_articles(gzhid)
    print(list)
    return list

def store_articles(json):
    id = json['re']
    with Session(engine) as session:
        db_hero = session.get(, hero_id)
        if not db_hero:
                for key, value in hero_data.items():
                    setattr(db_hero, key, value)
        session.add(db_hero)
        session.commit()
        return db_hero

    

@task(name="初始化一个微信读书", cache_expiration=timedelta(seconds=60))
def create_weread():
    wr = weread()
    return wr


@flow(name="每天更新最新的公众号内容")
def spider_gzh_all():
    list = get_gzh_list_id()
    wr = create_weread()
    for id in list:
        get_gzh_paper(wr, id)


if __name__ == "__main__":
    spider_gzh_all()
