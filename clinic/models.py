from django.db import models


class client(models.Model):
	Fam = models.CharField(max_length=30, verbose_name="Фамилия")
	Im = models.CharField(max_length=15, verbose_name="Имя")
	Otch = models.CharField(max_length=20, verbose_name="Отчество")
	Numm = models.CharField(max_length=15, verbose_name="Номер телефона")

	def __str__(self):
		return self.Fam


class user(models.Model):
	Fam = models.CharField(max_length=30, verbose_name="Фамилия")
	Im = models.CharField(max_length=15, verbose_name="Имя")
	Otch = models.CharField(max_length=20, verbose_name="Отчество")
	Numm = models.CharField(max_length=15, verbose_name="Номер телефона")
	Dolj = models.CharField(max_length=15, verbose_name="Должность")
	StajR = models.CharField(max_length=15, verbose_name="должность")

	def __str__(self):
		return self.Fam

