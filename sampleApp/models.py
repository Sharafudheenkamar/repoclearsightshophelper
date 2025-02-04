from django.db import models



# Create your models here.
class LoginTable(models.Model):
    UserName = models.CharField(max_length=100, null=True, blank=True)
    PassWord = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)

class UserTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Phone =models.IntegerField(null=True, blank=True)

    

class ManufactureTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    CompanyName = models.CharField(max_length=100, null=True, blank=True)
    CompanyAddress = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    phone =  models.IntegerField(null=True, blank=True)




from django.db.models.signals import post_delete
from django.dispatch import receiver
import qrcode
from io import BytesIO
from django.core.files import File
class ProductTable(models.Model):
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    ProductId = models.CharField(max_length=100, null=True, blank=True)
    ProductType = models.CharField(max_length=100, null=True, blank=True)
    Manufacturedate = models.DateField(null=True, blank=True)
    Expirydate = models.CharField(max_length=100, null=True, blank=True)
    Uplaodphoto = models.FileField(max_length=250, null=True, blank=True, upload_to="Media")
    Productprice = models.IntegerField(null=True, blank=True)
    Offers = models.CharField(max_length=100, null=True, blank=True)
    QRCodeImage = models.ImageField(upload_to='product_qr_codes/', null=True, blank=True)  # To store the QR code image

    


    def __str__(self):
        return self.ProductName or "Unnamed Product"
    def save(self, *args, **kwargs):
        # Generate a QR code for the product if it's new
        if not self.QRCodeImage and self.ProductId:
            qr_code = qrcode.make(self.ProductId)  # Create QR code from ProductId
            qr_code_image = BytesIO()
            qr_code.save(qr_code_image, 'PNG')  # Save it in PNG format
            qr_code_image.seek(0)
            self.QRCodeImage = File(qr_code_image, name=f"product_{self.ProductId}_qr.png")  # Assign the QR code image to the field
        
        super(ProductTable, self).save(*args, **kwargs)  # Save the product

     
class FeedBack(models.Model):
    USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    FeedBack = models.CharField(max_length=250, null=True, blank=True)
    Rating = models.CharField(max_length=250, null=True, blank=True)