from django.db import models


class client(models.Model):
	Fam = models.CharField(max_length=30, verbose_name="Фамилия")
	Im = models.CharField(max_length=15, verbose_name="Имя")
	Otch = models.CharField(max_length=20, verbose_name="Отчество")
	Numm = models.CharField(max_length=15, verbose_name="Номер телефона")

	def __str__(self):
		return self.Fam



class user(models.Model):
	Ty =(('V', 'Врач'),('S', 'Секретарь'))
	Fam = models.CharField(max_length=30, verbose_name="Фамилия")
	Im = models.CharField(max_length=15, verbose_name="Имя")
	Otch = models.CharField(max_length=20, verbose_name="Отчество")
	Numm = models.CharField(max_length=15, verbose_name="Номер телефона")
	Dolj = models.CharField(max_length=15, verbose_name="Должность")
	StajR = models.CharField(max_length=15, verbose_name="Стаж")
	Img = models.ImageField(blank=True, verbose_name="Ссылка картинки")
	Passw = models.CharField(max_length=50, verbose_name="Пароль" )
	Type = models.CharField(max_length=1, choices=Ty)

	def __str__(self):
		return self.Fam

class content(models.Model):
	Title = models.CharField(max_length=15, verbose_name="Заголовок")
	Description = models.CharField(max_length=120, verbose_name="Описание")
	# Image = models.ImageField(upload_to='products', blank=True, verbose_name="Изображение") если надо

	def __str__(self):
		return self.Title

class servers(models.Model):
	Title = models.CharField(max_length=50, verbose_name="Заголовок")
	Description = models.CharField(max_length=120, verbose_name="Описание")
	Price = models.CharField(max_length=7, verbose_name="Цена")

	def __str__(self):
		return self.Title

class doctor(models.Model):
	 Dolzhnost = models.CharField(max_length=15, verbose_name="Должность")
	 Stazh = models.CharField(max_length=120, verbose_name="Стаж")
	 tel = models.CharField(max_length=15, verbose_name="Телефон")
	 Fam = models.CharField(max_length=30, verbose_name="Фамилия")
	 Im = models.CharField(max_length=15, verbose_name="Имя")
	 Otch = models.CharField(max_length=20, verbose_name="Отчество")

	 def __str__(self):
 		return self.Dolzhnost

class Visit(models.Model):
	user = models.ForeignKey("user", on_delete=models.CASCADE,)
	#client = models.ForeignKey("client", on_delete=models.CASCADE,)
	#servies = models.ForeignKey("servers", on_delete=models.CASCADE,) 
	date = models.DateTimeField()
	Numm = models.CharField(max_length=15, verbose_name="Номер телефона")

	def __str__(self):
		return self.user

class Log(models.Model):
	username = models.CharField(max_length=40)
	quary = models.CharField(max_length=20)
	date_time = models.DateTimeField()

	def __str__(self):
		return self.user
