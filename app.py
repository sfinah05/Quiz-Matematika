from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
  # Menyimpan status tombol "Selanjutnya" apakah sudah diklik atau belum
  show_soal = request.form.get("show_soal", "false")

  hasil_soal1 = ""
  hasil_soal2 = ""
  hasil_soal3 = ""

  # Jika tombol "Cek Jawaban" diklik (Metode POST)
  if request.method == "POST" and "cek_jawaban" in request.form:
    show_soal = "true"  # Tetap tampilkan soal saat cek jawaban diklik
    jawab1 = request.form.get("soal1")
    jawab2 = request.form.get("soal2")
    jawab3 = request.form.get("soal3")

    # LOGIKA IF-ELSE SOAL 1
    if jawab1 == "12":
      hasil_soal1 = (
          "<span style='color:green;'><b>Benar!</b> (12)</span>"
      )
    else:
      hasil_soal1 = (
          f"<span style='color:red;'><b>Salah!</b> Jawaban Anda: {jawab1}</span>"
      )

    # LOGIKA IF-ELSE SOAL 2
    if jawab2 == "40":
      hasil_soal2 = (
          "<span style='color:green;'><b>Benar!</b> (40)</span>"
      )
    else:
      hasil_soal2 = (
          f"<span style='color:red;'><b>Salah!</b> Jawaban Anda: {jawab2}</span>"
      )

    # LOGIKA IF-ELSE SOAL 3
    if jawab3 == "5":
      hasil_soal3 = (
          "<span style='color:green;'><b>Benar!</b> (5)</span>"
      )
    else:
      hasil_soal3 = (
          f"<span style='color:red;'><b>Salah!</b> Jawaban Anda: {jawab3}</span>"
      )

  # Jika tombol "Selanjutnya" diklik, ubah status menjadi true
  if request.method == "POST" and "tombol_selanjutnya" in request.form:
    show_soal = "true"

  # Struktur HTML dan CSS Website
  html_page = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Web Belajar Matematika</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; display: flex; justify-content: center; }}
            .container {{ width: 100%; max-width: 500px; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 0 15px rgba(0,0,0,0.1); }}
            h2, h3 {{ color: #333; margin-top: 0; }}
            .biodata {{ background: #eef2f7; padding: 15px; border-radius: 6px; margin-bottom: 20px; border-left: 5px solid #0070f3; }}
            .biodata p {{ margin: 5px 0; font-size: 15px; }}
            .status {{ color: green; font-weight: bold; }}
            .button-group {{ display: flex; gap: 10px; margin-bottom: 20px; }}
            .btn {{ padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer; text-decoration: none; font-weight: bold; text-align: center; font-size: 14px; }}
            .btn-telu {{ background: #b30000; color: white; flex: 1; }}
            .btn-next {{ background: #0070f3; color: white; flex: 1; }}
            .soal-box {{ border-top: 2px dashed #ccc; padding-top: 20px; margin-top: 20px; }}
            .soal {{ margin-bottom: 15px; padding: 10px; border-bottom: 1px solid #eee; }}
            input[type="number"] {{ padding: 6px; width: 80px; margin-top: 5px; }}
            .btn-submit {{ background: #28a745; color: white; width: 100%; padding: 12px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>👋 Selamat Datang!</h2>
            
            <!-- Bagian Biodata -->
            <div class="biodata">
                <p><b>Nama:</b> Nama Anda Disini</p>
                <p><b>Universitas:</b> Telkom University</p>
                <p><b>Status:</b> <span class="status">● Aktif</span></p>
            </div>

            <!-- Bagian 2 Button Utama -->
            <form method="POST">
                <!-- Simpan status state biar kuis ga ilang saat di-refresh/submit -->
                <input type="hidden" name="show_soal" value="{show_soal}">
                
                <div class="button-group">
                    <!-- Button 1: Link keluar ke Website Tel-U -->
                    <a href="https://telkomuniversity.ac.id" target="_blank" class="btn btn-telu">🌐 Web Tel U</a>
                    
                    <!-- Button 2: Mengaktifkan area soal matematika -->
                    <button type="submit" name="tombol_selanjutnya" class="btn btn-next">➡️ Selanjutnya</button>
                </div>
    """

  # Jika tombol selanjutnya sudah diklik, potong HTML untuk memunculkan soal
  if show_soal == "true":
    html_page += f"""
                <div class="soal-box">
                    <h3>📝 Kuis Matematika If-Else</h3>
                    
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
                    <button type="submit" name="cek_jawaban" class="btn btn-submit">Cek Jawaban</button>
                </div>
    """

  # Penutup tag HTML
  html_page += """
            </form>
        </div>
    </body>
    </html>
  """

  return html_page


if __name__ == "__main__":
  app.run(debug=True)