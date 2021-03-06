# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

#посмотреть на типы полей в models и расписать нашу примерную 
#схему по классам.
#права пользователей
rights_choices = (
    ('B', 'Начальник'),#умеет одобрять, пишет комментарий и графу, откуда оплата.
    ('U', 'Пользователь'),#видит все заказы, но не видит, кто заказал
    )

currency_choices = (
    ('RUR', 'Руб'),
    ('USD', '$'),
    ('EUR', '€'),
    )

#статусы заказов
# N O D C - в один ряд, всего 4 стадии жизни заказа
# B - отложено,  серенькая
# R - отклонено, красненькая

status_choices = (
    ('5', 'Отложено'),
    ('0', 'Новое'), #New
    #('D', 'Отложено'), #Delayed
    #('P', 'В рассмотрении'), #Pending лишнее
    #('A', 'Одобрено'), #Approved
    ('4', 'Отклонено'), #Rejected
    ('1', 'Заказано'),
    #('O', 'Ожидание счета'), #waiting for Order лишнее
    ('2', 'Поставлено'), #waiting for Delivery лишнее
    #('E', 'Выдано пользователю'), #partially Received лишнее
    # и добавить "отложен"
    ('3', 'Выполнено'), #Completed 
    )
#группы объектов
group_choices = (
    ("C", u"Культуральные"),
    ("P", u"Пластик"),
    ("G", u"Общелабораторные"),
    ("S", u"Соли"),
    ("I", u"ИФА АВ"),
    ("W", u"Гели Вестерн"),
    ("O", u"Канцелярия"),
    ("F", u"Ферменты, наборы и т.д."),
    ("U", u"Остальное"),
    )

class Stuff(models.Model):
    """
    Класс для списка оборудования,
    когда-либо заказывавшегося
    """
    name_rus = models.CharField("русское название", max_length=300)
    name_exact = models.CharField("точное название", max_length=200)
    manuf = models.CharField("производитель", max_length=100)
    man_site = models.URLField("сайт производителя", blank=True, null=True)
    cat_num = models.CharField("номер в каталоге", max_length=200, blank=True, null=True, unique=True)
    package = models.CharField("фасовка", max_length=100, blank=True, null=True)
    measure = models.CharField("ед. изм.", max_length=5, blank=True, null=True)
    stgroup = models.CharField("группа", max_length=1, choices=group_choices)
    
    class Meta:
        verbose_name = "оборудование"
        verbose_name_plural = "оборудование"
        ordering = ['name_rus', ]
        

    def __unicode__(self):
        #get_FOO_display() - для отображения значений полей с выбором
        return u"{0} ( {1}, {2} {3} )".format(self.name_rus, self.cat_num, self.package, self.measure)

    def __str__(self):
        return u"{0} ( {1}, {2} {3} )".format(self.name_rus, self.cat_num, self.package, self.measure)

    def __repr__(self):
        return u"{0} ( {1}, {2} {3} )".format(self.name_rus, self.cat_num, self.package, self.measure)


class Wish(models.Model):
    """
    Класс для пожеланий
    """

    stuff = models.ForeignKey(Stuff, verbose_name="оборудование")
    pieces = models.IntegerField("количество")
    price_man = models.DecimalField("цена производителя", max_digits=1000, decimal_places=2, blank=True, null=True)
    currency_man = models.CharField("валюта производителя", max_length=3, default='RUR', choices=currency_choices, blank=True, null=True )
    price_rus = models.DecimalField("фактическая цена", max_digits=1000, decimal_places=2, blank=True, null=True)
    currency_rus = models.CharField("валюта", max_length=3, default='RUR', choices=currency_choices, blank=True, null=True)
    order_date = models.DateTimeField("дата заказа", auto_now=True)
    user = models.ForeignKey(User, verbose_name="пользователь")
    urgent = models.BooleanField("срочно")
    status = models.CharField("статус пожелания", max_length=1, choices=status_choices, default='0')
    comment = models.TextField("комментарий", blank=True, null=True)


    def total(self):
        return self.price_man * self.pieces

    class Meta:
        verbose_name = 'пожелание'
        verbose_name_plural = 'пожелания'
        ordering = ['status', '-urgent']

    def __unicode__(self):
        return u"Пожелание №{0}, {1} [ {2} ]".format(self.id, self.stuff, self.get_status_display())

class Event(models.Model):
    """
    Класс для записи изменений статусов заказов
    """
    wish = models.ForeignKey(Wish, verbose_name="заказ")
    oldstatus = models.CharField("статус пожелания", max_length=1, choices=status_choices, default='0')
    newstatus = models.CharField("статус пожелания", max_length=1, choices=status_choices, default='0')
    user = models.ForeignKey(User, verbose_name="пользователь")
    order_date = models.DateTimeField("дата заказа", auto_now=True)
