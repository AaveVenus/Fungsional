def konversi(j=0):
    def minggu(w=0):
        def hari(d=0):
            def jam(h=0):
                def menit(m=0):
                    return (w * 7 * 24 * 60) + (d * 24 * 60) + (h * 60) + m
                return menit
            return jam
        return hari
    return minggu(j)

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

OutputData = []

for item in data:
    split = item.split()
    minggu = int(split[0])
    hari = int(split[2])
    jam = int(split[4])
    menit = int(split[6])
    konver = konversi(minggu)(hari)(jam)(menit)
    OutputData.append(konver)

print(OutputData)
