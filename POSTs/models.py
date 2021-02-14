from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    price = models.IntegerField()
    describtion = models.CharField(max_length=300)
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')
    img3 = models.ImageField(upload_to='images')
    img4 = models.ImageField(upload_to='images')
    img5 = models.ImageField(upload_to='images')
    img6 = models.ImageField(upload_to='images')
    old_choice = (
        ('1 month to 6 month','1 month to 6 month'),
        ('6 month to 12 month','6 month to 12 month'),
        ('1 years to 2 years','1 years to 2 years'),
        ('3 years to 5 years','3 years to 5 years'),
        ('more than 5','more than 5'),
    )
    old = models.CharField(max_length=25 ,choices=old_choice )
    region_choice = (
        ("Abardeen Bazar","Abardeen Bazar"),
        ("Beadnabad","Beadnabad"),
        ("Bejoy Nagar","Bejoy Nagar"),
        ("Bhatubasti","Bhatubasti"),
        ("Bimilitan","Bimilitan"),
        ("Brichgunj","Brichgunj"),
        ("Calicut","Calicut"),
        ("Chakkargaon","Chakkargaon"),
        ("Dairy farm","Dairy farm"),
        ("Delanipur","Delanipur"),
        ("Dignabad","Dignabad"),
        ("Dollygunj ","Dollygunj "),
        ("Garacharma","Garacharma"),
        ("Govinda Nagar","Govinda Nagar"),
        ("Havelock (Swaraj Dweep)","Havelock (Swaraj Dweep)"),
        ("Haddo","Haddo"),
        ("Junglighat","Junglighat"),
        ("Lakshmanpur ","Lakshmanpur "),
        ("Middle point","Middle point"),
        ("Minnie Bay part","Minnie Bay part"),
        ("Nayagaon","Nayagaon"),
        ("Neil ( Shaheed Dweep)","Neil ( Shaheed Dweep)"),
        ("Pahargaon part","Pahargaon part"),
        ("Phoenix bay","Phoenix bay"),
        ("Port Blair","Port Blair"),
        ("Prothrapur","Prothrapur"),
        ("Radha Nagar","Radha Nagar"),
        ("Ram Nagar","Ram Nagar"),
        ("Rangachang","Rangachang"),
        ("School Line","School Line"),
        ("Shadipur","Shadipur"),
        ("Shyam Nagar","Shyam Nagar"),
        ("Sippighat","Sippighat"),
        (" Sitapur"," Sitapur"),
        ("south point","south point"),
        ("Teylorabad","Teylorabad"),
        ("Bambooflat","Bambooflat"),
        ("Bindraban","Bindraban"),
        ("Chouldari","Chouldari"),
        ("Ferrargunj","Ferrargunj"),
        ("Guptapara","Guptapara"),
        ("Hope Town","Hope Town"),
        ("Knapuram","Knapuram"),
        ("Manglutan","Manglutan"),
        ("Mannarghat","Mannarghat"),
        ("Mithakhari","Mithakhari"),
        ("Namunaghar","Namunaghar"),
        ("North Bay","North Bay"),
        ("Ograbraij","Ograbraij"),
        ("Shoal Bay","Shoal Bay"),
        ("Shore Point","Shore Point"),
        ("Stewartgunj","Stewartgunj"),
        ("Tusnabad","Tusnabad"),
        ("Wandur","Wandur"),
        ("Wimberlygunj","Wimberlygunj"),
        ("Harmender Bay","Harmender Bay"),
        ("Hut Bay","Hut Bay"),
        ("Netaji Nagar","Netaji Nagar"),
        ("Rabindra Nagar","Rabindra Nagar"),
        ("Ramakrishnapur","Ramakrishnapur"),
        ("Vivekanandapuram","Vivekanandapuram"),
        ("Diglipur","Diglipur"),
        ("Kalighat","Kalighat"),
        ("Kishori Nagar","Kishori Nagar"),
        ("Laxmipur","Laxmipur"),
        ("Madhupur","Madhupur"),
        ("Nabagram","Nabagram"),
        ("Ramakrishnagram","Ramakrishnagram"),
        ("Sitanagar","Sitanagar"),
        ("Subhashgram","Subhashgram"),
        ("Bakultala","Bakultala"),
        ("Kadamtala","Kadamtala"),
        ("Kaushalyanagar","Kaushalyanagar"),
        ("Long Island","Long Island"),
        ("Nilambur","Nilambur"),
        ("Nimbutala","Nimbutala"),
        ("Panchawati","Panchawati"),
        ("Rampur","Rampur"),
        ("Rangat","Rangat"),
        ("Sabari","Sabari"),
        ("Santanu","Santanu"),
        ("Uttara","Uttara"),
        ("Harinagar","Harinagar"),
        ("Karmatang","Karmatang"),
        ("Lucknow","Lucknow"),
        ("Mayabunder","Mayabunder"),
        ("Pahalgaon","Pahalgaon"),
        ("Pokadera","Pokadera"),
        ("Tugapur","Tugapur"),
        ("Malacca","Malacca"),
        ("Mus","Mus"),
        ("Perka","Perka"),
        ("Sawai","Sawai"),
        ("Tamaloo","Tamaloo"),
    )
    region = models.CharField(max_length=30 , choices=region_choice)