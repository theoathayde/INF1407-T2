from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, help_text="Entre com o username", primary_key=True)
    email = models.EmailField(help_text="Informe o Email", max_length=254)


class Post(models.Model):
    post_id = models.AutoField
    post_topic= models.CharField(help_text="Topico do post", max_length=300)
    post_content = models.CharField(help_text="Conteudo do post", max_length=5000)