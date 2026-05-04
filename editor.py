import cv2 
import numpy as np 

def zavantazhyty_photo(shliach):
    photo_orig = cv2.imdecode(np.fromfile(shliach, dtype=np.uint8), cv2.IMREAD_COLOR)
    photo_rgb = cv2.cvtColor(photo_orig, cv2.COLOR_BGR2RGB)
    return photo_rgb

def gray_photo(photo):
    photo_gray = cv2.cvtColor(photo, cv2.COLOR_RGB2GRAY)
    return photo_gray   

#яскравість
def zminy_yaskravist(photo, znachennya):
    photo_yaskravist = cv2.convertScaleAbs(photo, alpha=1, beta=znachennya)
    return photo_yaskravist 

def zminy_rozmir(photo, shyryna, vysota):
    rozmir = cv2.resize(photo, (shyryna, vysota))
    return rozmir  

def dzerkalo(photo):
    dzerkal_photo = cv2.flip(photo, 1)
    return dzerkal_photo

def negativ(photo):
    photo_neg = cv2.bitwise_not(photo)
    return photo_neg    

def povernuty(photo):
    photo_povern = cv2.rotate(photo, cv2.ROTATE_90_CLOCKWISE)
    return photo_povern

def zminy_kontrast(photo, znachennya):
    kontrast = cv2.convertScaleAbs(photo, alpha=znachennya, beta=0)
    return kontrast

def malunok(photo):
    gray = cv2.cvtColor(photo, cv2.COLOR_RGB2GRAY)
    invert = cv2.bitwise_not(gray)
    blurred =cv2.GaussianBlur(invert, (15,15), 0)
    invert_blur = cv2.bitwise_not(blurred)
    result = cv2.divide(gray, invert_blur, scale=256)
    return result   

def rozmyttya(photo):
    photo_rozmyv = cv2.GaussianBlur(photo, (51,51), 0)
    return photo_rozmyv 

def piksel(photo):
    vysota, shyryna = photo.shape[:2]
    malenke = cv2.resize(photo, (60,60))
    result = cv2.resize(malenke, (shyryna, vysota), interpolation=cv2.INTER_NEAREST)
    return result

def sepia(photo, k=1.0):
    matrix = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])   
    matrix_sepia = cv2.transform(photo, matrix) 
    matrix_sepia = np.clip(matrix_sepia, 0, 255).astype(np.uint8)
    matrix_img = cv2.addWeighted(photo, 1-k, matrix_sepia, k, 0)
    return matrix_img

def defect_krai(photo):
    gray_color = cv2.cvtColor(photo, cv2.COLOR_RGB2GRAY)
    result = cv2.Canny(gray_color, 50, 100)
    return result

def akvarel(photo):
    blur = cv2.bilateralFilter(photo, 15, 100, 100)
    result = cv2.medianBlur(blur, 5)
    return result 

def emboss(photo):
    kernel = np.array([[-2, -1, 0], [-1,1,0], [0,1,2]]) 
    photo_emboss = cv2.filter2D(photo, -1, kernel) 
    return photo_emboss 

def teplyi_color(photo, znachennya):
    r, g, b = cv2.split(photo)
    r = cv2.add(r, znachennya)
    g = cv2.add(g, znachennya//3)
    b = cv2.subtract(b, znachennya // 2)
    result = cv2.merge([r, g, b])
    return result   

def cholodnyi_color(photo, znachennya):
    r, g, b = cv2.split(photo)
    b = cv2.add(b, znachennya)
    r = cv2.add(r, znachennya//2)
    g = cv2.subtract(g, znachennya // 3)
    result = cv2.merge([r, g, b])
    return result  

def shum(photo, znachennya):
    noise = np.random.randint(0, znachennya, photo.shape, dtype=np.uint8)
    result = cv2.add(photo, noise)
    return result 

def rizkist(photo):
    kernel = np.array([[0, -1, 0], [-1, 5, -1 ], [0, -1, 0]]) 
    result = cv2.filter2D(photo, -1, kernel)
    return result 

def posteryzacja(photo, znachennya):
    result = (photo//znachennya)*znachennya
    return result.astype(np.uint8)  

def vinetka(photo, znachennya):
    rows, cols = photo.shape[:2]
    kernel_x = cv2.getGaussianKernel(cols, cols * znachennya)
    kernel_y = cv2.getGaussianKernel(rows, rows * znachennya)
    mask = kernel_y * kernel_x.T
    mask = mask / mask.max()
    result = photo.copy().astype(np.float64)
    for i in range(3):
        result[:,:,i] = result[:,:,i] * mask
    return result.astype(np.uint8)


        


