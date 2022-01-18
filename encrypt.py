#encrypt kalimat

list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0','P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e','f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' 'z' ,' ','.']

input = input ("Masukkan kata yang ingin di enkripsi: ")
string = ""
pindah = 23
for x in range(len(input)):
    sementara = list.index(input[x])+pindah
    string=string+list[sementara%64]

print("\nPlainText: ", input)
print("\nEnkripsi: ", string)