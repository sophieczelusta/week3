import wx
import os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import ctypes


EXIT_ID = 1
SAVE_ID = 2
OPEN_ID = 3

def lighten(pic,amount):
    metaporph = Image.open(pic)
    metaporph = metaporph.convert("RGBA")
    pixels = [(int(r*amount),int(g*amount),int(b*amount)) for (r,g,b,a) in metaporph.getdata()]
    metaporph.putdata(pixels)
    metaporph.save('temp.png')

def darken(pic,amount):
    metaporph = Image.open(pic)
    metaporph = metaporph.convert("RGBA")
    pixels = [(int(r*0.8),int(g*0.8),int(b*0.8)) for (r,g,b,a) in metaporph.getdata()]
    metaporph.putdata(pixels)
    metaporph.save('temp.png')

def greyscale(pic):
    metaporph = Image.open(pic)
    metaporph = metaporph.convert("RGBA")
    pixels = [(int((r+g+b)/3),int((r+g+b)/3),int((r + g + b) / 3)) for (r,g,b,a) in metaporph.getdata()]
    metaporph.putdata(pixels)
    metaporph.save('temp.png')

def solarer(x):
    if x < 128:
        x = 255 - x
        return x
    else:
        return x
def solarize(pic):
    metaporph = Image.open(pic)
    metaporph = metaporph.convert("RGBA")
    pixels = [(solarer(r),solarer(g),solarer(b)) for (r,g,b,a) in metaporph.getdata()]
    metaporph.putdata(pixels)
    metaporph.save('temp.png')

def posterer(x):
    if x <= 63:
        x = 0
        return x
    elif x > 63 and x <= 127:
        x = 100
        return x
    elif x > 127 and x <= 191:
        x = 150
        return x
    elif x > 191 and x <= 255:
        x = 200
        return x
    else:
        print("broken")

def posterize(pic):
    metaporph = Image.open(pic)
    metaporph = metaporph.convert("RGBA")
    pixels = [(posterer(r),posterer(g),posterer(b)) for (r,g,b,a) in metaporph.getdata()]
    metaporph.putdata(pixels)
    metaporph.save('temp.png')



class Photoshop(wx.Frame):

    def __init__(self,parent,title):
        super(Photoshop, self).__init__(parent,title=title,
        size=(1080,750))

        #self.frame = wx.Frame(None,title='Please let this work')
        self.PhotoMaxSize = 400


        self.InitUI()
        self.Centre()

    def InitUI(self):

        menubar = wx.MenuBar()
        filetab = wx.Menu() #set file and menu

        openfile = wx.MenuItem(filetab,OPEN_ID,'&Open File\tCtrl+O')
        filetab.Append(openfile)

        saveitem = wx.MenuItem(filetab,SAVE_ID,'&Save File\tCtrl+S')
        filetab.Append(saveitem) #add save to filetab

        filetab.AppendSeparator()

        quitprogram = wx.MenuItem(filetab,EXIT_ID,'&Quit\tCtrl+Q')
        filetab.Append(quitprogram) #create a filetab with qmi


        self.Bind(wx.EVT_MENU,self.onExit,id=EXIT_ID) #qmi exits the app
        self.Bind(wx.EVT_MENU,self.saveAs,id=SAVE_ID)

        menubar.Append(filetab, '&File')
        self.SetMenuBar(menubar) #adds the filetab to the menu and sets the menu as menubar (defined above)

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(25,20)

        openbutton = wx.Button(panel, label="Open",size=(90,25))
        sizer.Add(openbutton,pos=(0,0),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=10)

        self.photofind = wx.TextCtrl(panel,size=(900,25))
        sizer.Add(self.photofind,pos=(0,1),span=(0,15),flag=wx.TOP|wx.RIGHT,border=10)
        self.Bind(wx.EVT_BUTTON,self.onBrowse)

        self.nameofnew = wx.TextCtrl(panel,size=(900,25))
        sizer.Add(self.nameofnew,pos=(2,1),span=(2,15),flag=wx.TOP|wx.RIGHT,border=10)

        savebutton = wx.Button(panel,label="Save As:",size=(90,25))
        sizer.Add(savebutton,pos=(2,0),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=10)
        self.Bind(wx.EVT_BUTTON,self.saveAs,savebutton)

        self.img = wx.EmptyImage(400,400)
        self.imageCtrl = wx.StaticBitmap(panel,wx.ID_ANY,wx.BitmapFromImage(self.img))
        sizer.Add(self.imageCtrl,pos=(4,0),span=(21,8),flag=wx.LEFT,border=30)

        self.edited = wx.EmptyImage(400,400)
        self.editedCtrl = wx.StaticBitmap(panel,wx.ID_ANY,wx.BitmapFromImage(self.edited))
        sizer.Add(self.editedCtrl,pos=(4,8),span=(21,20))

        image = Image.new('RGBA',(400,400))
        image.save('temp.png')



        adjustments = ['Lighten','Darken','Greyscale','Solarize','Posterize']
        dropdown = wx.ComboBox(panel,id=wx.ID_ANY,size=(600,28),choices=adjustments,
                    style=wx.CB_READONLY)
        sizer.Add(dropdown,pos=(1,3),span=(1,17))
        dropdown.Bind(wx.EVT_COMBOBOX,self.onSelect)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizer(sizer)

    def onSelect(self,e):
        type = e.GetString()
        filepath = self.photofind.GetValue()
        picture = wx.Image(filepath,wx.BITMAP_TYPE_ANY)
        if type == "Lighten":
            newimage = lighten(filepath,3)
            self.showNew()
        elif type == "Darken":
            newimage = darken(filepath,3)
            self.showNew()
        elif type == "Greyscale":
            newimage = greyscale(filepath)
            self.showNew()
        elif type == "Solarize":
            newimage = solarize(filepath)
            self.showNew()
        elif type == "Posterize":
            newimage = posterize(filepath)
            self.showNew()
        else:
            print("You have no mouse conto=ro")



    def onBrowse(self,e):
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",
                                wildcard=wildcard,
                                style=wx.FD_OPEN)

        if dialog.ShowModal() == wx.ID_OK:
            self.photofind.SetValue(dialog.GetPath())
        dialog.Destroy()
        self.onView()

    def onView(self):
        filepath = self.photofind.GetValue()
        img = wx.Image(filepath,wx.BITMAP_TYPE_ANY)
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        img = img.Scale(NewW,NewH)

        self.imageCtrl.SetBitmap(wx.BitmapFromImage(img))

    def showNew(self):
        newimage = wx.Image(os.path.abspath('temp.png'), wx.BITMAP_TYPE_ANY)#.ConvertToBitmap()
        W = newimage.GetWidth()
        H = newimage.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        newimage = newimage.Scale(NewW,NewH)

        self.editedCtrl.SetBitmap(wx.BitmapFromImage(newimage))
        path = os.path.abspath('temp.png')



    def onExit(self,e):
        os.remove('temp.png')
        self.Close()

    def saveAs(self,e):
        newname = self.nameofnew.GetValue()
        filepathtonew = os.path.abspath('temp.png')
        new = Image.open(filepathtonew)

        new.save(newname)
        os.remove(filepathtonew)
        ctypes.windll.user32.MessageBoxW(0, "Your image has been saved as " + newname + ".", "Saved", 0)





def main():
    app = wx.App()
    editor = Photoshop(None, title="Photostore")
    editor.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
