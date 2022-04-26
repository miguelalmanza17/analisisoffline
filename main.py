from medusa import meeg
from medusa import components
import glob as glob
import matplotlib.pyplot as plt
import scipy.signal as scs
from medusa.frequency_filtering import FIRFilter
import medusa.spatial_filtering as msf


# def prepro(name):
#     print('dentro')
#     file = components.Recording.load_from_bson(name)
#     print(name)
#
#     # temporal
#     plt.plot(file.eeg.times, file.eeg.signal)
#     plt.show()
#
#     # psd
#     nperseg = 1000  # numero de muestras por segundo que se
#     noverlap = int(0.75 * 1000)
#     nfft = nperseg
#     f, psd = scs.welch(file.eeg.signal[:, 0], fs=file.eeg.fs, nperseg=nperseg, noverlap=noverlap, nfft=nfft)
#     # estamos cogiendo solo un canal, tendriamos que hacerlo con todos y poner las graficas una esncima de otras (con unoffset)
#     plt.plot(f, psd)
#     plt.show()
#
#     fir = FIRFilter(order=1000,
#                     cutoff=(1, 30),
#                     btype='bandpass')
#     fir.fit(fs=file.eeg.fs)
#     filtered_signal = fir.transform(file.eeg.signal)
#     filtered_signal = msf.car(filtered_signal)
#
#     nperseg = 1000
#     noverlap = int(0.75 * 1000)
#     nfft = nperseg
#     f, psd = scs.welch(filtered_signal[:, 0], fs=file.eeg.fs, nperseg=nperseg, noverlap=noverlap, nfft=nfft)
#     plt.plot(f, psd)
#     plt.show()


# --------------------------------------------------------------------------------------
# Guardamos la ruta de todos los archivos .bson para guardarlos en file
path = glob.glob('data/miguel/go-nogo/**' )

# prepro(path[0])
# SI GUARDO FILE EN LA FUNCION NO ME APARECE EN LA VENTANA DE ABAJO,
# SI LO GUARDO DESDE AQUI SI QUE APARECE

# for i in range(len(path)):
file = components.Recording.load_from_bson(path[0])
# file2 = components.Recording.load_from_bson(path[1])
# file3 = components.Recording.load_from_bson(path[2])
# file4 = components.Recording.load_from_bson(path[3])
# file5 = components.Recording.load_from_bson(path[4])
# file6 = components.Recording.load_from_bson(path[5])
# file7 = components.Recording.load_from_bson(path[6])
# file8 = components.Recording.load_from_bson(path[7])

# temporal
plt.plot(file.eeg.times, file.eeg.signal)
plt.show()

# psd
nperseg = 1000 #numero de muestras por segundo que se
noverlap = int(0.75*1000)
nfft = nperseg
f, psd = scs.welch(file.eeg.signal[:, 0], fs=file.eeg.fs, nperseg=nperseg, noverlap=noverlap, nfft=nfft)
# estamos cogiendo solo un canal, tendriamos que hacerlo con todos y poner las graficas una esncima de otras (con unoffset)
plt.plot(f, psd)
plt.show()

fir = FIRFilter(order=1000,
                cutoff=(1, 30),
                btype='bandpass')
fir.fit(fs=file.eeg.fs)
filtered_signal = fir.transform(file.eeg.signal)
filtered_signal = msf.car(filtered_signal)

print('------------------')
print(filtered_signal)

nperseg = 1000
noverlap = int(0.75*1000)
nfft = nperseg
f, psd = scs.welch(filtered_signal[:,0], fs=file.eeg.fs, nperseg=nperseg, noverlap=noverlap, nfft=nfft)
plt.plot(f, psd)
plt.show()

plt.plot((filtered_signal[:,0]))
plt.show()
plt.plot((filtered_signal[:,1]+50))
plt.show()
plt.plot((filtered_signal[:,3]+100))
plt.show()
plt.plot((filtered_signal[:,4]+150))
plt.show()
plt.plot((filtered_signal[:,5]+200))
plt.show()
plt.plot((filtered_signal[:,6]+250))
plt.show()
plt.plot((filtered_signal[:,7]+300))
plt.show()


# preprocesado = dict()
# preprocesado['signal'] = filtered_signal
# preprocesado['times'] = file.eeg.times
# preprocesado['fs'] = filtered_signal
# preprocesado['signal'] = filtered_signal
# #
# files = list()
# files.append()



# for i in range(file.eeg.signal.shape[1]):
#
#     print(i)





# path = "data/miguel/22-04-2022_125932.app.bson"
# file = components.Recording.load_from_bson(path)

# file.eeg.signal

#
# # temporal
# plt.plot(file.eeg.times, file.eeg.signal)
# plt.show()
#
# # psd
# nperseg = 1000
# noverlap = int(0.75*1000)
# nfft = nperseg
# f, psd = scs.welch(file.eeg.signal[:, 0], fs=file.eeg.fs, nperseg=nperseg, noverlap=noverlap, nfft=nfft)
# plt.plot(f, psd)
# plt.show()
#
# fir = FIRFilter(order=1000,
#                 cutoff=(1, 30),
#                 btype='bandpass')
# fir.fit(fs=file.eeg.fs)
# filtered_signal = fir.transform(file.eeg.signal)
# filtered_signal = msf.car(filtered_signal)
#
# nperseg = 1000
# noverlap = int(0.75*1000)
# nfft = nperseg
# f, psd = scs.welch(filtered_signal[:,0], fs=file.eeg.fs, nperseg=nperseg, noverlap=noverlap, nfft=nfft)
# plt.plot(f, psd)
# plt.show()
#
#
#
# preprocesado = dict()
# preprocesado['signal'] = filtered_signal
# preprocesado['times'] = file.eeg.times
# preprocesado['fs'] = filtered_signal
# preprocesado['signal'] = filtered_signal
#
# files = list()
# files.append()

