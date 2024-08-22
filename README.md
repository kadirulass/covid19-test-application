COVID-19 Vaka Sayısı Sorgulama
Bu proje, COVID-19 vaka sayıları hakkında bilgi sağlayan bir web uygulamasıdır. Kullanıcılar, seçtikleri ülke ve tarih için COVID-19 vaka sayısını görüntüleyebilirler. Proje, Flask ile geliştirilmiştir ve statik dosyalar Netlify ile dağıtılmaktadır.

Özellikler
Kullanıcıların seçtiği ülke ve tarih için COVID-19 vaka sayısını sorgulama
Güncel ziyaretçi sayısını gösterme
Kullanıcı dostu arayüz
Teknolojiler
Backend: Flask (Python)
Frontend: HTML, CSS
Veri Kaynağı: Pomber COVID-19 API
Deployment: Netlify
Kurulum
Geliştirme Ortamı
Python ve Flask Kurulumu: Python 3 ve Flask kütüphanesini yükleyin.

bash
Kodu kopyala
pip install flask pandas requests
Gerekli Paketler: Projeyi çalıştırmak için gerekli Python paketlerini yükleyin.

bash
Kodu kopyala
pip install -r requirements.txt
Proje Dosyaları: Proje dosyalarını indirin veya klonlayın.

bash
Kodu kopyala
git clone <repo-url>
Veritabanı Başlatma: Flask uygulamasını başlatmadan önce veritabanını oluşturun.

bash
Kodu kopyala
python app.py
Uygulama Çalıştırma
Uygulamayı Başlatma: Flask uygulamasını başlatın.

bash
Kodu kopyala
python app.py
Tarayıcıda Görüntüleme: Tarayıcınızda http://127.0.0.1:5000 adresine gidin.

Deployment
Web uygulamasını Netlify üzerinden dağıtmak için:

Netlify Hesabı: Netlify hesabınızı oluşturun veya giriş yapın.
Yeni Site Ekleme: Netlify panelinden yeni bir site oluşturun ve statik dosyalarınızı yükleyin.
Deploy Edin: Dosyalarınız yüklendiğinde Netlify, siteyi otomatik olarak dağıtacaktır.
Kullanım
Ana Sayfa: Ülke ve tarih seçerek COVID-19 vaka sayılarını sorgulayın.
Sonuç Sayfası: Seçilen ülke ve tarih için vaka sayısı, ölüm ve iyileşme sayılarını görüntüleyin.
Sorunlar ve Katkılar
Sorunlar veya katkılarınız varsa, GitHub Issues sayfasını ziyaret edebilirsiniz. Katkıda bulunmak isteyenler için pull request'ler açıktır.

Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını kontrol edin.
