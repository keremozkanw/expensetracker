# Expense Tracker

## 📌 Project Description (English)
Expense Tracker is a CLI (Command Line Interface) application that helps users track their personal expenses. It is built using Python and PostgreSQL. Users can record their expenses, list them, and view their total spending.

### 🚀 Features
- Add expenses
- List expenses
- View total spending
- Filter monthly expenses

### 🛠 Requirements
- Python 3.x
- PostgreSQL
- Required dependencies installed via pip

### 📥 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```

2. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up PostgreSQL Database**
   Create the database in PostgreSQL:
   ```sql
   CREATE DATABASE expense_tracker;
   ```
   Create a `.env` file and add the following:
   ```env
   DATABASE_URL=postgresql://username:password@localhost/expense_tracker
   ```

4. **Create Database Tables**
   ```bash
   python -m app.database
   ```

5. **Run the Application**
   ```bash
   python app/cli.py
   ```

### 📌 Usage
1. **Add an expense:** Select "1. Add Expense" when the program starts.
2. **List expenses:** Select "2. List Expenses" to view recorded expenses.
3. **Show total spending:** Use the "3. Show Total Spending" option.

## 📌 Proje Açıklaması (Türkçe)
Expense Tracker, kişisel giderlerinizi takip etmenizi sağlayan bir CLI (Komut Satırı Arayüzü) uygulamasıdır. Python ve PostgreSQL kullanılarak geliştirilmiştir. Kullanıcılar giderlerini kaydedebilir, listeleyebilir ve toplam harcamalarını görüntüleyebilir.

### 🚀 Özellikler
- Gider ekleme
- Giderleri listeleme
- Toplam harcamayı görüntüleme
- Aylık harcamaları filtreleme

### 🛠 Gereksinimler
- Python 3.x
- PostgreSQL
- pip ile yüklenmiş bağımlılıklar

### 📥 Kurulum

1. **Depoyu Kopyala**
   ```bash
   git clone https://github.com/kullaniciadi/expense-tracker.git
   cd expense-tracker
   ```

2. **Gerekli Paketleri Yükle**
   ```bash
   pip install -r requirements.txt
   ```

3. **PostgreSQL Veritabanını Ayarla**
   PostgreSQL’de aşağıdaki komutu çalıştırarak veritabanını oluşturun:
   ```sql
   CREATE DATABASE expense_tracker;
   ```
   `.env` dosyasını oluşturup şu bilgileri ekleyin:
   ```env
   DATABASE_URL=postgresql://username:password@localhost/expense_tracker
   ```

4. **Veritabanı Tablolarını Oluştur**
   ```bash
   python -m app.database
   ```

5. **Uygulamayı Çalıştır**
   ```bash
   python app/cli.py
   ```

### 📌 Kullanım
1. **Gider ekleme:** Program çalıştırıldığında "1. Gider Ekle" seçeneğini seçin.
2. **Giderleri listeleme:** "2. Giderleri Listele" seçeneğini seçerek kaydedilen giderleri görebilirsiniz.
3. **Toplam harcamayı gösterme:** "3. Toplam Harcamayı Göster" seçeneğini kullanın.

---

📌 **Geri bildirimleriniz veya geliştirme önerileriniz varsa, katkıda bulunabilirsiniz!** 🚀

