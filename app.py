from flask import Flask, request

app = Flask(__name__)


# Halaman utama (Tampilan Website)
@app.route("/", methods=["GET", "POST"])
def home():
  hasil_soal1 = ""
  hasil_soal2 = ""
  hasil_soal3 = ""

  # Jika tombol "Cek Jawaban" diklik (Metode POST)
  if request.method == "POST":
    # Mengambil input jawaban dari form web
    jawab1 = request.form.get("soal1")
    jawab2 = request.form.get("soal2")
    jawab3 = request.form.get("soal3")

    # LOGIKA IF-ELSE SOAL 1 (Pertambahan)
    if jawab1 == "12":
      hasil_soal1 = (
          "<span style='color:green;'><b>Benar!</b> (12)</span>"
      )
    else:
      hasil_soal1 = (
          f"<span style='color:red;'><b>Salah!</b> Anda menjawab"
          f" {jawab1}</span>"
      )

    # LOGIKA IF-ELSE SOAL 2 (Perkalian)
    if jawab2 == "40":
      hasil_soal2 = (
          "<span style='color:green;'><b>Benar!</b> (40)</span>"
      )
    else:
      hasil_soal2 = (
          f"<span style='color:red;'><b>Salah!</b> Anda menjawab"
          f" {jawab2}</span>"
      )

    # LOGIKA IF-ELSE SOAL 3 (Pembagian)
    if jawab3 == "5":
      hasil_soal3 = (
          "<span style='color:green;'><b>Benar!</b> (5)</span>"
      )
    else:
      hasil_soal3 = (
          f"<span style='color:red;'><b>Salah!</b> Anda menjawab"
          f" {jawab3}</span>"
      )

  # Struktur HTML dasar website agar bisa diakses di browser
  html_page = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Web Belajar Matematika</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }}
            .container {{ max-width: 500px; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
            h2 {{ color: #333; }}
            .soal {{ margin-bottom: 15px; padding: 10px; border-bottom: 1px solid #eee; }}
            input[type="number"] {{ padding: 5px; width: 80px; }}
            button {{ padding: 10px 15px; background: #0070f3; color: white; border: none; border-radius: 5px; cursor: pointer; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>📝 Kuis Matematika If-Else</h2>
            <form method="POST">
                
                <!-- SOAL 1 -->
                <div class="soal">
                    <p><b>Soal 1:</b> Berapakah 5 + 7?</p>
                    <input type="number" name="soal1" required> {hasil_soal1}
                </div>

                <!-- SOAL 2 -->
                <div class="soal">
                    <p><b>Soal 2:</b> Berapakah 8 x 5?</p>
                    <input type="number" name="soal2" required> {hasil_soal2}
                </div>

                <!-- SOAL 3 -->
                <div class="soal">
                    <p><b>Soal 3:</b> Berapakah 25 : 5?</p>
                    <input type="number" name="soal3" required> {hasil_soal3}
                </div>

                <br>
                <button type="submit">Cek Jawaban</button>
            </form>
        </div>
    </body>
    </html>
    """
  return html_page


# Hanya untuk keperluan lokal, vercel akan mengabaikan ini
if __name__ == "__main__":
  app.run(debug=True)