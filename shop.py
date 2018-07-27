import wx
import os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps


EXIT_ID = 1
SAVE_ID = 2
OPEN_ID = 3

def lighten(pic,amount):
    img = Image.open(pic)
    img = img.convert("RGBA")
    pixels = [(int(r*amount),int(g*amount),int(b*amount)) for (r,g,b,a) in img.getdata()]
    img.putdata(pixels)


class Photoshop(wx.Frame):

    super(Photoshop, self).__init__(parent,title=title,
    size=(1050,800))

    self.frame = wx.Frame(None,title='Please let this work')
    self.PhotoMaxSize = 400


    self.Centre()

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

    menubar.Append(filetab, '&File')
    self.SetMenuBar(menubar) #adds the filetab to the menu and sets the menu as menubar (defined above)

    panel = wx.Panel(self)
    sizer = wx.GridBagSizer(25,20)

    openbutton = wx.Button(panel, label="Open",size=(90,28))
    sizer.Add(openbutton,pos=(0,0),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=10)

    self.photofind = wx.TextCtrl(panel)
    sizer.Add(self.photofind,pos=(0,1),span=(0,17),flag=wx.EXPAND|wx.TOP|wx.RIGHT|wx.BOTTOM,border=10)
    self.Bind(wx.EVT_BUTTON,self.onBrowse)

    adjustments = ['Lighten','Darken','Greyscale','Solarize','Posterize']
    dropdown = wx.ComboBox(panel,id=wx.ID_ANY,size=(600,28),choices=adjustments,
                style=wx.CB_READONLY)
    sizer.Add(dropdown,pos=(1,3),span=(1,17))
    dropdown.Bind(wx.EVT_COMBOBOX,self.onSelect)

    img = wx.EmptyImage(400,400)
    self.imageCtrl = wx.StaticBitmap(panel,wx.ID_ANY,wx.BitmapFromImage(img))
    sizer.Add(self.imageCtrl,pos=(2,0),span=(20,9),flag=wx.LEFT,border=20)

    edited = wx.EmptyImage(400,400)
    self.editedCtrl = wx.StaticBitmap(panel,wx.ID_ANY,wx.BitmapFromImage(edited))
    sizer.Add(self.editedCtrl,pos=(2,9),span=(20,20))





    sizer.AddGrowableCol(1)
    sizer.AddGrowableRow(2)
    panel.SetSizer(sizer)

    def onSelect(self,e):
        print("no")



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
        self.panel.Refresh()




    def onExit(self,e):
        self.Close()




def main():
    app = wx.App()
    editor = Photoshop(None, title="Photostore")
    editor.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
