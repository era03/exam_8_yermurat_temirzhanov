from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import TextChoices



class CategoryChoices(TextChoices):
    SMARTPHONE = 'smartphone', 'Смартфоны'
    TV = 'tv', 'Телевизоры'
    OTHER = 'other', 'Разное'
    LAPTOP = 'laptop', 'Ноутбуки'


class Product(models.Model):
    name = models.CharField(
        verbose_name='Наименование товара', 
        max_length=200, 
        null=False, 
        blank=False
    )
    category = models.CharField(
        max_length=30, 
        null=False, 
        blank=False, 
        choices=CategoryChoices.choices, 
        default=CategoryChoices.OTHER, 
        verbose_name='Категория продукта'
    )
    description = models.TextField(
        verbose_name='Текст', 
        max_length=3000, 
        null=False, 
        blank=False
    )
    image = models.ImageField(
        null=True, 
        blank=True, 
        upload_to='product_pics', 
        verbose_name='Картинка товара'
    )


class Review(models.Model):
    author = models.ForeignKey(
        get_user_model(), 
        related_name='authors', 
        on_delete=models.CASCADE, 
        verbose_name='Пользователь'
    )
    product = models.ForeignKey(
        to='Product',
        verbose_name='Продукт',
        related_name='product',
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name='Отзыв', 
        max_length=3000
    )
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(5)
        ], 
        default=0, 
        verbose_name='Рейтинг товара'
    )
