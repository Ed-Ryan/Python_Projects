#Call all imports
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy.stats import mode
from scipy.ndimage import interpolation
import warnings 
warnings.filterwarnings('ignore') #found this on Stackoverflow
#Right from Example 7.4 in week 4
darkSHead = fits.getheader("QUESTdata/darks/dark_180.C22.fits")
darkS =np.transpose(np.array(fits.getdata("QUESTdata/darks/dark_180.C22.fits"), float))
print(darkSHead['EXPTIME'])
print(darkSHead['IMAGETYP'])
darkFHead = fits.getheader("QUESTdata/darks/dark_10.C22.fits")
darkF =np.transpose(np.array(fits.getdata("QUESTdata/darks/dark_10.C22.fits"), float))
print(darkFHead['EXPTIME'])
print(darkFHead['IMAGETYP'])

BiasOverScan = []
fList = []
ExpID = [1708, 1759, 1853, 1944, 2035, 2127, 2217, 2309, 2401]
for expId in ExpID:
    head = fits.getheader("QUESTdata/flats/2013091023%de.C22.fits" % expId)
    rawFData = np.transpose(fits.getdata("QUESTdata/flats/2013091023%de.C22.fits" % expId))
    rawFData.shape
    BiasPerRow = np.median(rawFData[637:636, :], axis=0)
    BiasOverScan.append(BiasPerRow)
    BiasPerRow.shape
    rawFData -= darkF
    fData = rawFData[0:637, :]
    fData.shape
    for i in range(2400):
        fData[0:637, i] -= BiasPerRow[i]
    fList.append(fData)
    print(head['EXPTIME'])
    print(head['IMAGETYP'])
ExpID = [457, 548, 641, 732, 822, 915]
for expId in ExpID:
    head = fits.getheader("QUESTdata/flats/20130911095%dm.C22.fits" % expId)
    rawFData = np.transpose(fits.getdata("QUESTdata/flats/20130911095%dm.C22.fits" % expId))
    rawFData.shape
    BiasPerRow = np.median(rawFData[637:636, :], axis=0)
    BiasPerRow.shape
    rawFData -= darkF
    flatData = rawFData[0:637, :]
    flatData.shape
    for i in range(2400):
        flatData[0:637, i] -= BiasPerRow[i]
    fList.append(fData)
    print(head['EXPTIME'])
    print(head['IMAGETYP'])

sHead1 = fits.getheader("QUESTdata/science/20130910234901s.C22.fits")
sRawData1 = np.transpose(np.array(fits.getdata("QUESTdata/science/20130910234901s.C22.fits"), float))
sRawData1.shape
BiasPerRow = (np.median(sRawData1[600:636, :], axis=0))
BiasPerRow.shape
sRawData1 -= darkS
sImage1 = sRawData1[0:637, :]
sImage1.shape
for i in range(2400):
    sImage1[0:637, i] -= BiasPerRow[i]

sHead2 = fits.getheader("QUESTdata/science/20130911020246s.C22.fits")
sRawData2 = np.transpose(np.array(fits.getdata("QUESTdata/science/20130911020246s.C22.fits"), float))
sRawData2.shape
BiasPerRow = (np.median(sRawData2[600:636, :], axis=0))
BiasPerRow.shape
sRawData2 -= darkS
sImage2 = sRawData2[0:637, :]
sImage2.shape
for i in range(2400):
    sImage2[0:637, i] -= BiasPerRow[i]

sHead3 = fits.getheader("QUESTdata/science/20130911040543s.C22.fits")
sRawData3 = np.transpose(np.array(fits.getdata("QUESTdata/science/20130911040543s.C22.fits"), float))
sRawData3.shape
BiasPerRow = (np.median(sRawData3[600:636, :], axis=0))
BiasPerRow.shape
sRawData3 -= darkS
sImage3 = sRawData3[0:637, :]
sImage3.shape
for i in range(2400):
    sImage3[0:637, i] -= BiasPerRow[i]

mFlat = np.median(np.array(fList), axis=0)
nFlat = mFlat / np.median(mFlat.flatten())
minp = min(nFlat.flatten())
maxp = max(nFlat.flatten())
rng = int(maxp-minp)
plt.xlabel("Pixel sensetivity")
plt.ylabel("Count")
plt.title("Normalised Master Flat Histogram")
plt.hist(nFlat.flatten(), bins=rng, range=(minp,maxp))
plt.savefig("coursework1Histo.png")
plt.show()
hdu = fits.PrimaryHDU(np.transpose(nFlat))
hdu.header.add_comment("Normalised bias of dark median")
fits.writeto('masterFlat.fits', hdu.data, hdu.header, output_verify='ignore', overwrite=True)

calS1 = sImage1/nFlat
calS1 = np.transpose(calS1[0:600, :])
fits.writeto('calS1.fits', calS1, sHead1, output_verify='ignore', overwrite=True)
calS2 = np.transpose(sImage2/nFlat)
fits.writeto('calS2.fits', calS2, sHead2, output_verify='ignore', overwrite=True)
calS3 = np.transpose(sImage3/nFlat)
fits.writeto('calS3.fits', calS3, sHead3, output_verify='ignore', overwrite=True)

skyval,loc = mode(calS1.flatten())
print(skyval)
finalS1 = calS1 - skyval
fits.writeto('finalSImage1.fits', finalS1, sHead1, output_verify='ignore', overwrite=True)
skyval,loc = mode(calS2.flatten())
print(skyval)
finalS2 = calS2 - skyval
fits.writeto('finalSImage2.fits', finalS2, sHead2, output_verify='ignore', overwrite=True)
skyval,loc = mode(calS3.flatten())
print(skyval)
finalS3 = calS3 - skyval
fits.writeto('finalSImage3.fits', finalS3, sHead3, output_verify='ignore', overwrite=True)

shift2 = interpolation.shift(finalS2, (16, -3))
shift3 = interpolation.shift(finalS3, (40, -6))
fits.writeto("shiftImage2.fits", shift2, sHead2, output_verify='ignore', overwrite=True)
fits.writeto("shiftImage3.fits", shift3, sHead3, output_verify='ignore', overwrite=True)
