"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus = {'anak': 'son', 'istri': 'wife'}

print(kamus['anak'])
print(kamus['istri'])

print('\nData ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar lokasi pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal' : '2021-02-16',
    'driver_list' : [
        {'nama' : 'eko', 'jarak' : 15},
        {'nama' : 'dwi', 'jarak' : 55},
        {'nama' : 'tri', 'jarak' : 95},
        {'nama' : 'catur', 'jarak' : 548}
    ]

}

print(data_dari_server_gojek)
print(f"\ndata driver di sekitar sini{data_dari_server_gojek['driver_list']}")
print(f"\ndriver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"\ndriver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"\ndriver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")