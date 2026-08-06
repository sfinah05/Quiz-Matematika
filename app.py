from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
  # 1. Mengambil data identitas dari form ketikan Anda
  nama_user = request.form.get("nama_user", "Nama Anda Disini")
  univ_user = request.form.get("univ_user", "Telkom University")
  status_user = request.form.get("status_user", "Aktif")

  # Jika tidak sengaja terhapus atau kosong, kembalikan ke default
  if not nama_user:
    nama_user = "Nama Anda Disini"

  # 2. Mengambil status halaman kuis
  show_soal = request.form.get("show_soal", "false")

  # 3. Mengambil nilai jawaban angka agar tidak hilang
  jawab1 = request.form.get("soal1", "")
  jawab2 = request.form.get("soal2", "")
  jawab3 = request.form.get("soal3", "")

  hasil_soal1 = ""
  hasil_soal2 = ""
  hasil_soal3 = ""
  notifikasi_sukses = ""

  # JIKA TOMBOL CEK JAWABAN DIKLIK
  if request.method == "POST" and "cek_jawaban" in request.form:
    show_soal = "true"

    benar_soal1 = False
    benar_soal2 = False
    benar_soal3 = False

    if jawab1 == "12":
      hasil_soal1 = (
          "<span style='color:green;'><b>Benar!</b> (12)</span>"
      )
      benar_soal1 = True
    elif jawab1 != "":
      hasil_soal1 = (
          f"<span style='color:red;'><b>Salah!</b> Jawaban Anda: {jawab1}</span>"
      )

    if jawab2 == "40":
      hasil_soal2 = (
          "<span style='color:green;'><b>Benar!</b> (40)</span>"
      )
      benar_soal2 = True
    elif jawab2 != "":
      hasil_soal2 = (
          f"<span style='color:red;'><b>Salah!</b> Jawaban Anda: {jawab2}</span>"
      )

    if jawab3 == "5":
      hasil_soal3 = (
          "<span style='color:green;'><b>Benar!</b> (5)</span>"
      )
      benar_soal3 = True
    elif jawab3 != "":
      hasil_soal3 = (
          f"<span style='color:red;'><b>Salah!</b> Jawaban Anda: {jawab3}</span>"
      )

    if benar_soal1 and benar_soal2 and benar_soal3:
      notifikasi_sukses = f"""
            <div style="background-color: #d4edda; color: #155724; padding: 15px; border-radius: 5px; margin-bottom: 20px; border: 1px solid #c3e6cb; text-align: center;">
                <h3 style="margin: 0 0 5px 0;">🎉 Selamat, {nama_user}! 🎉</h3>
                <p style="margin: 0; font-size: 16px;">Semua jawaban Anda benar. Anda mendapatkan <b>Nilai: 100</b>!</p>
            </div>
            """

  # JIKA TOMBOL SELANJUTNYA DIKLIK
  if request.method == "POST" and "tombol_selanjutnya" in request.form:
    show_soal = "true"

  # JIKA TOMBOL KEMBALI DIKLIK
  if request.method == "POST" and "tombol_kembali" in request.form:
    show_soal = "false"

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
            .edit-box {{ background: #fff3cd; padding: 15px; border-radius: 6px; margin-bottom: 20px; border: 1px solid #ffeeba; }}
            .edit-box label {{ display: block; margin-top: 8px; font-weight: bold; font-size: 13px; }}
            .edit-box input, .edit-box select {{ width: 95%; padding: 6px; margin-top: 4px; border: 1px solid #ccc; border-radius: 4px; }}
            .button-group {{ display: flex; gap: 10px; margin-bottom: 20px; }}
            .btn {{ padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer; text-decoration: none; font-weight: bold; text-align: center; font-size: 14px; }}
            .btn-telu {{ background: #b30000; color: white; flex: 1; }}
            .btn-next {{ background: #0070f3; color: white; flex: 1; }}
            .btn-back {{ background: #6c757d; color: white; width: 100%; padding: 10px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; margin-top: 15px; }}
            .soal-box {{ border-top: 2px dashed #ccc; padding-top: 20px; margin-top: 20px; }}
            .soal {{ margin-bottom: 15px; padding: 10px; border-bottom: 1px solid #eee; }}
            input[type="number"] {{ padding: 6px; width: 80px; margin-top: 5px; }}
            .btn-submit {{ background: #28a745; color: white; width: 100%; padding: 12px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; }}
        </style>
    </head>
    <body>
        <div class="container">
            
            {notifikasi_sukses}

            <h2>👋 Selamat Datang!</h2>
            
            <!-- Tampilan Biodata Atas -->
            <div class="biodata">
                <p><b>Nama:</b> {nama_user}</p>
                <p><b>Universitas:</b> {univ_user}</p>
                <p><b>Status:</b> <span class="status">● {status_user}</span></p>
            </div>

            <form method="POST">
                <!-- Status halaman kuis -->
                <input type="hidden" name="show_soal" value="{show_soal}">
  """

  # KONDISI JIKA SEDANG DI HALAMAN UTAMA (MENU AWAL)
  if show_soal == "false":
    html_page += f"""
                <div class="edit-box">
                    <h4 style="margin:0;">⚙️ Pengaturan Profil:</h4>
                    <label>Ubah Nama:</label>
                    <input type="text" name="nama_user" value="{nama_user}">
                    
                    <label>Ubah Universitas:</label>
                    <input type="text" name="univ_user" value="{univ_user}">
                    
                    <label>Ubah Status:</label>
                    <select name="status_user">
                        <option value="Aktif" {"selected" if status_user == "Aktif" else ""}>Aktif</option>
                        <option value="Tidak Aktif" {"selected" if status_user == "Tidak Aktif" else ""}>Tidak Aktif</option>
                        <option value="Cuti" {"selected" if status_user == "Cuti" else ""}>Cuti</option>
                    </select>
                </div>
                
                <div class='button-group'>
                    <a href='https://telkomuniversity.ac.id' target='_blank' class='btn btn-telu'>🌐 Web Tel U</a>
                    <button type='submit' name='tombol_selanjutnya' class='btn btn-next'>➡️ Selanjutnya</button>
                </div>
    """

  # KONDISI JIKA SEDANG DI HALAMAN SOAL KUIS
  if show_soal == "true":
    html_page += f"""
                <!-- Mengunci data nama agar tidak hilang saat Cek Jawaban ditekan -->
                <input type="hidden" name="nama_user" value="{nama_user}">
                <input type="hidden" name="univ_user" value="{univ_user}">
                <input type="hidden" name="status_user" value="{status_user}">

                <div class="soal-box">
                    <h3>📝 Kuis Matematika If-Else</h3>
                    
                    <div class="soal">
                        <p><b>Soal 1:</b> Berapakah 5 + 7?</p>
                        <input type="number" name="soal1" value="{jawab1}" required> {hasil_soal1}
                    </div>

                    <div class="soal">
                        <p><b>Soal 2:</b> Berapakah 8 x 5?</p>
                        <input type="number" name="soal2" value="{jawab2}" required> {hasil_soal2}
                    </div>

                    <div class="soal">
                        <p><b>Soal 3:</b> Berapakah 25 : 5?</p>
                        <input type="number" name="soal3" value="{jawab3}" required> {hasil_soal3}
                    </div>

                    <br>
                    <button type="submit" name="cek_jawaban" class="btn btn-submit">Cek Jawaban</button>
                    <button type="submit" name="tombol_kembali" class="btn btn-back">⬅️ Kembali ke Menu Awal</button>
                </div>
    """

  html_page += """
            </form>
        </div>
    </body>
    </html>
  """

  return html_page


if __name__ == "__main__":
  app.run(debug=True)