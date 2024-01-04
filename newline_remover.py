import streamlit as st

def hapus_garis_baru(teks):
  """Menghapus semua garis baru pada teks"""
  return teks.replace("\n", " ")

def main():
  """Fungsi utama"""
  # Judul aplikasi
  st.title("Hapus Semua Garis Baru")

  # Input teks
  teks_input = st.text_area("Masukkan teks", placeholder="Masukkan teks di sini")

  # Output teks
  teks_output = hapus_garis_baru(teks_input)
  st.code(teks_output, language="python")
  st.markdown("teks telah di copy")

  # Tombol run
  if st.button("Run"):
    pass

if __name__ == "__main__":
  main()
