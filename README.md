# Bilgisayarlı Görme Kullanan Katılım Takip Sistemi
Bu proje, bilgisayarlı görme kullanarak katılım takibi yapmayı amaçlayan bir Python uygulamasıdır. Proje, yüz tanıma teknolojisi ve kullanıcı girişiyle çalışır. Projenin ana amacı, belirli bir sınıfta veya etkinlikte katılımcıların yoklamasını almak ve yoklama verilerini bir CSV dosyasına kaydetmektir.

## Özellikler
Kullanıcı girişi: Proje, kullanıcı adı ve şifre girişiyle başlar. Kullanıcı adı ve şifre doğruysa, yoklama alım ekranına erişim sağlanır.
Yüz tanıma: Kamera üzerinden alınan görüntülerde yüz tanıma teknolojisi kullanılarak katılımcıların yüzleri tanınır. Tanınan katılımcılar yoklama listesine eklenir.
Yoklama alma: Tanınan katılımcıların adları, giriş saati ve tarihi bir CSV dosyasına kaydedilir.
Arayüz: Tkinter kütüphanesi kullanılarak basit bir kullanıcı arayüzü oluşturulmuştur. Arayüz, kullanıcıyı yönlendirmek ve işlem sırasında bilgi sağlamak için tasarlanmıştır.

## Gereksinimler
Python 3.x
OpenCV
NumPy
Face Recognition
Tkinter
Pillow
Gerekli kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

Copy code
pip install opencv-python numpy face_recognition pillow

## Kullanım
Projeyi çalıştırmak için main.py dosyasını çalıştırın.
Kullanıcı adı ve şifre alanlarını doldurun ve "Giriş" butonuna tıklayın.
Yoklama alım ekranında, kameranın önüne geçin ve yüzünüzün tanınmasını bekleyin.
Yüz tanıma sonucunda adınız, ekranda görünecektir ve yoklama listesine kaydedilecektir.
Yoklama alımını bitirmek için ESC tuşuna basın.

## Notlar
Proje dosyalarını düzenlerken, kullanıcı adı ve şifre gibi hassas bilgilerinizi main.py dosyasında güvenli bir şekilde saklayın.
Proje dosyalarınızı düzenlerken, kameranın tanıma kalitesini artırmak için encodeListKnown değişkenindeki kişilerin fotoğraflarını güncelleyebilirsiniz.
