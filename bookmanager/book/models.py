from django.db import models
'''
# Create your models here.
# 模型类需要继承自models.Model
# 系统会自动添加一个主键--id
# 字段
# 字段名=model.类型（选项）
# 字段名就是数据表的属性名
    char(M)
    varchar(M)
    M 就是选项
'''
class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10)

class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)